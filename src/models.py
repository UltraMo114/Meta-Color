"""
Color difference models using colour-science library

This module provides a unified interface for different color difference formulas.
For XYZ inputs, this project requires using each sample-pair's own reference
whitepoint (XYZw) from the dataset rather than assuming a fixed default (e.g. D65).
"""

from abc import ABC, abstractmethod
import numpy as np
import colour


_EPSILON = 216 / 24389  # (6/29)^3
_KAPPA = 24389 / 27


def xyz_to_lab_user_whitepoint(xyz: np.ndarray, whitepoint_xyz: np.ndarray) -> np.ndarray:
    """
    Convert CIE XYZ to CIE Lab using an explicit reference whitepoint XYZw (both same scale).

    Supports shape (3,) or (N, 3) for both inputs. Broadcasting is allowed for a
    single whitepoint (3,) with many XYZ rows (N, 3).
    """
    xyz_arr = np.asarray(xyz, dtype=float)
    wp_arr = np.asarray(whitepoint_xyz, dtype=float)

    if xyz_arr.shape[-1] != 3 or wp_arr.shape[-1] != 3:
        raise ValueError("xyz and whitepoint_xyz must end with 3 components (X, Y, Z)")

    if np.any(wp_arr == 0):
        raise ValueError("whitepoint_xyz must be non-zero in all components")

    t = xyz_arr / wp_arr
    f = np.where(t > _EPSILON, np.cbrt(t), (_KAPPA * t + 16.0) / 116.0)

    fx = f[..., 0]
    fy = f[..., 1]
    fz = f[..., 2]

    L = 116.0 * fy - 16.0
    a = 500.0 * (fx - fy)
    b = 200.0 * (fy - fz)

    return np.stack([L, a, b], axis=-1)


class ColorDifferenceModel(ABC):
    """Abstract base class for color difference models"""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def predict(self,
                reference: np.ndarray,
                sample: np.ndarray,
                input_type: str = 'XYZ',
                whitepoint: np.ndarray | None = None) -> float:
        """
        Calculate color difference between reference and sample

        Parameters
        ----------
        reference : np.ndarray
            Reference color (XYZ in 0-100 range or Lab)
        sample : np.ndarray
            Sample color (XYZ in 0-100 range or Lab)
        input_type : str
            Input color space: 'XYZ' or 'Lab'
        whitepoint : np.ndarray | None
            Reference whitepoint XYZw for XYZ inputs (shape: (3,)).
            Required when input_type='XYZ' for dataset-based evaluation.

        Returns
        -------
        float
            Color difference value
        """
        pass

    def _ensure_lab(self,
                    color: np.ndarray,
                    input_type: str,
                    whitepoint_xyz: np.ndarray | None) -> np.ndarray:
        """
        Convert input to Lab if needed

        Parameters
        ----------
        color : np.ndarray
            Input color
        input_type : str
            'XYZ' or 'Lab'
        whitepoint_xyz : np.ndarray | None
            Reference whitepoint XYZw for XYZ to Lab conversion.

        Returns
        -------
        np.ndarray
            Lab values
        """
        if input_type == 'XYZ':
            if whitepoint_xyz is None:
                raise ValueError("XYZ input requires whitepoint (XYZw); refusing to assume a default illuminant.")
            return xyz_to_lab_user_whitepoint(color, whitepoint_xyz)
        elif input_type == 'Lab':
            return color
        else:
            raise ValueError(f"Unknown input_type: {input_type}. Use 'XYZ' or 'Lab'")

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"


