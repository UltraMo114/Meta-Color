Journal of the Optical Society of America A

OPTICS, IMAGE SCIENCE, AND VISION

# Color-difference formula for evaluating color pairs with no separation:  $ \Delta E_{NS} $ 

FERESHTEH MIRJALILI, $ ^{1} $  MING RONNIER LUO, $ ^{1,2,*} $  GUIHUA CUI, $ ^{3} $  AND JAN MOROVIC $ ^{4} $ 

 $ ^{1} $ State Key Laboratory of Modern Optical Instrumentation, Zhejiang University, Hangzhou 310027, China

 $ ^{2} $ School of Design, University of Leeds, Leeds LS2 9JT, UK

 $ ^{3} $ School of Physics & Electronics Information Engineering, Wenzhou University, Wenzhou 325035, China

 $ ^{4} $ HP Inc., Barcelona, Catalonia, Spain

 $ ^{*} $ Corresponding author: m.r.luo@zju.edu.cn

Received 7 September 2018; revised 5 February 2019; accepted 19 March 2019; posted 19 March 2019 (Doc. ID 345361); published 16 April 2019

All color-difference formulas are developed to evaluate color differences for pairs of stimuli with hairline separation. In printing applications, however, color differences are frequently judged between a pair of samples with no separation (NS) because they are printed adjacently on the same piece of paper. A new formula,  $ \Delta E_{NS} $ , has been developed for pairs of stimuli with NS. An experiment was conducted to investigate the effect of different color-difference magnitudes using sample pairs with NS. 1012 printed pairs with NS were prepared around 11 CIE recommended color centers. The pairs, representing four color-difference magnitudes of 1, 2, 4, and 8 CIELAB units were visually evaluated by a panel of 19 observers using the gray-scale method. Comparison of the present data based on pairs with NS, and previously generated data using pairs with hairline separation, showed a clear separation effect. A new color-difference equation for the NS viewing condition ( $ \Delta E_{NS} $ ) is proposed by modifying the CIEDE2000 formula. The separation effect can be well described by the new formula. For a sample pair with NS, when the CIEDE2000 color difference is less than 9.1, a larger color difference leads to a larger lightness difference, but has no effect on the chromatic difference. When the CIEDE2000 color difference is greater than 9.1, the effect is the opposite. The new formula is recommended for future research to evaluate its performance in appropriate applications. © 2019 Optical Society of America

https://doi.org/10.1364/JOSAA.36.000789

### 1. INTRODUCTION

Since the recommendation of CIELAB color space and the associated color-difference formula by the Commission Internationale de l'Eclairage (CIE) in 1976 $ ^{[1]} $ , much effort has been devoted to try to improve its uniformity. Despite its simplicity, there is relatively poor correlation between color differences predicted by CIELAB and their equivalent visual judgments, especially for small to medium color differences, i.e.,  $ \Delta E_{ab}^{*} < 5 $   $ {}^{[2]} $ .

In 1987, CIE recommended collecting color-difference data surrounding five color centers including gray, red, green, blue, and yellow for coordinated research on color-difference evaluation [3]. Later, the number of color centers was extended to 19, of which the additional 12 centers provide extended coverage of the color gamut [4]. Following the CIE guidelines [3,4], several sets of visual data were collected using surface samples viewed under typical industrial viewing conditions, in order to develop new color-difference formulas and investigate the effect of various parametric factors such as the color of the background, the illumination, the magnitude of color difference, the stimulus size, the separation between the two samples, etc. A brief account of some important color-difference formulas and visual data sets is given below.

The Colour Measurement Committee [CMC(l:c)] color-difference formula was one of the earliest formulas after CIELAB. It was developed by the CMC of the Society of the Dyers and Colourists (SDC) based on experimental results obtained using textile samples [5]. In this formula, “l” refers to the lightness and “c” refers to the chroma weighting factor. Although CMC(l:c) performed better than CIELAB for small color differences, it did not perform well compared with those developed in the later stage [6].

In an attempt to overcome the problems associated with CMC(l:c), the BFD(l:c) color-difference formula was derived by Luo and Rigg at the University of Bradford, based on over 500 pairs of wool samples and using the gray-scale method to combine the many previously published data sets  $ [7,8] $ . The gray-scale method is a standard assessment method in the textile industry for assessing color fastness  $ [9] $ . In this method, the color difference between a pair of stimuli is compared visually.

with the lightness differences of a series of gray samples. A detailed description of the gray-scale method is given in Section 2.B. This method has also been widely used in the color-difference research field (see below).

The CIE recommended the CIE94 color-difference formula  $ [10] $  for field trials proposed by Berns et al.  $ [11] $  using visual assessments of 156 glossy paint sample pairs around 19 color centers, collected using the method of constant stimuli. This data set is known as the RIT–DuPont data set. Later, Kim and Nobbs  $ [12] $  investigated the weighting functions in the CIELAB color-difference formula using glossy paint samples. The corresponding data set, named the Leeds data set, consists of 243 and 104 pairs accumulated using the gray-scale and pair-comparison methods, respectively. The outcome was the Leeds color-difference (LCD) equation. Using a series of 418 paint samples around the five CIE color centers, Witt  $ [13] $  accumulated a new data set and studied the effect of magnitude and direction of color difference on color-difference evaluation using the gray-scale method. In 2001, using a combination of the BFD, RIT–DuPont, Leeds, and Witt data sets, the CIEDE2000 color-difference formula was proposed by Luo et al.  $ [6] $  and later recommended by CIE as the standard color-difference equation  $ [14] $ . This equation showed a considerable improvement over previously proposed color-difference formulas.

Although the above formulas can accurately predict perceptual color differences, they do not have an associated color space, because they are all modifications of CIELAB. Moreover, they do not consider a change in the viewing parameters such as the luminance of the adaptation field, the magnitude of the color difference, the separation effect, etc. In an attempt to develop a new, perceptually uniform color space, Luo et al. $ ^{[15]} $  revised their color appearance model, CIECAM97s to improve its accuracy and make it simpler. They proposed a new color appearance model, which was adopted by the CIE as the CIECAM02 color appearance model  $ [16] $ . Luo et al. later derived three uniform color spaces based on CIECAM02 to predict small color differences, to predict large color differences, and a combination of both, named CAM02-SCD, CAM02-LCD, and CAM02-UCS, respectively. CIECAM02 and CAM02-UCS have been widely used in many applications. However, some mathematical problems in the chromatic adaptation transform in CIECAM02 were found. Li et al.  $ [17] $  have recently revised the CIECAM02 model to solve these problems and have proposed a new color appearance model, CAM16, and its corresponding uniform color space, CAM16-UCS. It is hoped that this model will receive CIE recommendation at some time in the near future  $ [18] $ .

Morillas and Fairchild [19] recently proposed two color-difference metrics based on color-discrimination ellipsoids derived from the RIT–DuPont data set. They found that the performance of both metrics is significantly dependent on the magnitude of the color difference. After optimizing the equations with a power factor and a scaling factor with respect to the magnitude of the color difference, both formulas outperformed CIEDE2000. However, the new metrics are complex and computationally expensive, with 21 parameters to be computed.

Another stream of color-difference research has been to study the influence of various parametric factors, such as the separation and the color-difference magnitude, on the perceived color difference. CIE has recommended a set of "reference" viewing conditions for assessing color differences, i.e., a pair of hairline divided samples under a D65 simulator at 1000 lux, viewed by observers with normal color vision, object viewing mode, stimulus size of more than  $ 4^{\circ} $  subtended visual angle, color-difference magnitude of 0–5 CIELAB units, and visually homogeneous sample structure [4]. Since the two physical samples need to be juxtaposed, there would inevitably be a fine dividing line, known as a hairline, between the two samples. The psychophysical method for data acquisition was not specified by the CIE. However, most of the available data sets have been generated using the gray-scale or constant-stimuli methods.

The effect of separation on perceived color difference is an important aspect of color-difference evaluation. When evaluating color differences, three types of separation can be considered: hairline, gap, and "no-separation" (NS). A hairline is the virtual line that appears between a pair of samples when they are placed side by side. On the other hand, a gap is a larger spatial distance between a pair of samples such that the background can be clearly seen between the two samples. For samples with NS, the two samples are juxtaposed in a way that observers see the change of color from one sample to the other without any interference of a hairline or a gap. In order to achieve the pairs with NS in this work, the two samples were printed side by side on the same substrate as one physical specimen.

