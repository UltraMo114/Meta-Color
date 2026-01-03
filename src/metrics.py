"""
Metrics for evaluating color difference formulas

This module implements performance metrics from outline.md:
- STRESS (Standardized Residual Sum of Squares)
- dE/dV Ratio (Mean ratio between calculated and visual differences)
"""

import numpy as np
from typing import List, Tuple, Optional


def calculate_stress(predicted: np.ndarray,
                     observed: np.ndarray,
                     use_scaling: bool = True) -> float:
    """
    Calculate STRESS (Standardized Residual Sum of Squares)

    MATLAB reference (ref/STRESS.m):

        STRESS = 100 * sqrt(1 - (Σ(ΔE·ΔV))^2 / (Σ(ΔE^2) · Σ(ΔV^2)))

    Equivalent residual form (with optimal scaling factor f):

        STRESS = 100 * sqrt( Σ(ΔV - f·ΔE)^2 / Σ(ΔV^2) )

    where f is a scaling factor that minimizes the residual.

    Parameters
    ----------
    predicted : np.ndarray
        Predicted color differences (ΔE from formula)
    observed : np.ndarray
        Observed visual differences (ΔV)
    use_scaling : bool
        If True, apply optimal scaling factor f (default: True)

    Returns
    -------
    float
        STRESS value (lower is better, 0 = perfect fit)

    References
    ----------
    García et al. (2007) "Measurement of the relationship between
    perceived and computed color difference"
    """
    if len(predicted) != len(observed):
        raise ValueError("predicted and observed arrays must have same length")

    predicted = np.asarray(predicted, dtype=float).ravel()
    observed = np.asarray(observed, dtype=float).ravel()

    if predicted.size == 0:
        raise ValueError("predicted and observed must be non-empty")

    if use_scaling:
        # Use the closed-form STRESS.m expression (numerically stable and symmetric).
        dot = float(np.sum(predicted * observed))
        pred_energy = float(np.sum(predicted ** 2))
        obs_energy = float(np.sum(observed ** 2))
        denom = pred_energy * obs_energy

        if denom <= 0.0:
            raise ValueError("STRESS is undefined when Σ(predicted^2) or Σ(observed^2) is zero")

        ratio = (dot * dot) / denom
        # Guard against tiny negative due to floating error (e.g., ratio slightly > 1).
        inside = max(0.0, 1.0 - ratio)
        return 100.0 * float(np.sqrt(inside))

    # Unscaled variant (not MATLAB STRESS.m): f fixed to 1
    denominator = float(np.sum(observed ** 2))
    if denominator <= 0.0:
        raise ValueError("STRESS is undefined when Σ(observed^2) is zero")

    numerator = float(np.sum((observed - predicted) ** 2))
    return 100.0 * float(np.sqrt(numerator / denominator))


def calculate_pf_pt(predicted: np.ndarray,
                    observed: np.ndarray) -> Tuple[float, float]:
    """
    Calculate PF/PT standardized residual metrics

    PF = Percent of variance accounted for
    PT = Percent of total variance

    Parameters
    ----------
    predicted : np.ndarray
        Predicted color differences
    observed : np.ndarray
        Observed visual differences

    Returns
    -------
    Tuple[float, float]
        (PF, PT) values
    """
    # Optimal scaling factor
    f = np.sum(predicted * observed) / np.sum(predicted ** 2)

    # Residuals
    residuals = observed - f * predicted

    # PF: Percent of variance accounted for
    ss_residual = np.sum(residuals ** 2)
    ss_total = np.sum((observed - np.mean(observed)) ** 2)
    pf = 100.0 * (1.0 - ss_residual / ss_total)

    # PT: Total percent
    pt = 100.0 * np.sqrt(ss_residual / ss_total)

    return pf, pt


def calculate_de_dv_ratio(predicted: np.ndarray,
                          observed: np.ndarray,
                          return_std: bool = False) -> Tuple[float, Optional[float]]:
    """
    Calculate mean dE/dV ratio

    This metric measures how well the color difference formula
    predicts visual differences on average.

    Parameters
    ----------
    predicted : np.ndarray
        Predicted color differences (ΔE)
    observed : np.ndarray
        Observed visual differences (ΔV)
    return_std : bool
        If True, also return standard deviation (default: False)

    Returns
    -------
    Tuple[float, Optional[float]]
        (mean_ratio, std_ratio) if return_std=True, else (mean_ratio, None)

    Notes
    -----
    A ratio of 1.0 indicates perfect prediction on average.
    Ratio > 1.0: formula over-predicts visual differences
    Ratio < 1.0: formula under-predicts visual differences
    """
    # Avoid division by zero
    valid_mask = observed > 1e-10
    ratios = predicted[valid_mask] / observed[valid_mask]

    mean_ratio = np.mean(ratios)

    if return_std:
        std_ratio = np.std(ratios)
        return mean_ratio, std_ratio
    else:
        return mean_ratio, None


