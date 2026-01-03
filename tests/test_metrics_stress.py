import numpy as np
import pytest

from src.metrics import calculate_stress


def _stress_matlab_formula(predicted: np.ndarray, observed: np.ndarray) -> float:
    dot = float(np.sum(predicted * observed))
    denom = float(np.sum(predicted ** 2) * np.sum(observed ** 2))
    return 100.0 * float(np.sqrt(max(0.0, 1.0 - (dot * dot) / denom)))


def test_stress_matches_matlab_formula_random():
    rng = np.random.default_rng(0)
    predicted = rng.random(50)
    observed = rng.random(50)

    expected = _stress_matlab_formula(predicted, observed)
    actual = calculate_stress(predicted, observed, use_scaling=True)

    assert actual == pytest.approx(expected, rel=0.0, abs=1e-12)


def test_stress_zero_for_perfect_proportional_fit():
    rng = np.random.default_rng(1)
    predicted = rng.random(100)
    observed = 2.5 * predicted

    assert calculate_stress(predicted, observed, use_scaling=True) == pytest.approx(0.0, abs=1e-12)


def test_stress_raises_on_zero_energy():
    predicted = np.zeros(10)
    observed = np.ones(10)
    with pytest.raises(ValueError):
        calculate_stress(predicted, observed, use_scaling=True)

    predicted = np.ones(10)
    observed = np.zeros(10)
    with pytest.raises(ValueError):
        calculate_stress(predicted, observed, use_scaling=True)


def test_stress_unscaled_variant_matches_residual_definition():
    predicted = np.array([1.0, 2.0, 3.0])
    observed = np.array([1.0, 1.0, 1.0])

    expected = 100.0 * float(np.sqrt(np.sum((observed - predicted) ** 2) / np.sum(observed ** 2)))
    actual = calculate_stress(predicted, observed, use_scaling=False)

    assert actual == pytest.approx(expected, rel=0.0, abs=1e-12)