The conventional color-difference formulas are all developed based on pairs with hairline separation. However, in printing applications it is usually the case that colors are printed adjacent to one another, with no discernible gap on the same medium, e.g., paper (documents), card (packaging), or vinyl (display advertising). In this specific application, some problems with respect to the ineffectiveness of color-difference formulas have been reported, and it is this condition that is investigated in this paper.

In one of the earliest studies on the effect of separation on color-difference perception of painted specimens, Witt  $ [20] $  used a large gap of 3 mm width between the two samples, constituting an angular subtense of  $ 0.5^{\circ} $ . The results revealed that a correcting gap factor should be considered in the color-difference formulas. Witt also demonstrated that the gap factor decreases with increasing lightness of the samples.

Guan and Luo  $ [21,22] $  carried out an extensive study on two parametric effects: gap and magnitude of color difference. They compared the effect of a hairline and a large (7.6 cm) gap on the color-difference judgments of 75 wool sample pairs. The mean color difference of the whole data set was 3 CIELAB units. It was found that, although the visual differences of sample pairs with large separation were approximately 11% smaller than those for pairs having hairline separation, the separation effect was not as obvious as that found by Witt  $ [20] $ . They also investigated the parametric effect of sample separation using large color differences (a mean of 13 CIELAB units). Again, the sample pairs with a large gap showed smaller color differences than the pairs with hairline separation. The results of comparison of the chromatic discrimination ellipses between small and large color differences implied that there might be a large difference between small and large color-difference perception.

In a similar study, Xin et al. [23] used dyed cotton sample pairs around five CIE color centers. The average color difference of the sample pairs was approximately 5 CIELAB units. They also demonstrated that the perceived color difference of pairs with a hairline separation was 8% larger than those of the pairs with a 7.6 cm separation.

Xu and Yaguchi [24] studied the effect of color-difference magnitude on interobserver variability. Using a new visual data set ranging from small to large color differences around the five CIE color centers on a CRT display, they showed that interobserver variability for small color differences was approximately 40% inferior to that of large ones, implying less precision in color discrimination judgment for small differences.

Using self-luminous sample pairs with NS, 1-pixel, 2-pixel, and large gaps on a CRT display, Cui et al.  $ [25,26] $  found that changing the separation size between the two samples of a pair had only a small effect on the perceived color difference, but it did change the weighting factor between the lightness difference and the chromatic difference. However, they did find a distinct difference between pairs with and without separation (to be discussed later).

The “gap effect” has been also extensively studied by color-vision scientists. Pioneering research on the effect of a gap on color discrimination was conducted by Boynton et al.  $ [27] $ . They defined the gap effect as a phenomenon of altered discriminability due to a separation between the fields. They referred to it as a “positive” or a “negative” effect depending on whether the discriminability was improved or impaired, respectively. Their results showed that by introducing the gap between two color fields in a pair, the chromatic discriminability improved, while the luminance discriminability was impaired. It was found by later research that chromatic discriminability improved when only the signal of the short-wavelength (S) cones was varying. For discrimination where only the ratio of the signals of the long-wavelength (L) and middle-wavelength (M) cones was varying, a small gap effect was observed  $ [27,28] $ . Eskew  $ [29] $  found that the gap effect was reduced by increasing the exposure time. This may indicate that the effect of the gap on chromatic discrimination might not be as significant as its effect on lightness discrimination. Note that in most of these studies, it was difficult to achieve a NS arrangement because some kind of a dividing line could still be observed between the two stimuli.

With the above in mind, two goals were set for this research: to investigate the difference between pairs of samples with NS and pairs of samples with hairline separation, and to study the effect of color-difference magnitude on color-difference evaluation.

### 2. EXPERIMENTAL METHODS

### A. Sample Preparation

Eleven CIE color centers, distributed uniformly in CIELAB color space, were chosen for this study. These color centers were gray, red, high-chroma orange, yellow, high-chroma yellow-green, green, high-chroma green, blue-green, blue, high-chroma purple, and black. Table 1 gives the CIELAB values of the chosen color centers.

<div style="text-align: center;">Table 1. CIELAB Color Attributes  $ L^{*} $ ,  $ a^{*} $ ,  $ b^{*} $  of the 11 Color Centers Calculated Using the CIE Illuminant D65/1964 Colorimetric Observer Combination</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Color Center</td><td style='text-align: center;'>$ L^{*} $</td><td style='text-align: center;'>$ a^{*} $</td><td style='text-align: center;'>$ b^{*} $</td><td style='text-align: center;'>$ C_{ab}^{*} $</td><td style='text-align: center;'>$ b_{ab} $</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>Gray</td><td style='text-align: center;'>61.1</td><td style='text-align: center;'>-3.2</td><td style='text-align: center;'>3.2</td><td style='text-align: center;'>4.5</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>Red</td><td style='text-align: center;'>41.0</td><td style='text-align: center;'>33.2</td><td style='text-align: center;'>25.5</td><td style='text-align: center;'>41.9</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>High-chroma orange</td><td style='text-align: center;'>60.3</td><td style='text-align: center;'>33.0</td><td style='text-align: center;'>64.3</td><td style='text-align: center;'>72.2</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>Yellow</td><td style='text-align: center;'>84.1</td><td style='text-align: center;'>-6.7</td><td style='text-align: center;'>50.4</td><td style='text-align: center;'>50.9</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>High-chroma yellow green</td><td style='text-align: center;'>63.2</td><td style='text-align: center;'>-29.3</td><td style='text-align: center;'>44.1</td><td style='text-align: center;'>53.0</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>Green</td><td style='text-align: center;'>56.2</td><td style='text-align: center;'>-32.5</td><td style='text-align: center;'>4.9</td><td style='text-align: center;'>32.8</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>High-chroma green</td><td style='text-align: center;'>56.0</td><td style='text-align: center;'>-45.7</td><td style='text-align: center;'>5.7</td><td style='text-align: center;'>46.1</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>Blue-green</td><td style='text-align: center;'>50.6</td><td style='text-align: center;'>-18.7</td><td style='text-align: center;'>-6.9</td><td style='text-align: center;'>19.9</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>Blue</td><td style='text-align: center;'>37.0</td><td style='text-align: center;'>-1.3</td><td style='text-align: center;'>-27.9</td><td style='text-align: center;'>28.0</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>High-chroma purple</td><td style='text-align: center;'>45.4</td><td style='text-align: center;'>18.9</td><td style='text-align: center;'>-25.0</td><td style='text-align: center;'>31.4</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>Black</td><td style='text-align: center;'>29.8</td><td style='text-align: center;'>-3.1</td><td style='text-align: center;'>2.3</td><td style='text-align: center;'>3.8</td></tr></table>

For each color center, a systematic distribution of samples around the center in CIELAB color space was designed and produced. A group of seven, seven, and nine pairs were prepared in  $ L^{*}a^{*} $ ,  $ L^{*}b^{*} $ , and  $ a^{*}b^{*} $  planes for each color center, respectively. In each plane, the two color attributes varied while the third one was approximately constant, i.e.,  $ \Delta b^{*} $ ,  $ \Delta a^{*} $  or  $ \Delta L^{*} $  in  $ L^{*}a^{*} $ ,  $ L^{*}b^{*} $  or  $ a^{*}b^{*} $  planes, respectively, was always approximately zero. Note that  $ \Delta $  designates the difference between the sample and the color center. Additionally, the pairs had four levels of color-difference magnitudes, namely, 1, 2, 4, and 8 CIELAB units. These levels are denoted as  $ \Delta E_{M} = 1 $ , 2, 4, and 8 respectively. In total, 1012 pairs of samples were prepared for each color center.

