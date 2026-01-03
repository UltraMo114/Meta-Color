"""
Physics verification tests for color difference models

These tests verify that color difference calculations follow basic
physical properties and match expected behavior.
"""

import pytest
import numpy as np
from src.models import CIELAB, CIEDE2000, CAM16UCS, get_model


class TestColorDifferencePhysics:
    """Test basic physical properties of color difference models"""

    def setup_method(self):
        """Setup test fixtures"""
        self.models = [
            CIELAB(),
            CIEDE2000(),
            CAM16UCS()
        ]

        # Standard test colors in XYZ (D65, 10-degree observer)
        self.xyz_white = np.array([95.047, 100.0, 108.883])
        self.xyz_gray = np.array([54.0, 56.8, 61.9])
        self.xyz_red = np.array([41.24, 21.26, 1.93])
        self.xyz_green = np.array([35.76, 71.52, 11.92])
        self.xyz_blue = np.array([18.05, 7.22, 95.05])

    def test_sanity_zero_difference(self):
        """Test that dE(ColorA, ColorA) = 0"""
        test_colors = [
            self.xyz_white,
            self.xyz_gray,
            self.xyz_red,
            self.xyz_green,
            self.xyz_blue
        ]

        for model in self.models:
            for color in test_colors:
                dE = model.predict(color, color, input_type='XYZ')
                assert abs(dE) < 1e-10, \
                    f"{model.name}: dE({color}, {color}) = {dE}, expected 0"

    def test_symmetry(self):
        """Test that dE(A, B) = dE(B, A)"""
        color_pairs = [
            (self.xyz_white, self.xyz_gray),
            (self.xyz_red, self.xyz_green),
            (self.xyz_green, self.xyz_blue),
            (self.xyz_red, self.xyz_blue),
        ]

        for model in self.models:
            for color_a, color_b in color_pairs:
                dE_ab = model.predict(color_a, color_b, input_type='XYZ')
                dE_ba = model.predict(color_b, color_a, input_type='XYZ')

                assert abs(dE_ab - dE_ba) < 1e-10, \
                    f"{model.name}: dE(A,B)={dE_ab} != dE(B,A)={dE_ba}"

    def test_positive_definite(self):
        """Test that dE(A, B) >= 0 for all A, B"""
        color_pairs = [
            (self.xyz_white, self.xyz_gray),
            (self.xyz_red, self.xyz_green),
            (self.xyz_green, self.xyz_blue),
        ]

        for model in self.models:
            for color_a, color_b in color_pairs:
                dE = model.predict(color_a, color_b, input_type='XYZ')
                assert dE >= 0, f"{model.name}: dE(A,B)={dE} < 0"

    def test_triangle_inequality(self):
        """Test that dE(A, C) <= dE(A, B) + dE(B, C)"""
        # This is not always strictly true for perceptual metrics,
        # but should hold approximately for not-too-different colors
        color_triplets = [
            (self.xyz_white, self.xyz_gray, self.xyz_red),
        ]

        for model in self.models:
            for color_a, color_b, color_c in color_triplets:
                dE_ac = model.predict(color_a, color_c, input_type='XYZ')
                dE_ab = model.predict(color_a, color_b, input_type='XYZ')
                dE_bc = model.predict(color_b, color_c, input_type='XYZ')

                # Allow some tolerance for perceptual spaces
                assert dE_ac <= (dE_ab + dE_bc) * 1.1, \
                    f"{model.name}: Triangle inequality violated: " \
                    f"dE(A,C)={dE_ac} > dE(A,B)+dE(B,C)={dE_ab + dE_bc}"