class CIELAB(ColorDifferenceModel):
    """CIELAB color difference formula (ΔE*ab)"""

    def __init__(self):
        super().__init__('CIELAB')

    def predict(self,
                reference: np.ndarray,
                sample: np.ndarray,
                input_type: str = 'XYZ',
                whitepoint: np.ndarray | None = None) -> float:
        """
        Calculate CIELAB ΔE*ab color difference

        Parameters
        ----------
        reference : np.ndarray
            Reference color (XYZ in 0-100 range or Lab)
        sample : np.ndarray
            Sample color (XYZ in 0-100 range or Lab)
        input_type : str
            Input color space: 'XYZ' or 'Lab'
        whitepoint : np.ndarray | None
            Reference whitepoint XYZw for XYZ inputs (shape: (3,)).

        Returns
        -------
        float
            CIELAB ΔE*ab value
        """
        lab_ref = self._ensure_lab(reference, input_type, whitepoint)
        lab_sample = self._ensure_lab(sample, input_type, whitepoint)

        # Calculate Euclidean distance in Lab space
        delta_E = np.sqrt(np.sum((lab_sample - lab_ref) ** 2))

        return delta_E


class CIEDE2000(ColorDifferenceModel):
    """CIEDE2000 color difference formula"""

    def __init__(self, kL: float = 1.0, kC: float = 1.0, kH: float = 1.0):
        """
        Initialize CIEDE2000 model

        Parameters
        ----------
        kL : float
            Lightness parametric factor (default: 1.0)
        kC : float
            Chroma parametric factor (default: 1.0)
        kH : float
            Hue parametric factor (default: 1.0)
        """
        super().__init__('CIEDE2000')
        self.kL = kL
        self.kC = kC
        self.kH = kH

    def predict(self,
                reference: np.ndarray,
                sample: np.ndarray,
                input_type: str = 'XYZ',
                whitepoint: np.ndarray | None = None) -> float:
        """
        Calculate CIEDE2000 color difference

        Parameters
        ----------
        reference : np.ndarray
            Reference color (XYZ in 0-100 range or Lab)
        sample : np.ndarray
            Sample color (XYZ in 0-100 range or Lab)
        input_type : str
            Input color space: 'XYZ' or 'Lab'
        whitepoint : np.ndarray | None
            Reference whitepoint XYZw for XYZ inputs (shape: (3,)).

        Returns
        -------
        float
            CIEDE2000 ΔE value
        """
        lab_ref = self._ensure_lab(reference, input_type, whitepoint)
        lab_sample = self._ensure_lab(sample, input_type, whitepoint)

        # Use colour-science's CIEDE2000 implementation
        # Note: colour-science uses different parameter names
        delta_E = colour.difference.delta_E_CIE2000(
            lab_ref, lab_sample,
            textiles=False  # Use default lightness weighting
        )

        return delta_E