It can be seen from Table 1 that the color centers cover a wide range of  $ L^{*} $  [30,84],  $ a^{*} $  [-46,33], and  $ b^{*} $  [-27,64]. Figures 1(a)–1(c) illustrate the distribution of the color centers in CIELAB  $ a^{*}b^{*} $ ,  $ L^{*}a^{*} $ , and  $ L^{*}b^{*} $  planes, respectively. Figure 1(d) shows the sample distribution around the gray center for  $ \Delta E_{M} $  of 8 CIELAB units.  $ \Delta L^{*} $ ,  $ \Delta a^{*} $  and  $ \Delta b^{*} $  are the differences between the color center and the sample.

The sample pairs were printed on an HP Latex 365 Printer (HP, Barcelona, Spain) on an Avery Dennison matte white polymeric self-adhesive vinyl substrate with CMYKcm inks. For each pair, the color center and its corresponding sample were printed adjacent to each other on the same substrate such that there was NS between them. Each pair had a size of  $ 8 \, cm \times 8 \, cm $ , i.e., each sample in the pair had a size of  $ 4 \, cm \times 8 \, cm $ , and an approximate vertical field of view of  $ 4^\circ $ . The spectral reflectance of the samples was measured using an X-Rite SpectroEye spectrophotometer (X-Rite, Grand Rapids, U.S.). This portable instrument has  $ 45^\circ:0^\circ $  measuring geometry and measures the spectra in the range of 380–730 nm, with a spectral resolution of 10 nm. The short-term repeatability of the spectrophotometer and the uniformity of the printed samples were assessed before sample measurements. The former was evaluated by measuring a high-chroma green sample continuously 40 times within approximately 5 min. The latter was evaluated by measuring five points on the sample. For both tests, the mean color difference from the mean (MCDM) metric, in CIELAB units, was used [30]. The short-term repeatability and the sample uniformity were 0.0006 and 0.04 MCDM, respectively. These values indicate that the

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//44f8550f-c05e-4b59-b8f9-f964b0cab7f3/markdown_3/imgs/img_in_chart_box_291_105_581_364.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A24%3A15Z%2F-1%2F%2F07586e943f57e21729ff5da757e5cdc63cfc65bf2d46ec238e3718fe9cd12e60" alt="Image" width="24%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//44f8550f-c05e-4b59-b8f9-f964b0cab7f3/markdown_3/imgs/img_in_chart_box_597_107_886_363.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A24%3A15Z%2F-1%2F%2F60eaa447712e98f2e7306e063ab2ee3f9c20272ce40e8c60eb21f93b16cf825f" alt="Image" width="24%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//44f8550f-c05e-4b59-b8f9-f964b0cab7f3/markdown_3/imgs/img_in_chart_box_286_404_581_666.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A24%3A15Z%2F-1%2F%2F41e3dc56c5240a71ce067ff549d8e6a16ba750fd9ce94cbb709b3ba512561f16" alt="Image" width="24%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//44f8550f-c05e-4b59-b8f9-f964b0cab7f3/markdown_3/imgs/img_in_chart_box_604_411_914_669.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A24%3A15Z%2F-1%2F%2F75b96f007eb87d3362706e5ebd7891218e4ade1ecb50d16077dad4a09bb7a378" alt="Image" width="26%" /></div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;">Fig. 1. Distribution of the 11 CIE color centers in CIELAB. (a)  $ a^{*}b^{*} $ ; (b)  $ L^{*}a^{*} $ ; and (c)  $ L^{*}b^{*} $  planes; (d) distribution of the samples around the gray center in  $ L^{*}a^{*} $ ,  $ L^{*}b^{*} $ , and  $ a^{*}b^{*} $  planes for a color-difference magnitude of 8 CIELAB units.</div>


instrument has a high repeatability performance and the samples have good uniformity. In addition, for each sample pair, the sample representing the color center was measured only at one point, in the center, while the difference sample was measured at two points and the average of the two measurements calculated. The measurements were repeated during and at the end of the experiments to make sure that the samples underwent no color fading.

### B. Visual Assessment of Color Difference

The widely used gray-scale method was used for the visual assessment of the color difference  $ [9,31] $ . The gray scale was prepared using the same material as the samples. The color specification of the patches is given in Table 2. The gray scale consisted of nine samples, each with a different lightness level including a "standard" sample (i.e., the darkest sample or sample 1) and eight gray-scale samples. The gray-scale samples were prepared in such a way that the differences between the "standard" and each of the samples (samples 1–8) were essentially only a lightness difference: i.e., no variation in chroma  $ C_{ab}^{*} $  or hue angle  $ h_{ab} $ . Equation (1) was fitted to the data to define a relationship between the gray-scale numbers (GS) and their corresponding CIELAB color differences  $ (\Delta E_{ab}^{*}) $ . This equation is commonly used in conjunction with the gray-scale method:

 $$ \Delta V=0.0534\exp(0.701(\mathrm{G S})). $$ 

The visual color differences reported by the observers ( $ \Delta V $ ) and the respective  $ \Delta E_{ab}^{*} $  values should both increase monotonically.

<div style="text-align: center;">Table 2. CIELAB Values of the Gray-Scale Samples Calculated Using the CIE Illuminant D65/1964 Colorimetric Observer Combination</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Gray-Scale Number (GS)</td><td style='text-align: center;'>$ L^{*} $</td><td style='text-align: center;'>$ a^{*} $</td><td style='text-align: center;'>$ b^{*} $</td><td style='text-align: center;'>$ \Delta L^{*} $</td><td style='text-align: center;'>$ \Delta E_{ab}^{*} $</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>41.50</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>1.70</td><td style='text-align: center;'>0.00</td><td style='text-align: center;'>0.00</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>41.20</td><td style='text-align: center;'>0.12</td><td style='text-align: center;'>1.49</td><td style='text-align: center;'>0.29</td><td style='text-align: center;'>0.38</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>41.09</td><td style='text-align: center;'>-0.01</td><td style='text-align: center;'>1.34</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.55</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>42.17</td><td style='text-align: center;'>0.13</td><td style='text-align: center;'>1.42</td><td style='text-align: center;'>0.68</td><td style='text-align: center;'>0.75</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>43.07</td><td style='text-align: center;'>0.09</td><td style='text-align: center;'>1.76</td><td style='text-align: center;'>1.58</td><td style='text-align: center;'>1.58</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>45.14</td><td style='text-align: center;'>0.09</td><td style='text-align: center;'>1.67</td><td style='text-align: center;'>3.65</td><td style='text-align: center;'>3.65</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>48.81</td><td style='text-align: center;'>0.04</td><td style='text-align: center;'>1.39</td><td style='text-align: center;'>7.32</td><td style='text-align: center;'>7.32</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>56.00</td><td style='text-align: center;'>-0.50</td><td style='text-align: center;'>1.17</td><td style='text-align: center;'>14.51</td><td style='text-align: center;'>14.53</td></tr><tr><td style='text-align: center;'>Standard</td><td style='text-align: center;'>41.49</td><td style='text-align: center;'>0.04</td><td style='text-align: center;'>1.71</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

Therefore, Eq. (1) can be used to convert the visual differences to the corresponding  $ \Delta E_{ab}^{*} $  values.

A panel of 19 observers, including 10 males and 9 females, who were undergraduate and graduate students of Zhejiang University, participated in the visual assessment experiments. They were age 22 to 33 years old (i.e., average age of 27.5 years with a standard deviation of 5.5) and all had normal color vision according to the Ishihara Color Vision test. The visual assessments were conducted inside a viewing cabinet equipped with a spectrum-tunable LED lighting system (Thouslite, Changzhou, China) set to simulate CIE D65 illumination. The interior of the viewing cabinet was painted Munsell N7 natural gray. The colorimetric characteristics of the D65 simulator, including the spectral power distribution (SPD), the

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//44f8550f-c05e-4b59-b8f9-f964b0cab7f3/markdown_4/imgs/img_in_image_box_130_104_538_404.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A24%3A16Z%2F-1%2F%2Fad8345c79a9cb7300bda6bde16954e65909b65a17b8c15f5c4d9d9a393d50bde" alt="Image" width="34%" /></div>


<div style="text-align: center;">Fig. 2. Configuration of the test pair and the gray-scale samples in the viewing cabinet. (Note that the gray-scale pair at the bottom left has hairline separation, and the test pair at the bottom right has NS.)</div>


