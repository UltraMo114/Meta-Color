"""
Color difference models using colour-science library

This module provides a unified interface for different color difference formulas.
All models accept XYZ (0-100 range) or Lab inputs and return color differences.
"""

from abc import ABC, abstractmethod
import numpy as np
import colour


class ColorDifferenceModel(ABC):
    """Abstract base class for color difference models"""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def predict(self,
                reference: np.ndarray,
                sample: np.ndarray,
                input_type: str = 'XYZ') -> float:
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

        Returns
        -------
        float
            Color difference value
        """
        pass

    def _ensure_lab(self,
                    color: np.ndarray,
                    input_type: str,
                    illuminant: np.ndarray = colour.CCS_ILLUMINANTS['CIE 1964 10 Degree Standard Observer']['D65']) -> np.ndarray:
        """
        Convert input to Lab if needed

        Parameters
        ----------
        color : np.ndarray
            Input color
        input_type : str
            'XYZ' or 'Lab'
        illuminant : np.ndarray
            Illuminant for XYZ to Lab conversion (default: D65)

        Returns
        -------
        np.ndarray
            Lab values
        """
        if input_type == 'XYZ':
            # Convert XYZ (0-100) to Lab
            return colour.XYZ_to_Lab(color, illuminant=illuminant)
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
                input_type: str = 'XYZ') -> float:
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

        Returns
        -------
        float
            CIELAB ΔE*ab value
        """
        lab_ref = self._ensure_lab(reference, input_type)
        lab_sample = self._ensure_lab(sample, input_type)

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
                input_type: str = 'XYZ') -> float:
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

        Returns
        -------
        float
            CIEDE2000 ΔE value
        """
        lab_ref = self._ensure_lab(reference, input_type)
        lab_sample = self._ensure_lab(sample, input_type)

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
                input_type: str = 'XYZ') -> float:
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

        Returns
        -------
        float
            CAM16-UCS ΔE value
        """
        # CAM16 requires XYZ input
        if input_type == 'Lab':
            # Convert Lab back to XYZ (assuming D65 illuminant)
            illuminant = colour.CCS_ILLUMINANTS['CIE 1964 10 Degree Standard Observer']['D65']
            xyz_ref = colour.Lab_to_XYZ(reference, illuminant=illuminant)
            xyz_sample = colour.Lab_to_XYZ(sample, illuminant=illuminant)
        else:
            xyz_ref = reference
            xyz_sample = sample

        # Get white point (D65)
        XYZ_w = colour.CCS_ILLUMINANTS['CIE 1964 10 Degree Standard Observer']['D65'] * 100

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
            delta_E = cielab.predict(reference, sample, input_type)

        return delta_E


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
    >>> dE = model.predict(xyz_ref, xyz_sample, input_type='XYZ')
    """
    models = {
        'CIELAB': CIELAB,
        'CIEDE2000': CIEDE2000,
        'CAM16UCS': CAM16UCS,
        'CAM16-UCS': CAM16UCS,
    }

    if model_name not in models:
        raise ValueError(f"Unknown model: {model_name}. Available models: {list(models.keys())}")

    return models[model_name](**kwargs)