class CAM16UCS(ColorDifferenceModel):
    """CAM16-UCS color appearance model for uniform color spaces"""

    def __init__(self,
                 L_A: float = 100.0,
                 Y_b: float = 20.0,
                 surround: str = 'average'):
        """
        Initialize CAM16-UCS model

        Parameters
        ----------
        L_A : float
            Adapting field luminance in cd/m² (default: 100.0)
        Y_b : float
            Relative luminance of background (default: 20.0)
        surround : str
            Surround condition: 'average', 'dim', or 'dark' (default: 'average')
        """
        super().__init__('CAM16-UCS')
        self.L_A = L_A
        self.Y_b = Y_b
        self.surround = colour.VIEWING_CONDITIONS_CIECAM02[surround.capitalize()]

    def predict(self,
                reference: np.ndarray,
                sample: np.ndarray,
                input_type: str = 'XYZ',
                whitepoint: np.ndarray | None = None) -> float:
        """
        Calculate CAM16-UCS color difference

        Parameters
        ----------
        reference : np.ndarray
            Reference color (XYZ in 0-100 range or Lab)
        sample : np.ndarray
            Sample color (XYZ in 0-100 range or Lab)
        input_type : str
            Input color space: 'XYZ' or 'Lab'
        whitepoint : np.ndarray | None
            Reference whitepoint XYZw for XYZ inputs (shape: (3,)).

        Returns
        -------
        float
            CAM16-UCS ΔE value
        """
        if input_type == 'Lab':
            # Lab requires a reference whitepoint; defaulting to D65 is acceptable here.
            if whitepoint is None:
                illuminant_xy = colour.CCS_ILLUMINANTS['CIE 1964 10 Degree Standard Observer']['D65']
                whitepoint_xyz = colour.xy_to_XYZ(illuminant_xy) * 100
            else:
                whitepoint_xyz = np.asarray(whitepoint, dtype=float)
                illuminant_xy = colour.XYZ_to_xy(whitepoint_xyz)

            xyz_ref = colour.Lab_to_XYZ(reference, illuminant=illuminant_xy)
            xyz_sample = colour.Lab_to_XYZ(sample, illuminant=illuminant_xy)
        else:
            if whitepoint is None:
                raise ValueError("XYZ input requires whitepoint (XYZw); refusing to assume a default illuminant.")
            whitepoint_xyz = np.asarray(whitepoint, dtype=float)
            xyz_ref = np.asarray(reference, dtype=float)
            xyz_sample = np.asarray(sample, dtype=float)

        # Scale so that whitepoint Y == 100 (matching MATLAB reference pipeline).
        if float(whitepoint_xyz[1]) == 0.0:
            raise ValueError("whitepoint Y component must be non-zero")
        scale = 100.0 / float(whitepoint_xyz[1])
        XYZ_w = whitepoint_xyz * scale
        xyz_ref = xyz_ref * scale
        xyz_sample = xyz_sample * scale

        # Convert to CAM16 space
        try:
            cam16_ref = colour.XYZ_to_CAM16(
                xyz_ref,
                XYZ_w=XYZ_w,
                L_A=self.L_A,
                Y_b=self.Y_b,
                surround=self.surround
            )
            cam16_sample = colour.XYZ_to_CAM16(
                xyz_sample,
                XYZ_w=XYZ_w,
                L_A=self.L_A,
                Y_b=self.Y_b,
                surround=self.surround
            )

            # Convert to UCS coordinates (J', a', b')
            # CAM16-UCS uses J', aM', bM' coordinates
            Jpapbp_ref = colour.JMh_CAM16_to_UCS_Li2017(
                np.array([cam16_ref.J, cam16_ref.M, cam16_ref.h])
            )
            Jpapbp_sample = colour.JMh_CAM16_to_UCS_Li2017(
                np.array([cam16_sample.J, cam16_sample.M, cam16_sample.h])
            )

            # Calculate Euclidean distance in UCS space
            delta_E = np.sqrt(np.sum((Jpapbp_sample - Jpapbp_ref) ** 2))

        except Exception as e:
            # If CAM16 calculation fails (e.g., for out-of-gamut colors),
            # fall back to CIELAB
            print(f"Warning: CAM16 calculation failed ({e}), using CIELAB fallback")
            cielab = CIELAB()
            delta_E = cielab.predict(reference, sample, input_type, whitepoint=whitepoint)

        return delta_E