correlated color temperature (CCT), the color rendering index (CRI), and the illuminance were measured using a JETI Specbos 1211 spectroradiometer (Jena, Germany). The light source had a CCT of 6460, a CRI of 97, and an illuminance of 960 lx.

In the psychophysical experiment, the observers sat on a chair in front of the viewing cabinet at a distance of approximately 45 cm from the samples. The illumination:viewing geometry was always approximately  $ 0^{\circ}:45^{\circ} $ . The height of the chair was always adjusted to maintain the viewing distance and hence the viewing angle. The observers were asked to adapt to the mid-gray interior of the cabinet for 3 min. After adaptation, they were provided with the gray-scale samples (GS-1 to GS-8) and a "test pair" with NS for which the color difference was to be evaluated. Figure 2 shows the gray-scale samples and the test pair inside the viewing cabinet. In order to visually assess the color difference of the test pair, the observers were asked to choose one of the gray-scale samples and place it next to the "standard" having the identical color as GS-1. They had to compare the color difference of the test pair with the color difference formed by the "standard" and the gray-scale sample, repeat this comparison until they found the gray-scale sample having the closest color difference to that of the test pair, and report its number (1, 2, ..., 8). Note that the gray-scale pair was viewed under a hairline condition throughout the experiment. Similar conditions were used to collect the visual data used in the development of CIEDE2000.

In order to evaluate the intraobserver variability, the observers assessed the color differences of the 92 pairs associated with the gray color center twice. In total, 1012 sample pairs were visually assessed by each observer in 15–17 separate sessions. Each session was completed without any time restrictions, although it usually lasted 45 min to 1 h for each observer. Overall, 20,976 visual assessments were conducted in about 300 sessions by 19 observers in 576 h (i.e., 30 h for each observer) within a time frame of 2 months.

### 3. RESULTS AND DISCUSSION

### A. Observer Accuracy

The gray-scale numbers reported by the observers (GS) were converted to the corresponding color differences  $ (\Delta V) $  using Eq. (1). The visual color differences  $ (\Delta V) $  were then used to evaluate the observers' accuracy and test the performance of various color-difference formulas. In order to evaluate the extent of observers' accuracy in terms of intraobserver and interobserver variability, the standardized residual sum of squares (STRESS) metric [32] was used. STRESS is the most widely used assessment metric in color-difference research. By comparing two data sets A and B, STRESS can be calculated using Eq. (2):

 $$  STRESS=\left(\frac{\sum_{i=1}^{n}\left(A_{i}-FB_{i}\right)^{2}}{\sum_{i=1}^{n}F^{2}B_{i}^{2}}\right)^{1/2}\times100, $$ 

with  $ F = \sum_{i=1}^{n} A_{i}^{2} / \sum_{i=1}^{n} A_{i} B_{i} $ , where n is the number of sample pairs and F is a scaling factor to adjust A and B data sets to the same scale. The percent STRESS values are always between 0 and 100. Values of STRESS near zero indicate better agreement between two sets of data. In color-difference studies, a STRESS value exceeding 35 is typically an indicator of the poor performance of the color-difference formula [33].

For intraobserver variability, the average STRESS value of the 19 observers was 17. This value indicates that all observers were reasonably internally consistent. Table 3 presents the interobserver variability of the observers in terms of STRESS for different color centers and color-difference magnitudes. The interobserver variability of the 19 observers for all color centers ranged from 16 to 39 STRESS units, with a mean value of 28 units, which is larger than the average intraobserver variability (i.e., 17 STRESS units), as might be expected. This value indicates a reasonable degree of consistency between the observers. The typical interobserver variability for color-difference evaluation is around 35 STRESS units, which has been reported by other researchers [33]. The consistent results presented here may be attributed to the characteristics of the sample set with NS.

Comparing the STRESS values for different color centers in Table 3 shows that the lowest average STRESS value belongs to the gray center, suggesting that the assessment of the color difference of the gray stimuli might be easier for observers than the other color centers. The results shown in Table 3 also indicate that observers showed better performance in the assessment of the color difference of sample pairs in the  $ L^{*}a^{*} $  and  $ L^{*}b^{*} $  planes as compared to the  $ a^{*}b^{*} $  plane, given the average STRESS values of 24, 25, and 34, respectively. The mean STRESS value of the observations decreases with increasing color-difference magnitude. In other words, a higher observation variability is found when assessing the color difference of pairs having smaller color differences.

### B. Correlation between Various Visual Data Sets

The results of experiments on color difference can be conveniently summarized and compared as chromatic discrimination ellipses. For each color center, color discrimination can be represented by the ellipsoid equation,

 $$ \begin{aligned}\Delta E^{2}&=k_{1}\Delta a^{*2}+k_{2}\Delta a^{*}\Delta b^{*}+k_{3}\Delta b^{*2}+k_{4}\Delta a^{*}\Delta L^{*}\\&\quad+k_{5}\Delta b^{*}\Delta L^{*}+k_{6}\Delta L^{*2},\end{aligned} $$ 

where coefficients  $ k_{1} $  to  $ k_{6} $  are optimized to give the lowest STRESS value between the color differences calculated using

<div style="text-align: center;">Table 3. Interobserver Variability of Observers in Terms of STRESS for Different Color Centers and Color-Difference Magnitudes</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">Color Center</td><td rowspan="2">$ L^{*}a^{*} $</td><td rowspan="2">$ L^{*}b^{*} $</td><td rowspan="2">$ a^{*}b^{*} $</td><td colspan="4">$ \Delta E_{M} $</td><td rowspan="2">Overall STRESS</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>2</td><td style='text-align: center;'>4</td><td style='text-align: center;'>8</td></tr><tr><td style='text-align: center;'>Gray</td><td style='text-align: center;'>17</td><td style='text-align: center;'>19</td><td style='text-align: center;'>24</td><td style='text-align: center;'>29</td><td style='text-align: center;'>22</td><td style='text-align: center;'>20</td><td style='text-align: center;'>19</td><td style='text-align: center;'>22</td></tr><tr><td style='text-align: center;'>Red</td><td style='text-align: center;'>24</td><td style='text-align: center;'>24</td><td style='text-align: center;'>33</td><td style='text-align: center;'>35</td><td style='text-align: center;'>30</td><td style='text-align: center;'>30</td><td style='text-align: center;'>27</td><td style='text-align: center;'>30</td></tr><tr><td style='text-align: center;'>High-chroma orange</td><td style='text-align: center;'>23</td><td style='text-align: center;'>23</td><td style='text-align: center;'>34</td><td style='text-align: center;'>33</td><td style='text-align: center;'>30</td><td style='text-align: center;'>27</td><td style='text-align: center;'>26</td><td style='text-align: center;'>29</td></tr><tr><td style='text-align: center;'>Yellow</td><td style='text-align: center;'>23</td><td style='text-align: center;'>26</td><td style='text-align: center;'>39</td><td style='text-align: center;'>44</td><td style='text-align: center;'>35</td><td style='text-align: center;'>27</td><td style='text-align: center;'>24</td><td style='text-align: center;'>29</td></tr><tr><td style='text-align: center;'>High-chroma yellow green</td><td style='text-align: center;'>25</td><td style='text-align: center;'>25</td><td style='text-align: center;'>36</td><td style='text-align: center;'>41</td><td style='text-align: center;'>31</td><td style='text-align: center;'>28</td><td style='text-align: center;'>24</td><td style='text-align: center;'>28</td></tr><tr><td style='text-align: center;'>Green</td><td style='text-align: center;'>25</td><td style='text-align: center;'>25</td><td style='text-align: center;'>37</td><td style='text-align: center;'>39</td><td style='text-align: center;'>32</td><td style='text-align: center;'>29</td><td style='text-align: center;'>24</td><td style='text-align: center;'>29</td></tr><tr><td style='text-align: center;'>High-chroma green</td><td style='text-align: center;'>19</td><td style='text-align: center;'>22</td><td style='text-align: center;'>30</td><td style='text-align: center;'>30</td><td style='text-align: center;'>26</td><td style='text-align: center;'>26</td><td style='text-align: center;'>21</td><td style='text-align: center;'>25</td></tr><tr><td style='text-align: center;'>Blue-green</td><td style='text-align: center;'>28</td><td style='text-align: center;'>29</td><td style='text-align: center;'>36</td><td style='text-align: center;'>46</td><td style='text-align: center;'>33</td><td style='text-align: center;'>29</td><td style='text-align: center;'>27</td><td style='text-align: center;'>31</td></tr><tr><td style='text-align: center;'>Blue</td><td style='text-align: center;'>32</td><td style='text-align: center;'>30</td><td style='text-align: center;'>35</td><td style='text-align: center;'>56</td><td style='text-align: center;'>39</td><td style='text-align: center;'>28</td><td style='text-align: center;'>27</td><td style='text-align: center;'>30</td></tr><tr><td style='text-align: center;'>High-chroma purple</td><td style='text-align: center;'>22</td><td style='text-align: center;'>25</td><td style='text-align: center;'>38</td><td style='text-align: center;'>35</td><td style='text-align: center;'>29</td><td style='text-align: center;'>26</td><td style='text-align: center;'>25</td><td style='text-align: center;'>28</td></tr><tr><td style='text-align: center;'>Black</td><td style='text-align: center;'>24</td><td style='text-align: center;'>24</td><td style='text-align: center;'>33</td><td style='text-align: center;'>36</td><td style='text-align: center;'>29</td><td style='text-align: center;'>27</td><td style='text-align: center;'>24</td><td style='text-align: center;'>27</td></tr><tr><td style='text-align: center;'>Mean</td><td style='text-align: center;'>24</td><td style='text-align: center;'>25</td><td style='text-align: center;'>34</td><td style='text-align: center;'>39</td><td style='text-align: center;'>30</td><td style='text-align: center;'>27</td><td style='text-align: center;'>24</td><td style='text-align: center;'>28</td></tr></table>