def calculate_rmse(predicted: np.ndarray,
                   observed: np.ndarray,
                   use_scaling: bool = True) -> float:
    """
    Calculate Root Mean Square Error

    Parameters
    ----------
    predicted : np.ndarray
        Predicted color differences
    observed : np.ndarray
        Observed visual differences
    use_scaling : bool
        If True, apply optimal scaling factor (default: True)

    Returns
    -------
    float
        RMSE value
    """
    if use_scaling:
        f = np.sum(predicted * observed) / np.sum(predicted ** 2)
    else:
        f = 1.0

    rmse = np.sqrt(np.mean((observed - f * predicted) ** 2))

    return rmse


def calculate_pearson_r(predicted: np.ndarray,
                        observed: np.ndarray) -> float:
    """
    Calculate Pearson correlation coefficient

    Parameters
    ----------
    predicted : np.ndarray
        Predicted color differences
    observed : np.ndarray
        Observed visual differences

    Returns
    -------
    float
        Pearson r value (-1 to 1, higher is better)
    """
    r = np.corrcoef(predicted, observed)[0, 1]
    return r


def evaluate_model_performance(predicted: np.ndarray,
                               observed: np.ndarray) -> dict:
    """
    Calculate all performance metrics for a color difference model

    Parameters
    ----------
    predicted : np.ndarray
        Predicted color differences from formula
    observed : np.ndarray
        Observed visual differences

    Returns
    -------
    dict
        Dictionary containing all metrics:
        - 'stress': STRESS value
        - 'rmse': Root Mean Square Error
        - 'pearson_r': Pearson correlation
        - 'mean_ratio': Mean dE/dV ratio
        - 'std_ratio': Standard deviation of dE/dV ratio
        - 'pf': Percent variance accounted for
        - 'pt': Percent total variance
    """
    stress = calculate_stress(predicted, observed)
    rmse = calculate_rmse(predicted, observed)
    pearson_r = calculate_pearson_r(predicted, observed)
    mean_ratio, std_ratio = calculate_de_dv_ratio(predicted, observed, return_std=True)
    pf, pt = calculate_pf_pt(predicted, observed)

    return {
        'stress': stress,
        'rmse': rmse,
        'pearson_r': pearson_r,
        'mean_ratio': mean_ratio,
        'std_ratio': std_ratio,
        'pf': pf,
        'pt': pt
    }


class PerformanceEvaluator:
    """Helper class for evaluating model performance across multiple datasets"""

    def __init__(self):
        self.results = {}

    def add_result(self,
                   dataset_name: str,
                   predicted: np.ndarray,
                   observed: np.ndarray):
        """
        Add evaluation results for a dataset

        Parameters
        ----------
        dataset_name : str
            Name of the dataset
        predicted : np.ndarray
            Predicted color differences
        observed : np.ndarray
            Observed visual differences
        """
        metrics = evaluate_model_performance(predicted, observed)
        self.results[dataset_name] = metrics

    def get_summary(self) -> dict:
        """
        Get summary statistics across all datasets

        Returns
        -------
        dict
            Dictionary with mean and std for each metric
        """
        if not self.results:
            return {}

        # Collect all metrics
        all_metrics = {
            key: [self.results[dataset][key] for dataset in self.results]
            for key in self.results[list(self.results.keys())[0]].keys()
        }

        # Calculate summary statistics
        summary = {}
        for metric_name, values in all_metrics.items():
            summary[metric_name] = {
                'mean': np.mean(values),
                'std': np.std(values),
                'min': np.min(values),
                'max': np.max(values)
            }

        return summary

    def print_summary(self):
        """Print formatted summary of results"""
        print("\n" + "="*80)
        print("Performance Summary Across All Datasets")
        print("="*80)

        summary = self.get_summary()

        for metric_name, stats in summary.items():
            print(f"\n{metric_name.upper()}:")
            print(f"  Mean: {stats['mean']:.4f}")
            print(f"  Std:  {stats['std']:.4f}")
            print(f"  Min:  {stats['min']:.4f}")
            print(f"  Max:  {stats['max']:.4f}")

        print("="*80 + "\n")