class SUCS(ColorDifferenceModel):
    """sUCS colourspace Euclidean distance (Li et al. 2024)."""

    def __init__(self, adaptation_transform: str = "CAT02"):
        super().__init__("sUCS")
        self.adaptation_transform = adaptation_transform

        illuminant_xy = colour.CCS_ILLUMINANTS["CIE 1964 10 Degree Standard Observer"]["D65"]
        self._d65_xyz_domain1 = colour.xy_to_XYZ(illuminant_xy)

    def _delta_sucs_from_xyz(
        self,
        xyz_ref: np.ndarray,
        xyz_sample: np.ndarray,
        whitepoint_xyz: np.ndarray,
    ) -> np.ndarray:
        xyz_ref = np.asarray(xyz_ref, dtype=float)
        xyz_sample = np.asarray(xyz_sample, dtype=float)
        wp = np.asarray(whitepoint_xyz, dtype=float)

        if xyz_ref.shape[-1] != 3 or xyz_sample.shape[-1] != 3 or wp.shape[-1] != 3:
            raise ValueError("reference, sample, and whitepoint must end with 3 components (X, Y, Z)")
        if xyz_ref.shape != xyz_sample.shape:
            raise ValueError(f"reference and sample must have the same shape, got {xyz_ref.shape} and {xyz_sample.shape}")

        if wp.shape != (3,) and wp.shape != xyz_ref.shape:
            raise ValueError(f"whitepoint must have shape (3,) or match XYZ shape; got {wp.shape} for XYZ {xyz_ref.shape}")
        if np.any(wp[..., 1] == 0):
            raise ValueError("whitepoint Y component must be non-zero")

        # Normalize so that source whitepoint has Y=1 (Domain1 requirement).
        scale = 1.0 / wp[..., 1]
        xyz_ref = xyz_ref * scale[..., np.newaxis]
        xyz_sample = xyz_sample * scale[..., np.newaxis]
        wp = wp * scale[..., np.newaxis]

        # Adapt to D65, then convert to sUCS Iab and compute Euclidean distance.
        xyz_ref_d65 = colour.adaptation.chromatic_adaptation_VonKries(
            xyz_ref, wp, self._d65_xyz_domain1, transform=self.adaptation_transform
        )
        xyz_sample_d65 = colour.adaptation.chromatic_adaptation_VonKries(
            xyz_sample, wp, self._d65_xyz_domain1, transform=self.adaptation_transform
        )

        iab_ref = colour.XYZ_to_sUCS(xyz_ref_d65)
        iab_sample = colour.XYZ_to_sUCS(xyz_sample_d65)

        return np.linalg.norm(iab_sample - iab_ref, axis=-1)

    def predict(
        self,
        reference: np.ndarray,
        sample: np.ndarray,
        input_type: str = "XYZ",
        whitepoint: np.ndarray | None = None,
    ) -> float:
        if input_type == "XYZ":
            if whitepoint is None:
                raise ValueError("XYZ input requires whitepoint (XYZw); refusing to assume a default illuminant.")
            return self._delta_sucs_from_xyz(reference, sample, whitepoint)

        if input_type == "Lab":
            # Lab values require a reference whitepoint; if none is provided,
            # assume D65 10-degree to maintain a usable default.
            if whitepoint is None:
                illuminant_xy = colour.CCS_ILLUMINANTS["CIE 1964 10 Degree Standard Observer"]["D65"]
                wp_xyz = self._d65_xyz_domain1
            else:
                wp_xyz_raw = np.asarray(whitepoint, dtype=float)
                if wp_xyz_raw.shape != (3,):
                    raise ValueError("Lab input expects whitepoint of shape (3,) when provided.")
                if float(wp_xyz_raw[1]) == 0.0:
                    raise ValueError("whitepoint Y component must be non-zero")
                illuminant_xy = colour.XYZ_to_xy(wp_xyz_raw)
                wp_xyz = wp_xyz_raw * (1.0 / float(wp_xyz_raw[1]))

            xyz_ref = colour.Lab_to_XYZ(reference, illuminant=illuminant_xy)
            xyz_sample = colour.Lab_to_XYZ(sample, illuminant=illuminant_xy)
            return self._delta_sucs_from_xyz(xyz_ref, xyz_sample, wp_xyz)

        raise ValueError(f"Unknown input_type: {input_type}. Use 'XYZ' or 'Lab'")


# Factory function for easy model creation
def get_model(model_name: str, **kwargs) -> ColorDifferenceModel:
    """
    Get a color difference model by name

    Parameters
    ----------
    model_name : str
        Name of the model: 'CIELAB', 'CIEDE2000', or 'CAM16UCS'
    **kwargs
        Additional arguments for model initialization

    Returns
    -------
    ColorDifferenceModel
        Initialized color difference model

    Examples
    --------
    >>> model = get_model('CIEDE2000', kL=1.0, kC=1.0, kH=1.0)
    >>> dE = model.predict(xyz_ref, xyz_sample, input_type='XYZ', whitepoint=xyzw)
    """
    models = {
        'CIELAB': CIELAB,
        'CIEDE2000': CIEDE2000,
        'CAM16UCS': CAM16UCS,
        'CAM16-UCS': CAM16UCS,
        'SUCS': SUCS,
        'sUCS': SUCS,
    }

    if model_name not in models:
        raise ValueError(f"Unknown model: {model_name}. Available models: {list(models.keys())}")

    return models[model_name](**kwargs)