Eq. (3) and the visual data ( $ \Delta V $ ) for each color center. Setting  $ \Delta E $  to unity allows calculation of  $ \Delta L^{*} $ ,  $ \Delta a^{*} $ , and  $ \Delta b^{*} $  values of an ellipsoid corresponding to  $ \Delta V $  of 1. Setting  $ \Delta L^{*} $  to zero allows the corresponding ellipse in  $ \Delta a^{*}\Delta b^{*} $  plane to be calculated. The ellipse equation for the present data set, referred to as the ZJU (Zhejiang University) data set, was fitted for each color-difference magnitude (i.e.,  $ \Delta E_{M} $  of 1, 2, 4, and 8), separately.

Figure 3 plots the fitted ellipses in the  $ a^{*}b^{*} $  plane. There exists a general agreement between various color-difference magnitudes in terms of the ellipse shape and orientation. However, the larger ellipses are obtained for larger color differences. Moreover, the smallest ellipses are located at the origin, and the ellipse size increases by increasing the chroma. Also, most of the ellipses are oriented towards the origin, except for those in the blue region.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//44f8550f-c05e-4b59-b8f9-f964b0cab7f3/markdown_5/imgs/img_in_image_box_99_943_568_1389.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A24%3A16Z%2F-1%2F%2F1ff0cd05d7f48e736de6ebec411347fbb01171768b0c34480703f854c02a050a" alt="Image" width="39%" /></div>


<div style="text-align: center;">Fig. 3. Chromatic discrimination ellipses of 11 color centers for various color difference magnitudes in  $ a^{*}b^{*} $  plane: blue,  $ \Delta E_{M}=1 $ ; red,  $ \Delta E_{M}=2 $ ; black,  $ \Delta E_{M}=4 $ ; green,  $ \Delta E_{M}=8 $ .</div>


The ZJU ellipses were compared with four previously published data sets (Witt, RIT–DuPont, Cheung and Rigg [34], and Cui et al.). It is reasonable to compare these data sets because they were all generated based on the five CIE color centers.

Figure 4 shows the ellipses fitted to the visual differences obtained for the color-difference magnitude of 8, i.e., ZJU_8, together with the ellipses of the above-mentioned four data sets, in an  $ a*b* $  diagram. The ZJU_8 ellipses were chosen because they always gave the best agreement with the ellipses from the other studies. The LMG0N subset representing the pairs with NS was selected from Cui's data set for comparison with the present data. The F parameter in Eq. (2) was used as the scaling factor for adjusting the sizes of the ellipses from different data sets. It automatically adjusts the  $ \Delta E $  in Eq. (3) to have the same size as the visual data.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//44f8550f-c05e-4b59-b8f9-f964b0cab7f3/markdown_5/imgs/img_in_image_box_625_944_1098_1392.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A24%3A16Z%2F-1%2F%2Fb4480db404c58adf1018009e72749e33996f6fe75fdb3aea0dd158c8dca2c47a" alt="Image" width="39%" /></div>


<div style="text-align: center;">Fig. 4. Chromatic discrimination ellipses of the five CIE color centers for different data sets in  $ a^{*}b^{*} $  plane: black, ZJU_8; green, Witt; red, Cheung and Rigg; cyan, RIT–DuPont; blue, Cui-LMG0N.</div>


Most of the data sets were generated using surface colors, except for Cui et al. data, which was produced based on CRT colors, including 16 subsets, varying in sample size, background color, separation, and color of separation, among which the LMG0N and the LMG1B subsets are of interest in this work. The LMG0N subset was generated against a mid-gray background with NS. The LMG1B subset, however, was generated using the same conditions as LMG0N except for a 1-pixel black dividing line between the samples. (Note that the other subsets were not used because they were generated using different colored backgrounds or larger separation distances.) on color-difference perception and there is not much difference between color-difference perception of surface and self-luminous colors with NS.

### C. Performance of Various Color-Difference Formulas

Equation (4) shows a generic color-difference formula, including the lightness, chroma, and hue parametric factors,  $ k_{L} $ ,  $ k_{C} $ , and  $ k_{H} $  for the lightness, chroma, and hue, respectively, designed to consider different viewing parameters such as texture, background, separation, etc.:

 $$ \Delta E=\sqrt{\left(\frac{\Delta L}{k_{L}S_{L}}\right)^{2}+\left(\frac{\Delta C}{k_{C}S_{C}}\right)^{2}+\left(\frac{\Delta H}{k_{H}S_{H}}\right)^{2}+RT\left(\frac{\Delta C}{k_{C}S_{C}}\right)\left(\frac{\Delta H}{k_{H}S_{H}}\right)}, $$ 

Figure 5 shows the correlation between the ZJU data set and the other data sets in terms of the STRESS parameter.

Although the ZJU ellipses agree reasonably well with the other data sets, it can be seen in Fig. 5 that the ZJU_8 subset agrees the best with the other sets in terms of the shape and orientation of the ellipses, but not the size. This is most likely due to the smaller interobserver variability associated with this subset (see Table 3). Additionally, irrespective of the magnitude of color difference, the ZJU ellipses agree the best with the Witt and RIT–DuPont ellipses, and the worst with Cheung and Rigg's ellipses. This discrepancy is most likely attributed to the texture of the surface colors used in these studies. Although the pairs in the three data sets were assessed under the hairline condition, due to having unsmooth edges, the textile pairs in Cheung and Rigg's work presented a wider gap than the paint samples in the RIT–DuPont and the Witt sets. This suggests that even the width of the hairline has a big impact on the visual results.

Comparing with the LMG0N and the LMG1B subsets from Cui's data set, the ZJU data set agrees markedly better with LGM0N, which was produced using the sample pairs with NS. This suggests that separation has a great impact

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//44f8550f-c05e-4b59-b8f9-f964b0cab7f3/markdown_6/imgs/img_in_chart_box_130_1108_541_1408.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A24%3A17Z%2F-1%2F%2Fe712672e4a7a0344246656fc2801274b9a43dd21344c4518341efdea3046a516" alt="Image" width="34%" /></div>


<div style="text-align: center;">Fig. 5. Correlation between the ZJU data set and the Witt, Cheung and Rigg, RIT–DuPont and Cui et al. data sets in terms of STRESS.</div>