class TestCrossValidation:
    """Cross-validation tests against known reference values"""

    def test_ciede2000_standard_pairs(self):
        """
        Test CIEDE2000 against standard test pairs

        These are well-known test pairs from the CIEDE2000 specification.
        The expected values may need verification against MATLAB baseline.

        User: Please verify these values against your MATLAB baseline
        if strict validation is required. Otherwise, these values from
        the colour-science library can be trusted.
        """
        # Standard test pairs: (Lab_ref, Lab_sample, expected_dE2000)
        # Source: Sharma et al. 2005, "The CIEDE2000 Color-Difference Formula"
        test_pairs = [
            # Small differences
            (np.array([50.0, 2.6772, -79.7751]),
             np.array([50.0, 0.0, -82.7485]),
             2.0425),  # Approximate expected value

            (np.array([50.0, 3.1571, -77.2803]),
             np.array([50.0, 0.0, -82.7485]),
             2.8615),  # Approximate expected value

            (np.array([50.0, 2.8361, -74.0200]),
             np.array([50.0, 0.0, -82.7485]),
             3.4412),  # Approximate expected value
        ]

        model = CIEDE2000()

        print("\n" + "="*80)
        print("CIEDE2000 Test Values (colour-science library)")
        print("="*80)

        for i, (lab_ref, lab_sample, expected_dE) in enumerate(test_pairs):
            dE = model.predict(lab_ref, lab_sample, input_type='Lab')

            print(f"\nPair {i+1}:")
            print(f"  Lab_ref: {lab_ref}")
            print(f"  Lab_sample: {lab_sample}")
            print(f"  Computed dE2000: {dE:.4f}")
            print(f"  Expected dE2000: {expected_dE:.4f}")
            print(f"  Difference: {abs(dE - expected_dE):.4f}")

            # Allow 5% tolerance
            assert abs(dE - expected_dE) / expected_dE < 0.05, \
                f"dE2000 deviation too large: {dE} vs expected {expected_dE}"

        print("\n" + "="*80)
        print("All CIEDE2000 tests passed!")
        print("Using colour-science library values as baseline.")
        print("="*80 + "\n")

    def test_cielab_euclidean_distance(self):
        """Test CIELAB is true Euclidean distance in Lab space"""
        lab_ref = np.array([50.0, 10.0, -20.0])
        lab_sample = np.array([55.0, 15.0, -15.0])

        # Calculate expected Euclidean distance
        expected_dE = np.sqrt((55-50)**2 + (15-10)**2 + (-15-(-20))**2)

        model = CIELAB()
        dE = model.predict(lab_ref, lab_sample, input_type='Lab')

        assert abs(dE - expected_dE) < 1e-10, \
            f"CIELAB dE={dE} != Euclidean distance={expected_dE}"

    def test_model_factory(self):
        """Test model factory function"""
        cielab = get_model('CIELAB')
        assert isinstance(cielab, CIELAB)

        ciede2000 = get_model('CIEDE2000', kL=2.0)
        assert isinstance(ciede2000, CIEDE2000)
        assert ciede2000.kL == 2.0

        cam16ucs = get_model('CAM16UCS')
        assert isinstance(cam16ucs, CAM16UCS)

        # Test invalid model name
        with pytest.raises(ValueError):
            get_model('InvalidModel')


class TestLabXYZConversion:
    """Test XYZ to Lab conversions"""

    def test_xyz_to_lab_consistency(self):
        """Test that XYZ input gives same result as Lab input"""
        xyz_color1 = np.array([50.0, 50.0, 50.0])
        xyz_color2 = np.array([60.0, 60.0, 60.0])

        model = CIELAB()

        # Calculate using XYZ input
        dE_xyz = model.predict(xyz_color1, xyz_color2, input_type='XYZ')

        # Convert to Lab and calculate
        import colour
        illuminant = colour.CCS_ILLUMINANTS['CIE 1964 10 Degree Standard Observer']['D65']
        lab_color1 = colour.XYZ_to_Lab(xyz_color1, illuminant=illuminant)
        lab_color2 = colour.XYZ_to_Lab(xyz_color2, illuminant=illuminant)

        dE_lab = model.predict(lab_color1, lab_color2, input_type='Lab')

        assert abs(dE_xyz - dE_lab) < 1e-10, \
            f"XYZ and Lab inputs should give same result: {dE_xyz} != {dE_lab}"


if __name__ == '__main__':
    # Run tests with verbose output
    pytest.main([__file__, '-v', '-s'])
