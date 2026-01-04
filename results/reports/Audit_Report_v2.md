# Statistical Audit Report: Performance Evaluation of CIEDE2000 Across 32 Datasets

**Prepared for:** CIE Technical Committee Review
**Date:** January 2026
**Subject:** Validation of Meta-Color Data Infrastructure Against CIEDE2000 Benchmark

---

## 1. Introduction

### 1.1 Objective

The present study aims to validate the Meta-Color data infrastructure by evaluating the performance of the CIEDE2000 colour-difference formula across 32 experimental datasets spanning a wide range of colour-difference magnitudes and viewing conditions. The analysis focuses on assessing the consistency of CIEDE2000 predictions relative to visual assessments and identifying potential heterogeneity across datasets that may impact subsequent modelling efforts.

### 1.2 Methodology

To account for the inherent scaling differences between datasets—arising from variations in psychophysical methods (ratio judgement, pair comparison, threshold detection), colour-difference magnitudes (threshold ellipses vs. suprathreshold pairs), and measurement units—a rigorous normalization procedure was applied to each dataset individually.

#### 1.2.1 Scaling Factor Computation

For each dataset, a **Scaling Factor** ($F$) was computed to minimize the least-squares error between the computed colour difference ($\Delta E_{00}$, predicted by CIEDE2000) and the visual colour difference ($\Delta V$, obtained from psychophysical experiments). The scaling factor was determined using Equation (1):

$$F = \frac{\sum_{i=1}^{N} \Delta E_{00,i} \cdot \Delta V_i}{\sum_{i=1}^{N} \Delta E_{00,i}^2}$$

where $N$ represents the number of sample pairs in the dataset. This formulation ensures that the scaled predicted colour differences are brought onto the same scale as the visual assessments, thereby enabling direct comparison across datasets with fundamentally different experimental paradigms.

#### 1.2.2 Performance Metric

The analysis focuses on the **Scaled Ratio**, defined as:

$$R_i = \frac{\Delta E_{00,i}}{F \cdot \Delta V_i}$$

Under ideal conditions where CIEDE2000 perfectly predicts visual results, $R_i$ should equal 1.0 for all sample pairs. Deviations from unity indicate systematic bias or random scatter in the model's predictions. The distribution of scaled ratios provides insight into both the central tendency (via the mean ratio) and the consistency (via the standard deviation) of CIEDE2000 performance.

The performance of CIEDE2000 was quantified using the Standardized Residual Sum of Squares (STRESS) measure, following CIE 217:2016 recommendations. The STRESS value expresses the percentage error between the model predictions and visual results after scaling correction.

---

## 2. Performance Consistency Across Colour-Difference Magnitudes

### 2.1 Global Performance Statistics

The analysis encompassed **18,137 colour-difference pairs** across 32 datasets. The global statistics for the Scaled Ratio distribution are summarized below:

- **Global Mean Ratio:** 0.9828
- **Global Standard Deviation:** 0.6664
- **±1σ Range:** [0.3164, 1.6491]
- **Global Outlier Rate:** 1.67% (303 pairs exceeding ±1σ bounds)

The global mean ratio of 0.9828 indicates that, on average, CIEDE2000 predictions are within 2% of the visual assessments after scaling normalization. This result is by construction close to unity due to the least-squares optimization inherent in the scaling factor calculation. The standard deviation of 0.6664 quantifies the scatter around the mean and reflects the combined effects of inter-observer variability, intra-observer repeatability, and model limitations.

### 2.2 Visual Analysis: Magnitude Dependency

Figure 1 presents the Scaled Ratio plotted against the computed colour difference ($\Delta E_{00}$), commonly referred to as the "Ronnier Plot" in the colour science literature.

**[Figure 1: Scaled Ratio vs. Computed Colour Difference]**
*The red solid line indicates the global mean ratio (0.9828). Blue dashed lines represent ±1 standard deviation bands (0.3164 to 1.6491). Green dotted lines indicate ±2 standard deviation bounds.*

#### 2.2.1 Interpretation

The scatter plot reveals **no significant dependency** of the Scaled Ratio on colour-difference magnitude. The cloud of data points is distributed relatively evenly across the range of computed colour differences, with no systematic tilt or curvature evident in the pattern. Specifically:

1. **Absence of Systematic Bias:** The mean line remains approximately horizontal across the magnitude range, indicating that CIEDE2000 does not systematically over-predict for small colour differences while under-predicting for large ones (or vice versa).

2. **Homoscedasticity:** The vertical spread of points appears roughly constant across the magnitude range, suggesting that the prediction error does not systematically increase or decrease with colour-difference magnitude.

3. **Standard Deviation Bands:** The ±1σ bands (blue dashed lines) encompass the majority of data points across all magnitudes. The relatively wide bands (spanning approximately 1.33 units) reflect the substantial inter-observer and intra-observer variability inherent in colour-difference assessment, consistent with findings reported by Wang et al. (2012) and Luo et al. (2023).

#### 2.2.2 Implications for CIEDE2000 Validity

The flat distribution of the Scaled Ratio across magnitudes suggests that **CIEDE2000 maintains consistent performance** across the range of colour differences represented in the 32 datasets. This finding supports the extended validity of CIEDE2000 beyond its original design scope (small colour differences, $\Delta E_{ab}^* < 5$) and aligns with the conclusions of Wang et al. (2012), who found that CIEDE2000 "worked effectively for the full range of colour differences."

However, it is important to note that the standard deviation of 0.6664 is substantial relative to the mean, indicating considerable variability in individual predictions. This scatter underscores the need for robust statistical methods when evaluating colour-difference formulae and suggests potential for improvement through weighted modeling or dataset-specific parametric adjustments.

---

## 3. Dataset Heterogeneity: The "Naughty List"

### 3.1 Outlier Analysis

To identify datasets exhibiting anomalous behavior, the percentage of sample pairs falling outside the ±1σ range was computed for each of the 32 datasets. Figure 2 presents the outlier ranking, sorted in descending order of outlier rate.

**[Figure 2: Outlier Rate by Dataset]**
*Datasets are ranked by the percentage of sample pairs with Scaled Ratios outside the ±1σ range.*

### 3.2 High-Noise Datasets

The top three datasets with the highest outlier rates are:

1. **WCG (Wide Colour Gamut):** 25.0% outlier rate
2. **Parametric-NS (No Separation):** 10.2% outlier rate
3. **BIGC-T2-SG (Semi-Gloss):** 5.1% outlier rate

These datasets exhibit substantially higher noise levels compared to the global average of 1.67%.

#### 3.2.1 Hypothesized Sources of Heterogeneity

The elevated outlier rates in these datasets may arise from several factors:

**WCG Dataset:**
The Wide Colour Gamut dataset represents colours at the extreme boundaries of achievable chromaticity, often involving highly saturated stimuli. Previous research (Luo et al., 2023) has demonstrated that CIEDE2000, which was developed primarily using datasets with moderate chroma levels, exhibits reduced accuracy for highly saturated colours. Additionally, observer uncertainty increases for colours near the spectral locus, contributing to higher inter-observer variability.

**Parametric-NS Dataset:**
The "No Separation" paradigm, in which colour samples are presented in direct contact without a neutral gap, is known to induce simultaneous contrast and assimilation effects that are not accounted for in CIEDE2000. Mirjalili et al. (2019) demonstrated that colour-difference formulae developed for separated samples systematically under-perform when applied to no-separation configurations, necessitating the development of specialized formulae such as $\Delta E_{NS}$.

**BIGC-T2-SG Dataset:**
The semi-gloss surface finish introduces additional complexity through specular reflections and variable viewing geometry. Gloss has been identified as a parametric effect that influences colour-difference perception (CIE 101:1993), yet CIEDE2000 does not incorporate gloss-dependent terms. The elevated outlier rate likely reflects this model limitation.

### 3.3 Implications for Future Modeling

The identification of high-noise datasets has important implications for subsequent modeling efforts:

1. **Weighted Regression:** Datasets with high outlier rates should be down-weighted or analyzed separately to prevent them from disproportionately influencing model optimization.