where  $ \Delta L $ ,  $ \Delta C $ , and  $ \Delta H $  are differences in lightness, chroma, and hue,  $ k_{L} $ ,  $ k_{C} $ , and  $ k_{H} $  are the parametric factors and the  $ S_{L} $ ,  $ S_{C} $ , and  $ S_{H} $  are the weighting functions for the lightness, chroma, and hue components, respectively. RT is the rotation function provided to improve the performance of the color-difference formula when fitting chromatic differences in the blue region of color space [6]. Note that the parametric factors were designed for different applications, e.g., for the CIEDE2000 and CIE94 formulas,  $ k_{L} = k_{C} = k_{H} = 1 $  for samples having a smooth surface such as paint and plastic patches, while  $ k_{L} = 2 $  and  $ k_{C} = k_{H} = 1 $  for rough surfaces such as textile samples.

The performance of a set of color-difference formulas, including CIELAB, CMC, CIEDE2000, CIE94, CAM02-UCS, and CAM16-UCS, was tested using the present data set. In order to investigate the separation and color-difference magnitude effects on the performance of each formula, three forms of color-difference formula were tested: the original, the power-corrected [35], and the parametric factor-optimized [21] equations. It is expected that the last two modifications should enhance the performance of all formulas.

In the first test, the original form of each color-difference formula in which  $ k_{L} = k_{C} = k_{H} = 1 $  was used. The performance of each formula in predicting the visual differences was then evaluated in terms of the STRESS parameter. The respective STRESS values are compared as bar charts in Fig. 6(a), and it can be seen that in original form, when  $ k_{L} = k_{C} = k_{H} = 1 $ , all formulas markedly outperformed the CIELAB and the CMC formula. CIE94 performed the best overall followed by CAM16-UCS, CAM02-UCS, and CIEDE2000.

One of the advantages of using the STRESS parameter to evaluate the strength of the relationship between the perceived and predicted color differences is the possibility of implementing the F-test using the STRESS values, to test the statistical difference between two color-difference formulas  $ [32] $ . For two given color-difference formulas,  $ DE_{1} $  and  $ DE_{2} $ , the F value can be calculated by Eq. (5):

 $$ F=\frac{STRESS_{DE_{1}}^{2}}{STRESS_{DE_{2}}^{2}}. $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//44f8550f-c05e-4b59-b8f9-f964b0cab7f3/markdown_7/imgs/img_in_chart_box_157_106_589_412.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A24%3A17Z%2F-1%2F%2F3be000c24c72528f40cb5efdf54a893881599d6787fb8d26d47b9ee3e7b2cb04" alt="Image" width="36%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//44f8550f-c05e-4b59-b8f9-f964b0cab7f3/markdown_7/imgs/img_in_chart_box_611_108_1042_413.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A24%3A17Z%2F-1%2F%2F4e44e724afc86f2fe86e8136ec6e68516bc837e79688501fa11587c59ff081d5" alt="Image" width="36%" /></div>


<div style="text-align: center;">Fig. 6. Performance of the original, the power-corrected, and the parametric factor-optimized color-difference formulas in terms of STRESS for (a) six formulas; (b) CIEDE2000.</div>


The F value was used to compare the performance of the formulas after each modification. For the present data set, the critical F value,  $ F_{C} $ , for the two-tailed F distribution with a 95% confidence level and  $ (\infty, \infty) $  degrees of freedom is 1. Considering that the number of the samples was large (N = 1012), an infinite number of degrees of freedom could be assumed. No significant difference was found among the CAM02-UCS, the CAM16-UCS, and the CIEDE2000 formulas according to the F-test.

The next test was to apply a power factor to the formulas. Huang et al. [35] found that introducing a single power factor could lead to an overall improvement in the performance of the formula regardless of the color-difference magnitude. As was expected, the performance of all formulas improved slightly after power correction. However, again according to the F-test, there was no significant difference among the three improved formulas.

In the last test, the color-difference formulas were modified by optimizing the chroma and lightness parametric factors,  $ k_{C} $  and  $ k_{L} $ , with  $ k_{H}=1 $ , to give the best fit to the visual differences. Again, the performance of all formulas improved according to the F-test. However, it was found that the chroma parametric factor  $ k_{C} $  is always larger than  $ k_{L} $ , indicating that all formulas predicted a larger lightness difference compared to the chroma difference with the hue difference in between. For all formulas except CIELAB, the  $ k_{C} $  values were close to 1, ranging from 0.82 to 0.93, while the  $ k_{L} $  values were always less than 1. This means that the chroma and hue differences were well balanced (i.e.,  $ k_{C} \approx k_{H} = 1 $ ), and only the lightness difference affected the total color difference. A  $ k_{L} $  value less than 1 results from a larger perceived lightness difference; hence a larger total color difference is perceived for pairs with NS [see Eq. (4)]. Again, this behavior might be attributed to the separation effect, i.e., the larger perceived color difference, which is mainly a lightness difference when there is no hairline or separation between the samples.

In order to test this premise, all formulas were modified only for the  $ k_{L} $  factor with  $ k_{C} = k_{H} = 1 $ . Figure 6(a) shows that the performance of all modified formulas improved. Although the improvement was not significant according to the F-test, this result still indicates that only applying the  $ k_{L} $  factor should be sufficient to describe the effect of color-difference magnitude. Figure 6(b) illustrates the performance of the CIEDE2000 color-difference formula for the ZJU data set and various color-difference magnitudes together with the corresponding optimized  $ k_{L} $  values. It can be seen that all the optimized  $ k_{L} $  values are less than 1 and proportional to the size of the color difference. Note that CIEDE2000 with  $ k_{L} = k_{C} = k_{H} = 1 $  was developed using all the previous data, which were generated under the hairline viewing condition. For the current results, however, the  $ k_{L} $  values less than 1 indicate that there is a parametric effect due to the separation.

The present results demonstrated that the perceived lightness difference of pairs with NS is larger than the perceived lightness difference of pairs with hairline separation. This result is in line with the findings of Boynton and his colleagues  $ [27] $ . However, we found that chromatic difference (i.e., excluding lightness) difference appears to be less affected by separation.

### D. Developing a Color-Difference Equation for Pairs with NS

As demonstrated in the previous section, changing the size of the color difference affects the total color-difference perception when there is no hairline or gap between the samples. The perceived color difference for pairs with NS is larger, and it is mainly due to the lightness difference, while the hue and chroma differences are well balanced. Considering this effect, a new equation for the lightness difference parametric factor is proposed as a linear function of color difference  $ (\Delta E) $ . The new lightness difference parametric factor  $ (D_{L}) $  is given in Eq. (6):

 $$ D_{L}=a\Delta E+b, $$ 

where  $ \Delta E $  is the color difference, and a and b are constants to be optimized. The optimized a and b values for each tested color difference formula are given in Table 4. Note that  $ D_{L} $  values are less than 1.0 unless the color difference exceeds 15.6, 9.1, 8.3, 10.3, and 10.3 for CIELAB, CIEDE2000, CIE94, CAM02-UCS, and CAM16-UCS, respectively. In other words, the lightness difference is perceived to be more visible than the chroma and hue differences until it reaches

<div style="text-align: center;">Table 4. Optimized a, b, c, and d Coefficients for Various Color-Difference Formulas</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Color Difference Formula</td><td style='text-align: center;'>a</td><td style='text-align: center;'>b</td><td style='text-align: center;'>c</td><td style='text-align: center;'>d</td></tr><tr><td style='text-align: center;'>CIELAB</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.22</td><td style='text-align: center;'>0.72</td><td style='text-align: center;'>0.95</td></tr><tr><td style='text-align: center;'>CIEDE2000</td><td style='text-align: center;'>0.08</td><td style='text-align: center;'>0.27</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.91</td></tr><tr><td style='text-align: center;'>CIE94</td><td style='text-align: center;'>0.08</td><td style='text-align: center;'>0.34</td><td style='text-align: center;'>0.73</td><td style='text-align: center;'>0.94</td></tr><tr><td style='text-align: center;'>CAM02-UCS</td><td style='text-align: center;'>0.07</td><td style='text-align: center;'>0.28</td><td style='text-align: center;'>0.72</td><td style='text-align: center;'>0.93</td></tr><tr><td style='text-align: center;'>CAM16-UCS</td><td style='text-align: center;'>0.07</td><td style='text-align: center;'>0.27</td><td style='text-align: center;'>0.73</td><td style='text-align: center;'>0.93</td></tr></table>

a certain level of color difference, after which the perceived lightness difference starts to be less important.

To find the formula with the highest performance, three modified versions were proposed for each color-difference formula: the magnitude-corrected equation, $\Delta E_{1}$, the power-corrected equation, $\Delta E_{2}$, and the magnitude-power-corrected equation, $\Delta E_{3}$. Their generic forms are given in Eqs. (7)–(9):

 $$ \Delta E_{1}=\sqrt{\left(\frac{\Delta L}{D_{L}}\right)^{2}+(\Delta C)^{2}+(\Delta H)^{2}+\mathrm{R T}}, $$ 

 $$ \Delta E_{2}=\Big[\sqrt{(\Delta L)^{2}+(\Delta C)^{2}+(\Delta H)^{2}+\mathrm{R T}}\Big]^{c}, $$ 

 $$ \Delta E_{3}=\left[\sqrt{\left(\frac{\Delta L}{D_{L}}\right)^{2}+(\Delta C)^{2}+(\Delta H)^{2}+\mathrm{R T}}\right]^{d}, $$ 

where RT is the rotation function, which needs to be set to zero for all formulas except for CIEDE2000, and c and d are power factors, which were obtained by minimizing the STRESS values between each formula and the present visual data. The optimized values are shown in Table 4. Comparing the optimized coefficients in Table 4 indicates that the coefficients do not vary much across the color-difference formulas. The performance of the five formulas after optimization was tested in terms of STRESS, and the results are compared in Fig. 7(a). Additionally, the performance of the modified CIEDE2000 formula is summarized in Fig. 7(b).

Both power correction and magnitude correction are intended to improve the performance of color-difference equations. By comparing the STRESS values in Fig. 7, it can be seen that although power correction enhanced the performance of all formulas  $ (\Delta E_{2}) $ , the improvement was not very obvious. The F-test also showed no significant difference between the original and the power-corrected  $ (\Delta E_{2}) $  formulas. On the other hand, after applying the new lightness-difference parametric factor  $ (D_{L}) $  in the original formula,  $ \Delta E_{1} $  showed a markedly better performance, as the STRESS values drastically decreased.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//44f8550f-c05e-4b59-b8f9-f964b0cab7f3/markdown_8/imgs/img_in_chart_box_157_1097_586_1430.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A24%3A18Z%2F-1%2F%2F93f833545c3b8e64e0c506808cd93d995a732e2a59cc340ca1ff5c4f0a7179dc" alt="Image" width="36%" /></div>


Further improvement in the performance of the formulas was not achieved after power correction of  $ \Delta E_{1} $ . As can be seen in Fig. 7, there is not a large improvement from  $ \Delta E_{1} $  to  $ \Delta E_{3} $ , as the corresponding STRESS values are very close. Again, CIE94 followed by CAM16-UCS and CIEDE2000 performed very well, and all formulas outperformed CIELAB.

It is encouraging that the magnitude-corrected CIEDE2000 formula gave one of the most accurate predictions of all the color-difference formulas. Hence, this equation is designated as the "color-difference formula for 'no-separation' viewing condition,"  $ \Delta E_{NS} $ , which is given in Eq. (10):

 $$ \Delta E_{\mathrm{N S}}=\sqrt{\left(\frac{\Delta L^{\prime}}{D_{L}}\right)^{2}+(\Delta C^{\prime})^{2}+(\Delta H^{\prime})^{2}+\mathrm{R T}(\Delta C^{\prime})(\Delta H^{\prime})}, $$ 