2. **Parametric Extensions:** The observed heterogeneity suggests the need for parametric factors to account for viewing conditions (separation vs. no-separation), surface properties (gloss level), and chromaticity extremes (wide colour gamut).

3. **Dataset-Specific Validation:** Models should be validated separately on high-noise datasets to ensure that improvements in global performance do not come at the expense of degraded performance on edge cases.

---

## 4. Conclusion

### 4.1 Summary

The present audit successfully harmonized 32 colour-difference datasets using dataset-specific scaling factors, enabling a comprehensive evaluation of CIEDE2000 performance across a wide range of experimental conditions. The analysis yielded the following key findings:

1. **Scaling Factor Robustness:** The scaling factor approach effectively normalized datasets with disparate psychophysical methods and measurement units, as evidenced by the global mean ratio of 0.9828.

2. **Magnitude Independence:** The Scaled Ratio exhibited no systematic dependency on colour-difference magnitude, supporting the extended validity of CIEDE2000 across the range from threshold to large colour differences.

3. **Moderate Global Scatter:** The global standard deviation of 0.6664 reflects a combination of inherent observer variability and model limitations, consistent with STRESS values reported in the literature.

4. **Dataset Heterogeneity:** Three datasets (WCG, Parametric-NS, BIGC-T2-SG) exhibited anomalously high outlier rates (5–25%), likely attributable to extreme chromaticity, simultaneous contrast effects, and gloss-related factors.

### 4.2 Verdict on Data Integrity

The baseline performance confirms the **integrity of the Meta-Color data infrastructure**. The global statistics align with expected values for a well-calibrated dataset collection, and the majority of datasets (29 of 32) exhibit low outlier rates consistent with normal observer variability.

The observed outliers in specific datasets do not indicate data corruption or processing errors; rather, they reflect genuine limitations in the CIEDE2000 formula when applied to edge cases beyond its original design scope. This finding underscores the **necessity for weighted modeling** in subsequent analysis phases (Module 2), wherein dataset-specific weights can be assigned based on the observed noise characteristics.

### 4.3 Recommendations for Module 2

1. **Implement Dataset Weighting:** Apply inverse-variance weighting to down-weight datasets with high outlier rates during model optimization.

2. **Investigate Parametric Effects:** Conduct separate analyses for subgroups (separated vs. no-separation, matte vs. glossy, moderate vs. wide gamut) to quantify parametric effects systematically.

3. **Benchmark Alternative Formulae:** Extend the audit to evaluate CAM16-UCS and other uniform colour spaces to identify models with superior performance on the high-noise datasets.

4. **Observer Variability Analysis:** For datasets with repeat observations, compute inter- and intra-observer STRESS values to partition total variance into observer-related and model-related components.

---

## References

- CIE 101:1993. *Parametric Effects in Colour-Difference Evaluation*. Vienna: CIE Central Bureau.
- CIE 217:2016. *Recommended Method for Evaluating the Performance of Colour-Difference Formulae*. Vienna: CIE Central Bureau.
- Luo, M. R., Cui, G., & Rigg, B. (2001). The development of the CIE 2000 colour-difference formula: CIEDE2000. *Color Research & Application*, 26(5), 340–350.
- Luo, M. R., Xu, Q., Pointer, M., Melgosa, M., Cui, G., Li, C., Xiao, K., & Huang, M. (2023). A comprehensive test of colour-difference formulae and uniform colour spaces using available visual datasets. *Color Research & Application*, 48(3), 267–282.
- Mirjalili, F., Luo, M. R., Cui, G., & Morovic, J. (2019). Color-difference formula for evaluating color pairs with no separation: ΔE_NS. *Journal of the Optical Society of America A*, 36(5), 789–799.
- Wang, H., Cui, G., Luo, M. R., & Xu, H. (2012). Evaluation of colour-difference formulae for different colour-difference magnitudes. *Color Research & Application*, 37(5), 316–325.

---

**Appendix A: Dataset Summary Statistics**
*[Available upon request: Per-dataset scaling factors, STRESS values, and outlier counts]*

**Appendix B: Computational Details**
*Analysis performed using Python 3.x with NumPy/Pandas libraries. CIEDE2000 implementation verified against CIE test vectors.*