with  $ D_{L}=0.08\Delta E_{00}+0.27 $ , where  $ \Delta L' $ ,  $ \Delta C' $ , and  $ \Delta H' $  are the CIEDE2000 terms for lightness, chroma, and hue differences,  $ \mathrm{RT}(\Delta C')(\Delta H') $  is the interactive term between chroma and hue differences, and  $ \Delta E_{00} $  is the CIEDE2000 color difference. These terms are calculated according to the same procedure used to calculate the CIEDE2000. A worked example of the calculation of  $ \Delta E_{NS} $  is given in Appendix A.

Equation (10) can well describe the visual phenomena observed in the experiment. When  $ \Delta E_{00} $  is smaller than 9.1, a larger color-difference magnitude results in a higher value of  $ D_{L} $ , leading to a lower lightness difference  $ (\Delta L^{\prime}/D_{L}) $ , and a lower  $ \Delta E_{NS} $  value. This implies that the border between the two samples is important for judging the color difference. A clear perceived border will reduce the perceived color difference. This is in agreement with the findings of Cui et al. [25]. For  $ \Delta E_{00} $  values larger than 9.1, the effect is the opposite, i.e., a larger color difference will lead to a larger  $ D_{L} $ , but results in a

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//44f8550f-c05e-4b59-b8f9-f964b0cab7f3/markdown_8/imgs/img_in_chart_box_607_1098_1038_1429.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A24%3A18Z%2F-1%2F%2F92149ea4b5c6f785ac48910bf0f4aacbeb7dd644e36070ecbaaf5d0740df7ca7" alt="Image" width="36%" /></div>


<div style="text-align: center;">Fig. 7. Performance of original and modified color-difference formula in terms of STRESS for (a) five formulas; (b) CIEDE2000.</div>


smaller  $ (\Delta L^{\prime}/D_{L}) $  and hence a smaller  $ \Delta E_{NS} $ . However, further experimentation is required to verify the latter conclusion.

 $ \Delta E_{NS} $  is proposed for applications where there is no hairline or separation gap between the sample pairs under judgment. The formula is now being extensively tested by HP Inc., and the results of its performance evaluation will be reported in the near future.

### 4. CONCLUSIONS

Using a series of printed color-difference pairs without separation, a comprehensive color discrimination data set was accumulated, and the effect of separation and color-difference magnitude on the performance of various color-difference formulas was investigated. Modifying some of the advanced color-difference formulas by optimizing the lightness parametric factor,  $ k_{L} $ , resulted in an improvement in the performance of the formulas. The findings imply that for pairs with NS, the lightness difference has the major contribution to the total color difference, although such an effect is reduced by increasing the size of the color difference. Based on the results, a new lightness-difference parametric equation is proposed as a linear function of the color difference. The new function has been applied to various color-difference formulas, and the performance of all tested formulas was markedly improved. A new color-difference formula based on CIEDE2000 was developed for sample pairs with NS, covering a wide range of color-difference magnitudes smaller than 9.1 CIEDE2000 units. The new equation is designated as the color-difference formula for NS viewing condition:  $ \Delta E_{NS} $ . Further research should be carried out to verify the present results, especially for color differences larger than  $ 9.1 \Delta E_{00} $  units.

## APPENDIX A:  $ \Delta E_{NS} $  WORKED EXAMPLE

This example shows how to calculate the color difference between a standard (S) and a sample patch (P) using the  $ \Delta E_{NS} $  equation. See Tables 5 and 6. Two sets of input data are given. The XYZ tristimulus values were calculated using the CIE D65 illuminant and the 1964 standard colorimetric observer.

<div style="text-align: center;">Table 5. Input Values for the Worked Examples</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="3">Reference White</td><td colspan="3">Pair 1</td><td colspan="3">Pair 2</td></tr><tr><td style='text-align: center;'>$ X_{n} $</td><td style='text-align: center;'>$ Y_{n} $</td><td style='text-align: center;'>$ Z_{n} $</td><td style='text-align: center;'>X</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>Z</td><td style='text-align: center;'>X</td><td style='text-align: center;'>Y</td><td style='text-align: center;'>Z</td></tr><tr><td style='text-align: center;'>95.78</td><td style='text-align: center;'>100.00</td><td style='text-align: center;'>104.61</td><td style='text-align: center;'>$ S_{1} $</td><td style='text-align: center;'>8.90</td><td style='text-align: center;'>9.53</td><td style='text-align: center;'>23.10</td><td style='text-align: center;'>$ S_{2} $</td><td style='text-align: center;'>58.26</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>$ P_{1} $</td><td style='text-align: center;'>9.21</td><td style='text-align: center;'>9.72</td><td style='text-align: center;'>23.38</td><td style='text-align: center;'>$ P_{2} $</td><td style='text-align: center;'>59.10</td></tr></table>

<div style="text-align: center;">Table 6. Intermediate and Final Output Values for the Worked Examples</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>$ L^{*} $</td><td style='text-align: center;'>$ a^{*} $</td><td style='text-align: center;'>$ b^{*} $</td><td style='text-align: center;'>$ C^{*} $</td><td style='text-align: center;'>$ \Delta E_{00} $</td><td style='text-align: center;'>$ D_{L} $</td><td style='text-align: center;'>$ \Delta E_{\mathrm{NS}} $</td></tr><tr><td style='text-align: center;'>$ S_{1} $</td><td style='text-align: center;'>36.99</td><td style='text-align: center;'>-1.92</td><td style='text-align: center;'>-29.53</td><td style='text-align: center;'>29.59</td><td style='text-align: center;'>0.95</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>1.25</td></tr><tr><td style='text-align: center;'>$ P_{1} $</td><td style='text-align: center;'>37.34</td><td style='text-align: center;'>-0.82</td><td style='text-align: center;'>-29.42</td><td style='text-align: center;'>29.43</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>$ S_{2} $</td><td style='text-align: center;'>84.1</td><td style='text-align: center;'>-7.82</td><td style='text-align: center;'>48.76</td><td style='text-align: center;'>49.38</td><td style='text-align: center;'>0.61</td><td style='text-align: center;'>0.32</td><td style='text-align: center;'>0.80</td></tr><tr><td style='text-align: center;'>$ P_{2} $</td><td style='text-align: center;'>84.36</td><td style='text-align: center;'>-6.91</td><td style='text-align: center;'>48.10</td><td style='text-align: center;'>48.59</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

Funding. National Natural Science Foundation of China (NSFC) (61775190); HP Inc. Barcelona, Spain.

## REFERENCES

1. Commission Internationale de l'Eclairage (CIE), Colorimetry, CIE Publication No. 15 (CIE Central Bureau, 2004).

2. H. Wang, G. H. Cui, M. R. Luo, and H. S. Xu, “Evaluation of colour difference formulae for different colour difference magnitudes,” Color Res. Appl. 37, 316–325 (2012).

3. A. R. Robertson, “CIE guidelines for coordinated research on colour difference evaluation,” Color Res. Appl. 3, 149–151 (1978).

4. K. Witt, “CIE guidelines for coordinated future work on industrial colour-difference evaluation,” Color Res. Appl. 20, 399–403 (1995).

5. F. J. J. Clarke, R. McDonald, and B. Rigg, "Modification to the JPC79 colour-difference formula," J. Soc. Dyers Colour. 100, 128–132 (1984).

6. M. R. Luo, G. Cui, and B. Rigg, “The development of the CIE 2000 colour-difference formula: CIEDE2000,” Color Res. Appl. 26, 340–350 (2001).

7. M. R. Luo and B. Rigg, "BFD (l:c) colour-difference formula. Part I: Development of the formula," J. Soc. Dyers Colour. 103, 86–94 (1987).

8. M. R. Luo and B. Rigg, “BFD (l:c) colour-difference formula. Part II: Performance of the formula,” J. Soc. Dyers Colour. 103, 126–132 (1987).

9. "Textiles—Tests for Colour Fastness: grey scale for assessing change in colour," ISO 105-A02:1993 (ISO, 1993).

10. R. S. Berns, D. H. Alman, L. Reniff, G. D. Snyder, and M. R. Balonon-Rosen, "Visual determination of suprathreshold color difference tolerances using probit analysis," Color Res. Appl. 16, 297–316 (1991).

11. Commission Internationale de l'Eclairage (CIE), "Industrial colour-difference evaluation," CIE Publication No. 116 (CIE Central Bureau, 1995).

12. D. H. Kim and J. H. Nobbs, "New weighting functions for the weighted CIELAB colour-difference formula," in Proceedings of the AIC (AIC, 1997), pp. 446–449.

13. K. Witt, “Geometric relations between scales of small colour differences,” Color Res. Appl. 24, 78–92 (1999).

14. “Colorimetry-Part 6: CIEDE2000 colour-difference formula,” ISO/CIE 11664–6:2014(E) (CIE Central Bureau, 2014).

15. M. R. Luo, G. Cui, and C. Li, “Uniform colour spaces based on CIECAM02 colour appearance model,” Color Res. Appl. 31, 320–330 (2006).

16. Commission Internationale de l'Eclairage (CIE), "A colour appearance model for colour management systems: CIECAM02," CIE Publication No. 159 (CIE Central Bureau, 2004).

17. C. Li, Z. Li, Z. Wang, Y. Xu, M. R. Luo, G. Cui, M. Melgosa, M. H. Brill, and M. Pointer, “Comprehensive color solutions: CAM16, CAT16, and CAM16-UCS,” Color Res. Appl. 42, 703–718 (2017).

18. Commission Internationale de l'Eclairage (CIE), JTC 10 (D8/D1): A Nnew Colour Appearance Model for Colour Management Systems: CIECAM16 (CIE, 2019).

19. S. Morillas and M. D. Fairchild, "Using suprathreshold color difference ellipsoids to estimate any perceptual color difference," J. Visual Commun. Image Represent. 55, 142–148 (2018).

20. K. Witt, “Parametric effects on surface color difference evaluation at threshold,” Color Res. Appl. 15, 189–199 (1990).

21. S. Guan and M. R. Luo, “Investigation of parametric effects using small colour differences,” Color Res. Appl. 24, 331–343 (1999).

22. S. Guan and M. R. Luo, “Investigation of parametric effects using large colour differences,” Color Res. Appl. 24, 356–368 (1999).

23. J. H. Xin, C. C. Lam, and M. R. Luo, “Investigation of parametric effects using medium colour difference pairs,” Color Res. Appl. 26, 376–383 (2001).

24. H. Xu and H. Yaguchi, “Visual evaluation at scale of threshold to suprathreshold color difference,” Color Res. Appl. 30, 198–208 (2005).

25. G. Cui, M. R. Luo, B. Rigg, and W. Li, "Colour-difference evaluation using CRT colours. Part I: Data gathering and testing colour-difference formulae," Color Res. Appl. 26, 394–402 (2001).

26. G. Cui, M. R. Luo, B. Rigg, and W. Li, "Colour-difference evaluation using CRT colours. Part II: Parametric effects," Color Res. Appl. 26, 403–412 (2001).

27. R. M. Boynton, M. M. Hayhoe, and D. I. A. MacLeod, "The gap effect: chromatic and achromatic visual discrimination as affected by field separation," Opt. Acta 24, 159–177 (1977).

28. E. D. Montag, “Influence of boundary information on the perception of color,” J. Opt. Soc. Am. A 14, 997–1006 (1997).

29. R. T. Eskew, “The gap effect revisited: slow changes in chromatic sensitivity as affected by luminance and chromatic borders,” Vis. Res. 29, 717–729 (1989).

30. F. W. Billmeyer and P. J. Alessi, “Assessment of color-measuring instruments,” Color Res. Appl. 6, 195–202 (1981).

31. M. R. Luo and B. Rigg, “Chromaticity-discrimination ellipses for surface colours,” Color Res. Appl. 11, 25–42 (1986).

32. P. A. García, R. Huertas, M. Melgosa, and G. Cui, “Measurement of the relationship between perceived and computed color differences,” J. Opt. Soc. Am. A 24, 1823–1829 (2007).

33. M. Huang, H. Liu, G. Cui, and M. R. Luo, “Testing uniform color spaces and color difference formulae using printed samples,” Color Res. Appl. 37, 326–335 (2012).

34. M. Cheung and B. Rigg, "Colour-difference ellipsoids for five colour centers," Color Res. Appl. 11, 185–195 (1986).

35. M. Huang, G. Cui, M. Melgosa, M. Sánchez-Marañón, C. Li, M. R. Luo, and H. Liu, “Power functions improving the performance of color difference formulas,” Opt. Express 23, 597–610 (2015).

