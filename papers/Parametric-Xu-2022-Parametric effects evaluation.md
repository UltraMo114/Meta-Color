# Parametric effects in color-difference evaluation

Qiang Xu, Keyu Shi, and Ming Ronnier Luo $ ^{*} $ 

State Key Laboratory of Modern Optical Instrument, Zhejiang University, Hangzhou, China

 $ ^{*} $ m.r.luo@zju.edu.cn

Abstract: An experiment was conducted to investigate three parameters affecting color-difference evaluation on a display: 4 sample sizes ( $ 2^{\circ} $ ,  $ 4^{\circ} $ ,  $ 10^{\circ} $ , and  $ 20^{\circ} $ ), 2 color-difference magnitudes (4 and 8 CIELAB units), and 2 separations (inclusion or exclusion of the separation line between two colors in a pair). Sample pairs surrounding 5 CIE recommended color centers were prepared. In total, 1120 sample pairs of colors were assessed 20 times using the grey-scale method. The experimental results were used to reveal various parametric effects and to verify the performance of different color matching functions (CMFs) and four color difference formulae and uniform color spaces. It was found that there was little difference in terms of  $ \Delta E $  values calculated using different CMFs for all the color models tested. A parametric formula was proposed to predict three parametric effects for sample pairs having no-separation line: 1) differences in sample size, 2) media (surface and self-luminous colors), and 3) color-difference magnitudes.

© 2022 Optica Publishing Group under the terms of the Optica Open Access Publishing Agreement

### 1. Introduction

Color-difference has been extensively investigated for over a century and, as a result, a number of color-difference formulae have been developed to evaluate color-difference. Significant progress was made after the recommendation of CIELAB  $ [1] $  in 1976, leading to further advanced color-difference formulae  $ [2-6] $  until the recommendation of CIEDE2000  $ [7] $ . The latter formula is the official recommendation of CIE  $ [8] $  and it is widely used across many industries. In 2006, CAM02-UCS  $ [9] $ , based on the CIE 2002 color appearance model, CIECAM02  $ [10] $ , was derived to give accurate prediction of color differences under different viewing conditions. More recently, CAM16-UCS  $ [11] $ , has been proposed to supersede CAM02-UCS  $ [9] $  to overcome some mathematical drawbacks. Both these UCSs give very similar performance in predicting color differences. ZCAM-QMh  $ [12] $  was also developed to include both one- and two-dimensional absolute color appearance attributes, and to fit the earlier published color-difference data, together with new data from high dynamic range conditions and from wide color gamut displays. The four formulae or spaces were used in this study.

According to the CIE [5], color-difference formulae should be restricted to apply to a set of reference viewing conditions, i.e., a pair of samples in direct edge contact, subtending a visual angle larger than  $ 4^{\circ} $  field of view (FoV) against a uniform neutral grey background ( $ L^{*}=50 $ ) illuminated by a D65 simulator at 1000 lx, and the color-difference magnitude should be less than 5 CIELAB  $ \left(\Delta E_{ab}^{*}\right) $  units. Note that the pairs having edge contact means that observers can view a separation line between two samples in a pair. These conditions are usually achieved in industry by using lighting cabinets. However, the viewing conditions in real life could be very different. Hence, CIE also encouraged researchers [13] to investigate parametric effects, i.e., viewing conditions that differ from the above reference conditions. This resulted in the findings of some prominent parametric effects caused by, for example, lightness crispening [14], chromatic crispening [15,16], texture [17], physical size (FoV) [15,16], color-difference magnitude [18,19], separation [19], image [20] and illuminant [21]. The results from Mirjalili et al. [19] revealed that a separation effect occurred in the lightness difference affecting total color-difference. The present study extended their study to include the effects of the in/exclusion of a separation, and various FoVs and color-difference magnitudes.

Another issue that has been raised more recently is in regard to the application of different color matching functions (CMFs). The CIE recommended the use of the CIE 1931 2° and 1964 10° CMFs for FoVs less and greater than 4°, respectively. More recently, CIE 2006 CMFs  $ [22,23] $  have been proposed, as cone fundamentals between 1° and 10° FoV, and observers from 20-80 years old, to take into consideration an individual's lens optical density, macular pigment, and visual pigment. The CIE 2006 2°, 10° and 4° CMFs  $ [22,23] $  have been investigated to compare with the two conventional CMFs, Fig. 1. The present results include visual results from 4 FoVs that can be used to verify the CMFs. Figure 1 shows that differences occur in the peak wavelengths for the  $ \bar{x} $  and  $ \bar{z} $  functions, as well as differences between 450-500 nm for the  $ \bar{y} $  function. The latter range could affect the calculation of colorimetric data, especially for lighting and display products that use blue LED emission in this region.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_1/imgs/img_in_chart_box_392_470_830_830.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A35Z%2F-1%2F%2Fa328b14c3c2c153e3e96cdbc7544cfeee960dd9174447fa9552db73ece2c5bc2" alt="Image" width="35%" /></div>


<div style="text-align: center;">Fig. 1. Different CIE CMFs.</div>


With the above in mind, the present experiment was designed to study three parametric color-difference effects: 1) inclusion or exclusion of a separation line between the two samples in a pair, 2) two color-difference magnitudes (4 and 8 CIELAB units), and 3) 4 fields of view (FoVs)  $ (2^{\circ}, 4^{\circ}, 10^{\circ} $  and  $ 20^{\circ}) $ .

### 2. Experimental

#### 2.1. Display

The experiment was conducted in a darkened room using a 31-inch NEC PA311D liquid crystal display, with a resolution of  $ 4096 \times 2160 $  pixels. The correlated color temperature (CCT) of the display peak white was set to 6500 K with a luminance of  $ 300 \, cd/m^2 $ . The Gain-Offset-Gamma (GOG) model [24] was used to characterize the display. The predictive accuracy of the GOG model gave an average of 0.35 CIEDE2000 ( $ \Delta E_{00} $ ) [25] units over 1120 sample colors in the present experiment, with a standard deviation of  $ 0.20 \, \Delta E_{00} $  units. In addition, sample pairs were measured 5 times during the experimental period, and their associated mean values were used in the analysis. The MCDM (mean color difference from the mean) of the 5 measurements was  $ 0.12 \, \Delta E_{00} $  units, with a standard deviation of  $ 0.05 \, \Delta E_{00} $  units. The above results indicate the display to be accurate and have high stability over time. All the measurements were made using a Konica Minolta CS2000A tele-spectroradiometer. The data were recorded in terms of the spectral power distribution of the samples on the display so that the XYZ tristimulus values could be computed using the different CMFs.

#### 2.2. Stimuli

CIE has encouraged researchers to share the data in the areas of color difference [26]. The five CIE recommended color centers were typical examples to be extensive studied, i.e., grey, red, yellow, green, and blue [27]. Figure 2 shows the CIELAB color specification of each color center under illuminant D65 and the CIE 1964 10° CMFs, together with their  $ L^{*} $  values. Figure 3 shows the distribution of the sample pairs for each center. For each color-difference magnitude (4 or 8 CIELAB units), 14 sample pairs were prepared surrounding each color center, including 1 pair with only a lightness difference, 6 pairs with mixed lightness and chromatic differences and 7 pairs with only chromatic differences, i.e., no lightness differences. Sample colors were distributed uniformly from 0° to 180° in the  $ \Delta a^{*}\Delta b^{*} $  plane, and from 0° to 90° in the  $ \Delta L^{*}\Delta a^{*} $  plane, or the  $ \Delta L^{*}\Delta b^{*} $  plane, respectively. Table 1 lists the viewing parameters for each of the 16 experimental phases (2 magnitudes, 2 separations, 4 FoVs). For each pair of samples, there were two separation conditions, corresponding to with-separation (S) or no-separation (NS). The former was produced by adding a black line one pixel wide across the edge between the two samples, to simulate the direct edge contact of the surface color pairs. Each sample pair had 4 FoVs, set at 2°, 4°, 10°, or 20°. In total, 1,120 sample pairs (14 samples × 5 centers × 2 magnitudes × 2 (S or NS) × 4 FoVs) were studied. In addition, 320 pairs (out of the 1120 pairs) were repeated (2 pairs in the  $ \Delta a^{*}\Delta b^{*} $  plane, 1 pair in the  $ \Delta L^{*}\Delta a^{*} $  plane and 1 pair in the  $ \Delta L^{*}\Delta b^{*} $  plane for each color center). The results from the repeated pairs were used to evaluate intra-observer variation. The visual result of each pair was obtained by averaging the results from 20 observers.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_2/imgs/img_in_chart_box_414_698_813_1095.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A36Z%2F-1%2F%2Fc7ea665648f1e132895041142b35e3404512636d997046b1438f91922bfa0bff" alt="Image" width="32%" /></div>


<div style="text-align: center;">Fig. 2. The 5 CIE color centers under D65 and CIE 1964  $ 10^{\circ} $  CMF condition. The number denotes the  $ L^{*} $  value of each center.</div>


<div style="text-align: center;">Table 1. The viewing parameters studied</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Groups</td><td style='text-align: center;'>ΔEab*</td><td style='text-align: center;'>Separation</td><td style='text-align: center;'>FoVs</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>4</td><td style='text-align: center;'>S</td><td style='text-align: center;'>2°, 4°, 10°, 20°</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>4</td><td style='text-align: center;'>NS</td><td style='text-align: center;'>2°, 4°, 10°, 20°</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>8</td><td style='text-align: center;'>S</td><td style='text-align: center;'>2°, 4°, 10°, 20°</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>8</td><td style='text-align: center;'>NS</td><td style='text-align: center;'>2°, 4°, 10°, 20°</td></tr></table>

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_3/imgs/img_in_chart_box_230_184_673_439.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A37Z%2F-1%2F%2F5e4f74647feb8ded927cbafc72239add6352002b4f5cc75502adbfefdcd275e9" alt="Image" width="36%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_3/imgs/img_in_chart_box_733_183_992_441.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A37Z%2F-1%2F%2F051f60d91ede1266d9614648c6d78ce6b8e774ffda812a8272ccc91bbed17219" alt="Image" width="21%" /></div>


<div style="text-align: center;">Fig. 3. The sample pair distribution in (a)  $ \Delta a^{*}\Delta b^{*} $  and (b)  $ \Delta L^{*}\Delta a^{*} $  (or  $ \Delta b^{*} $ ) planes for color difference magnitudes of 4 and 8 CIELAB units. (For (b), the triangle and dots represent the sample pairs along the  $ \Delta L^{*} $  axis and in the  $ \Delta L^{*}\Delta a^{*} $  or the  $ \Delta L^{*}\Delta b^{*} $  planes, respectively).</div>


#### 2.3. Visual assessment

The grey-scale method [28] was used to assess the color-differences of sample pairs. The grey-scale samples consisted of 9 ISO 105-A02 samples [28] (GS-1 to GS-5 with an interval of 0.5) and one additional sample (GS-0.5). The latter sample was added to extend the color difference range of the grey scale. This was done to avoid visual differences of some sample pairs exceeding that of the grey scale sample pairs. (It was found that pairs having the same  $ \Delta E_{ab}^{*} $  values, some having mixed  $ \Delta L^{*} $  and chromatic differences, appeared to have larger differences than those having only  $ \Delta L^{*} $  or chromatic differences.) The grey-scale pairs were constructed between the standard (GS-5) and each of GS-0.5 to GS-5 samples. The actual grey-scale pairs agreed well with those of the ISO standard, with a mean of  $ 0.1 \Delta E_{ab}^{*} $  units. Equation (1) was used to scale the visual judgments in terms of grey-scale values (GS) to visual color-difference values ( $ \Delta V $ ), and was obtained by minimizing the  $ \Delta E_{ab}^{*} $  between the measured color-differences of the neighboring grey samples and the corresponding grey scale numbers (GS). Figure 4 shows the transformation between grey-scale (GS) and visual difference ( $ \Delta V $ ). Defined by Eq. (1). The predicted color-differences agreed with the actual grey-scale pairs specified by ISO within a mean of  $ 0.2 \Delta E_{ab}^{*} $  units.

 $$ \varDelta V=0.1172GS^{4}-1.7394GS^{3}+9.6987GS^{2}-26.0010GS+31.8068. $$ 

The experiment was divided into 4 parts, according to the values of the FoVs of  $ 2^{\circ} $ ,  $ 4^{\circ} $ ,  $ 10^{\circ} $  and  $ 20^{\circ} $ . Each pair was assessed by 20 observers. Note that 7 observers participated all parts of the experiment; others participated in only parts of the experiment. In total, there were 46 normal color vision observers, including 21 males and 25 females, having an age range from 19 to 30 years with a mean of 24 years and a standard deviation of 2.9 years.

The experiment was carried out in a darkened room. Observers were seated 60 cm in front of the display. After a 1-minute adaptation period viewing only the mid-grey background  $ (L^{*}=50) $ , observers were asked to assess the color-difference of the sample pairs using the grey-scale method. They were encouraged to report their result to one decimal place, e.g., 3.3. Figure 5 shows the experimental situation for the 4 FoVs. Sample pairs were displayed in the center of the screen in a random order. The grey-scale pairs were displayed along the top of the screen from left to right or from right to left alternately. Observers clicked one of grey-scale pairs. The selected grey-scale pair was then displayed to the left or right of the sample pair. The distance between the two pairs was fixed at  $ 2.5^{\circ} $  for all FoVs. Observers were asked to find the grey-scale pair that appeared to have a similar color-difference to that of the sample pair, and then to report the score in terms of the GS value using the scroll bar at the bottom of the screen. The observers

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_4/imgs/img_in_chart_box_410_182_813_517.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A37Z%2F-1%2F%2F6e5536856d22de47bf5a18e2d0f35e094b25492b8b9b1340e5f878ed4761ee91" alt="Image" width="32%" /></div>


<div style="text-align: center;">Fig. 4. The transformation between grey-scale (GS) and visual difference ( $ \Delta V $ ).</div>


could then press the 'Previous' or 'Next' button to redo the previous pair or to move on to the next pair, respectively. Each observer did two sessions, each session including 180 pairs, lasting approximately 60 minutes.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_4/imgs/img_in_image_box_232_701_609_914.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A37Z%2F-1%2F%2F4b6b54beb25e57fae31ed865c298a2bb96174aa057cb1e93ddae7f34b931c158" alt="Image" width="30%" /></div>


<div style="text-align: center;">(a)  $ 2^{\circ} $  S</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_4/imgs/img_in_image_box_613_702_989_916.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A37Z%2F-1%2F%2F4d0c4befe4162bbee9fb1ecfd1faeed429b3a88fe7485480322b518f4911ce2d" alt="Image" width="30%" /></div>


<div style="text-align: center;">(b)  $ 4^{\circ} $  S</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_4/imgs/img_in_image_box_232_933_610_1144.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A37Z%2F-1%2F%2Fe34b756dabf9cc3792d89d66b6657564b954a46281f93b3382de9171cabf032b" alt="Image" width="30%" /></div>


<div style="text-align: center;">(c)  $ 10^{\circ} $  S</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_4/imgs/img_in_image_box_612_933_990_1144.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A37Z%2F-1%2F%2F66a96e48209c01fdbe6c82c8d8f3503173a8d71ec33d5107b072a9a64ff62611" alt="Image" width="30%" /></div>


<div style="text-align: center;">(d)  $ 20^{\circ} $  NS</div>


<div style="text-align: center;">Fig. 5. The experimental interface for (a)  $ 2^{\circ} $ , (b)  $ 4^{\circ} $ , (c)  $ 10^{\circ} $ , and (d)  $ 20^{\circ} $  FoVs. The scrollbar in (a) is enlarged 250% for legibility. Note the scrollbar was the original size for all FoVs in the real experiment.</div>


### 3. Results and discussions

The standard residual sum of squares (STRESS)  $ [29] $  (see Eq. (2)) metric was used to evaluate the disagreement between the two datasets considered.

 $$ STRESS=100\sqrt{\frac{\sum\left(\boldsymbol{F}\Delta\boldsymbol{E}_{i}-\Delta\boldsymbol{V}_{i}\right)^{2}}{\sum\Delta V_{i}^{2}}}, $$ 

where  $ F = \frac{\sum \Delta E_{i} \Delta V_{i}}{\sum \Delta E_{i}^{2}} $ , a scaling factor to adjust the visual color-difference,  $ \Delta V $  and measured color-difference,  $ \Delta E $  to be on the same scale. A STRESS value of zero indicates perfect agreement.

Two types of statistical test were used to test the significant difference between two datasets. The first was ANOVA test (alpha level 0.05), used to reveal parametric effect such as separation, FoV. The second test was F-test (alpha level 0.05) based on STRESS values, to test statistical difference, e.g., between two color models to predict a visual dataset.

#### 3.1. Observer variations

Intra-observer and inter-observer variations were first investigated. Figure 6 shows the interobserver variations of each FoV group, in STRESS units according to five groups (the S, NS,  $ \Delta E_{ab}^{*}=8 $  and  $ \Delta E_{ab}^{*}=4 $  groups and total) together with the intra-observer variation of the total data. In addition, the 95% confidence interval was plotted for each bar. For the inter-observer variation, the STRESS values were 43 (2°), 41 (4°), 42 (10°) and 39 (20°), with an average of 41. Note that typical inter-observer variation for assessing color differences has been found to be in the range about 32-38. For assessing parametric color differences on displays using the grey scale method this can increase to 40-45 as found here  $ [15,30,31] $ .

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_5/imgs/img_in_chart_box_232_783_990_1006.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A38Z%2F-1%2F%2F0e72f9a741d50cbb27ea57712e9e5629e59331b8021136ba0784e56e55b0fd7e" alt="Image" width="61%" /></div>


<div style="text-align: center;">Fig. 6. Inter- and intra-observer variation in STRESS units. Error bar denotes the 95% confidence interval.</div>


Comparing the observer variations between the S and NS groups, it was found that the former had more variation than the latter by approximately 5%. Comparing the large and small  $ \Delta E_{ab}^{*} $  magnitude groups, the visual difference of the  $ 8\ \Delta E_{ab}^{*} $  group was consistently smaller than that of the  $ 4\ \Delta E_{ab}^{*} $  group by approximately 7%. However, there was no significant difference in the above comparisons according to the F-test ( $ F=1.00\sim1.27, F_{C}=0.72, 1/F_{C}=1.40 $ ).

Comparing the four different FoVs, the  $ 2^{\circ} $  and  $ 20^{\circ} $  fields had the worst and best consistency, respectively. This leads to the suggestion that observers performed more consistently as the FoV increases.

The intra-observer variations (320 out of 1120 pairs were repeated by each observer) were 27  $ (2^{\circ}) $ , 23  $ (4^{\circ}) $ , 21  $ (10^{\circ}) $  and 21  $ (20^{\circ}) $  in STRESS units, with an average of 23. The intra-observer variations were thus approximately half the STRESS values for inter-observer variation. According to the F-test, a significant difference was found between  $ 2^{\circ} $  vs  $ 10^{\circ} $  (F = 1.65,  $ F_{C} = 0.64 $ ,  $ 1/F_{C} = 1.56 $ ) and between  $ 2^{\circ} $  vs  $ 20^{\circ} $  (F = 1.65).

#### 3.2. Visual effect

##### 3.2.1. Size effect

The size effect was investigated by calculating between  $ \Delta V $  values between two individual FoVs, and between each FoV and overall mean. Figure 7 shows the scatter plots for the above comparisons.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_6/imgs/img_in_chart_box_229_344_420_531.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A38Z%2F-1%2F%2F67285adf0311a99d3e88ddd6289e8486d68e49407e33dd0ddf209378c67bb9e2" alt="Image" width="15%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_6/imgs/img_in_chart_box_421_343_612_531.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A38Z%2F-1%2F%2F6f83ec23eeeb065087bc08a4f34655f6e02bdb6a05cc5b80fe5c1351397cd834" alt="Image" width="15%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_6/imgs/img_in_chart_box_612_344_804_532.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A39Z%2F-1%2F%2F8e5c476895e44564496e389eb54fee9e3d64687d424642c9dda17ec34ebfdeca" alt="Image" width="15%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_6/imgs/img_in_chart_box_804_344_994_532.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A39Z%2F-1%2F%2F991e7da259d85572d5132ab28b47e74a6bee98d98637656cf724b09ddebac09d" alt="Image" width="15%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_6/imgs/img_in_chart_box_420_544_611_735.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A39Z%2F-1%2F%2F1e995cdcb3a93965e6ea7d793e5047712531507bad033ee3132ccb0564af23f5" alt="Image" width="15%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_6/imgs/img_in_chart_box_611_545_804_736.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A39Z%2F-1%2F%2F681387fb47ba5c3c64767778fd9687abf0696275eee6af7b71c932214e7c88ac" alt="Image" width="15%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_6/imgs/img_in_chart_box_805_546_994_734.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A39Z%2F-1%2F%2Ff94d136db493e998b6a0930847527aabda96b27f1de136c0af76cb286ac404a9" alt="Image" width="15%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_6/imgs/img_in_image_box_271_804_502_866.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A39Z%2F-1%2F%2F90577d8090d8bc4e3b45c4420c34051ce0961f1e59a4fae2d7c1ff5845f47f3c" alt="Image" width="18%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_6/imgs/img_in_chart_box_611_749_803_938.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A39Z%2F-1%2F%2F0abc79fed6aaf3cbc1b3ab27bbb3dd7d465e4f527ec262b1a7a384eeb86145d5" alt="Image" width="15%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_6/imgs/img_in_chart_box_804_749_994_939.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A39Z%2F-1%2F%2Fecba97e9e1b08245967f313e9fc0a3624f6842c786fcb43e2c461cc5b4394ddb" alt="Image" width="15%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_6/imgs/img_in_chart_box_804_953_994_1141.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A39Z%2F-1%2F%2Fa635dafb0ab6da049c12b8788e1b5a137dc13a277ee21efe243344387a93189f" alt="Image" width="15%" /></div>


<div style="text-align: center;">Fig. 7. The scatter diagrams and STRESS values calculated between different FoV phases, and between each phase and the overall mean (diagrams in the last column).</div>


Comparing to the overall mean results, the STRESS values were very similar, 14  $ (2^{\circ}) $ , 10  $ (4^{\circ}) $ , 12  $ (10^{\circ}) $  and 11  $ (20^{\circ}) $ . Comparing each FoV against the others, the mean STRESS values were 21  $ (2^{\circ}) $ , 18  $ (4^{\circ}) $ , 19  $ (10^{\circ}) $  and 19  $ (20^{\circ}) $ , where the  $ 2^{\circ} $  and  $ 4^{\circ} $  FoVs, and the  $ 10^{\circ} $  and  $ 20^{\circ} $  FoVs were close to each other (17 STRESS units). The  $ \Delta V $  values between the  $ 2^{\circ} $  and  $ 10^{\circ} $  FoVs had the largest difference (23 STRESS units). According to the ANOVA test, there was no significant difference between all pairs of the FoVs (F=0.37, p=0.773).

##### 3.2.2. Separation effect

To reveal the separation effect, the visual differences  $ (\Delta V) $  of the sample pairs between the NS and S groups were evaluated in terms of STRESS units. Figure 8 shows the  $ \Delta V $  values between the S and NS groups, where the black and red dots represent sample pairs without or with a lightness difference, respectively. A systematic trend can be seen in that sample pairs with and without lightness differences have larger or smaller visual differences, respectively. This reveals the parametric effect due to separation. When a pair of samples include a lightness difference, with no separation line between the two samples, the visual difference will appear much greater than the equivalent pair with a separation line. Note that all four datasets that include sample pairs with a separation line (BFD [3,4], RIT-DuPont [32], Leeds [6] and Witt [33]) were used to develop advanced color models (CIEDE2000, CAM16-UCS, ZCAM-QMh). More recently, Mirjalili et al. [19], Zhao et al. [30] and Xu et al. [31] investigated color-differences using sample pairs with no separation line. According to the CIE reference conditions, sample pair should have a separation line [5].

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_7/imgs/img_in_chart_box_305_558_605_856.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A40Z%2F-1%2F%2Fa6f231655db5e858269db90186464f6751ffa5725f129d8bf1002c82983f0bb7" alt="Image" width="24%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_7/imgs/img_in_chart_box_618_559_918_855.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A40Z%2F-1%2F%2F598c6d56cc2d56eb2aeca89433cd79b27eb06630a2b21e88163f4aa98d806815" alt="Image" width="24%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_7/imgs/img_in_chart_box_305_864_606_1158.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A40Z%2F-1%2F%2F476b3e19b1d081c6c68cc89534ee1febb37721284813239e9f84039d066b2f17" alt="Image" width="24%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_7/imgs/img_in_chart_box_617_864_919_1158.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A40Z%2F-1%2F%2F1eb1e1c4794ace1e384560616330bc0af3e6e645e211dd6ab2174416fa2bcb80" alt="Image" width="24%" /></div>


<div style="text-align: center;">Fig. 8. Scatter plots of  $ \Delta V $  values between the NS and S groups: (a)  $ 2^{\circ} $ , (b)  $ 4^{\circ} $ , (c)  $ 10^{\circ} $ , (d)  $ 20^{\circ} $ . Red solid, red open, black solid, black open dots denote  $ \Delta E_{ab}^{*}=4 $  including  $ \Delta L^{*} $ ,  $ \Delta E_{ab}^{*}=8 $  including  $ \Delta L^{*} $ ,  $ \Delta E_{ab}^{*}=4 $  excluding  $ \Delta L^{*} $ ,  $ \Delta E_{ab}^{*}=8 $  excluding  $ \Delta L^{*} $  pairs, respectively.</div>


Table 2 lists the STRESS values calculated between  $ \Delta V $  values from the NS and S groups, with pairs including  $ \Delta L^{*} $  (Fig. 3(b)), excluding  $ \Delta L^{*} $  (Fig. 3(a)) and combined respectively. The smallest STRESS values of each set are underlined. Comparing the S and NS groups, the pairs including lightness differences had better agreement than those with excluding lightness differences, and the larger FoV subsets had better agreement than the smaller FoVs subsets. As

can be seen, when combining all the pairs with different FoVs (see Overall set), the disagreement between the S and NS groups further increased.

<div style="text-align: center;">Table 2. The STRESS values of  $ \Delta V $  values calculated between the S and NS groups $ ^{a} $ </div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>S vs NS subsets</td><td style='text-align: center;'>2°</td><td style='text-align: center;'>4°</td><td style='text-align: center;'>10°</td><td style='text-align: center;'>20°</td><td style='text-align: center;'>Mean</td><td style='text-align: center;'>Overall</td></tr><tr><td style='text-align: center;'>Including  $ \Delta L^{*} $  set (70)</td><td style='text-align: center;'>21</td><td style='text-align: center;'>19</td><td style='text-align: center;'>16</td><td style='text-align: center;'>16</td><td style='text-align: center;'>18</td><td style='text-align: center;'>20</td></tr><tr><td style='text-align: center;'>Excluding  $ \Delta L^{*} $  set (70)</td><td style='text-align: center;'>31</td><td style='text-align: center;'>21</td><td style='text-align: center;'>25</td><td style='text-align: center;'>23</td><td style='text-align: center;'>25</td><td style='text-align: center;'>25</td></tr><tr><td style='text-align: center;'>Combined (140)</td><td style='text-align: center;'>36</td><td style='text-align: center;'>32</td><td style='text-align: center;'>29</td><td style='text-align: center;'>26</td><td style='text-align: center;'>31</td><td style='text-align: center;'>32</td></tr></table>

 $ ^{a} $ (The numbers in the brackets represent the number of sample pairs.)

According to ANOVA test, for the combined set, there was significant difference between all pairs for the  $ 2^{\circ} $  and  $ 20^{\circ} $  FoVs (F = 4.04 and 5.09, p = 0.048 and 0.027, respectively). However, for the inclusion and exclusion of  $ \Delta L^{*} $  groups, there was a significant difference between the NS and S groups for all FoVs (F = 7.58, p = 0.007 for the including  $ \Delta L^{*} $  group  $ 20^{\circ} $  FoV.  $ F = 13.98 \sim 56.52 $ , p < 0.001 for the others).

##### 3.2.3. Color-difference magnitude effect

The visual differences  $ (\Delta V) $  of sample pairs having color-differences of  $ 4\;\Delta E_{ab}^{*} $  group were compared with those with  $ 8\;\Delta E_{ab}^{*} $  group. Figure 9 shows a very similar trend for all FoVs, i.e., the visual results of the  $ 8\;\Delta E_{ab}^{*} $  group to be about twice larger than those of the  $ 4\;\Delta E_{ab}^{*} $  group. Sample pairs in the S and NS groups had a similar color-difference magnitude effect. Table 3 shows the differences expressed in STRESS units. These values were quite similar (about 19) for all FoVs and overall results.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_8/imgs/img_in_chart_box_363_798_857_1297.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A40Z%2F-1%2F%2F29686b9221b2ce7e702b50eefc833f1a6d6268c2ca022ef613ede10b0ba6dde2" alt="Image" width="40%" /></div>


<div style="text-align: center;">Fig. 9. A scatter plot between  $ \Delta V $  values of sample pairs that have  $ 4 \Delta E_{ab}^{*} $  units and those that have  $ 8 \Delta E_{ab}^{*} $  units.</div>


<div style="text-align: center;">Table 3. The STRESS values of  $ \Delta V $  values calculated between 4 and 8  $ \Delta E_{ab}^{*} $  groups $ ^{a} $ </div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>$ \Delta E^{*}_{ab} $  4 vs 8 subsets</td><td style='text-align: center;'>2°</td><td style='text-align: center;'>4°</td><td style='text-align: center;'>10°</td><td style='text-align: center;'>20°</td><td style='text-align: center;'>Mean</td><td style='text-align: center;'>Overall</td></tr><tr><td style='text-align: center;'>S set (70)</td><td style='text-align: center;'>19</td><td style='text-align: center;'>19</td><td style='text-align: center;'>21</td><td style='text-align: center;'>21</td><td style='text-align: center;'>20</td><td style='text-align: center;'>20</td></tr><tr><td style='text-align: center;'>NS set (70)</td><td style='text-align: center;'>19</td><td style='text-align: center;'>17</td><td style='text-align: center;'>21</td><td style='text-align: center;'>16</td><td style='text-align: center;'>18</td><td style='text-align: center;'>17</td></tr><tr><td style='text-align: center;'>S + NS (140)</td><td style='text-align: center;'>19</td><td style='text-align: center;'>18</td><td style='text-align: center;'>21</td><td style='text-align: center;'>19</td><td style='text-align: center;'>19</td><td style='text-align: center;'>18</td></tr></table>

<div style="text-align: center;"> $ ^{a} $ (The numbers in the brackets represent the number of pairs.)</div>


##### 3.2.4. Comparing chromatic difference ellipses

Chromatic difference ellipses for the S and NS groups were fitted in CIELAB  $ a^{*}b^{*} $  and CAM16-UCS  $ a^{\prime}b^{\prime} $  planes, respectively. A color-difference ellipse is given in Eq. (3).

 $$ \Delta E=\sqrt{g_{11}\Delta a^{2}+g_{12}\Delta a\Delta b+g_{22}\Delta b^{2}}, $$ 

where coefficients  $ g_{11} $  to  $ g_{22} $  were optimized to give the least STRESS value between color-differences predicted by the ellipse equation  $ (\Delta E) $  and the visual differences  $ (\Delta V) $ . Only 7 excluding  $ \Delta L^{*} $  (chromatic) pairs for each color center were used to fit a chromatic ellipse. The  $ \Delta E $  values from Eq. (3) were fixed to have a visual difference  $ \Delta V $  of 4 or 8 to plot ellipses for the 4 and  $ 8\Delta E_{ab}^{*} $  groups, respectively. Note that  $ \Delta V $  values of 4 and 8 correspond to 9.8 (19.3) and 22.3 (34.8)  $ \Delta E_{ab}^{*} $  units for S (NS) parameters, respectively.

Figure 10 shows the chromatic difference ellipses plotted in CIELAB and CAM16-UCS, respectively. Circles corresponding to  $ \Delta V $  values of 4 and 8 were also plotted. The parameters for CAM16-UCS (adapting luminance  $ L_{a} $ , luminance factor of the neutral background  $ Y_{b} $  and the surround) were 59.0 (using CIE 1964 CMFs), 18.4 and 'dim', respectively. Note that the stimuli sampled surrounding a circle in CIELAB space could be slightly distorted in CAM16-UCS space. However, the ellipses were fitted to the visual results in CAM16-UCS space, and not fitted using the data transformed from those in CIELAB ellipses. Thus, the ellipses should be a true representation in CAM16-UCS.

Some patterns in the ellipses can be summarized as below:

• The ellipses can be divided into 2 distinct groups according to the ellipse size: those that represent small magnitudes ( $ \Delta E_{ab}^{*}=4 $ ) and those that represent large magnitudes ( $ \Delta E_{ab}^{*}=8 $ ). For the NS group, the effect becomes less distinct.

• The NS group ellipses have larger sizes than the S group ellipses due to the excluding  $ \Delta L^{*} $  (chromatic) pairs having smaller visual differences for the NS pairs than those for the S pairs (as mentioned in section 3.2.2, also see Fig. 8).

• For the S group, different FoVs ellipses had similar shapes and orientations. For the NS ellipses,  $ 2^{\circ} $  FoV ellipse was in general more elongated (longer and thinner) than the others in the Grey, Red and Yellow color centers.

From Fig. 10, all the NS ellipses are larger than the S ellipses by a factor of approximately 1.90. Also, all CAM16-UCS ellipses are closer to the constant-sized circle than the CIELAB ellipses. This indicates that the CIELAB space is less uniform than the CAM16-UCS space. This was further verified by using measures of the global and local uniformity as calculated by Eqs. (4) and (5) [31] respectively, where A and B are semi-major and semi-minor axes, and S is the area ( $ \pi AB $ ) respectively. A smaller Local and Global values indicate a more uniform color space. The results showed that CAM16-UCS performed better than CIELAB, by 1.9 and 1.3.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_304_184_920_269.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A42Z%2F-1%2F%2F2d8c2b2dae4c3b6dce50de373be735e10a8077c56e69969335c5fadac9914428" alt="Image" width="50%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_306_269_449_433.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A42Z%2F-1%2F%2Fff1d51105cd69afb4d582800ffcaa8bfff3e6c9b8a7dc9fda95bf6ab701b98cd" alt="Image" width="11%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_457_271_602_434.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A42Z%2F-1%2F%2F838f0b2ff4dd55420149274f513395ff8a9677e3f83de8a53a8f974e83bed42b" alt="Image" width="11%" /></div>


<div style="text-align: center;">CIELAB Red-NS</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_611_285_757_430.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A42Z%2F-1%2F%2F3bc25b57c22909775680d769b37be46d4a37c15e94ab190d0cdc42149db1a70d" alt="Image" width="11%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_763_275_913_431.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A42Z%2F-1%2F%2F907100567c7fc2f12f6afa2976bbfee8b5f5874f967d1643cd24afda134065b4" alt="Image" width="12%" /></div>


<div style="text-align: center;">CAM16-UCS Red-S</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_305_436_448_709.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A42Z%2F-1%2F%2Fe22c3258b29fa47b27b7ff5ae80607623cb0ad32c17be91420bf8d520d20a9b2" alt="Image" width="11%" /></div>


<div style="text-align: center;">CAM16-UCS Red-NS</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_458_438_602_710.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A42Z%2F-1%2F%2Fccc8b200a26709322f4bc1ac9c5acebbad5f7ca2d8b973aa89a74ca595c57e4b" alt="Image" width="11%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_612_454_755_707.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A42Z%2F-1%2F%2Fb481e6bf6124817cf3884f9ead3e2d2666c8f9ead88c5b0b6fe435d02217caeb" alt="Image" width="11%" /></div>


<div style="text-align: center;">CAM16-UCS Yellow-S</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_764_437_916_707.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A42Z%2F-1%2F%2F546c73491768b5c3a5ddbd39bd9f96cef8274161b472c142cecdb22be45ee549" alt="Image" width="12%" /></div>


<div style="text-align: center;">CAM16-UCS Yellow-NS</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_305_710_450_919.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A42Z%2F-1%2F%2F3631519dce4b165d88462b5d1ec11eeca2f019aee5145f46c5ac77b062fec36e" alt="Image" width="11%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_456_713_605_919.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A42Z%2F-1%2F%2F926a193ae3399a6f9820fde3b336c615f09f65c89f4108c592d575f28b8fc5f3" alt="Image" width="12%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_614_728_758_914.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A42Z%2F-1%2F%2F2f9a21ee09cf07e3823106e526ded0f45e53fb417be64dc448cc1187e29ffd61" alt="Image" width="11%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_767_725_918_915.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A42Z%2F-1%2F%2F5c65f0fb0cf723ac59eda6a09b1a9afcd000d0240707783982ac03f998b9e15c" alt="Image" width="12%" /></div>


<div style="text-align: center;">CAM16-UCS Green-S</div>


<div style="text-align: center;">CAM16-UCS Green-NS</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_chart_box_306_921_448_1106.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A43Z%2F-1%2F%2F657ee5519a269e40441efdb389b5c0144d5a23807203896e207d6ad323035574" alt="Image" width="11%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_chart_box_456_923_603_1107.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A43Z%2F-1%2F%2F0af7cd65ab6e2fe27fbc83752c4e6dfda7389dbca304178c9937dc13d8948d51" alt="Image" width="12%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_chart_box_611_940_757_1103.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A43Z%2F-1%2F%2F93f587e62859526acd1b1271fc5f6d8824a212f9e2eabc6f242f5c3b7d5449a0" alt="Image" width="11%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_306_1108_449_1267.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A43Z%2F-1%2F%2Fa641b3e0f44cc350775b6f0fd48f1e85f13782c2bf9c01a4ade674210db0893a" alt="Image" width="11%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_764_936_919_1104.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A43Z%2F-1%2F%2F11deb377fdcabf69b6292476aacc860ec449a3104735d0a9474bb8ab515aa390" alt="Image" width="12%" /></div>


<div style="text-align: center;">CAM16-UCS Blue-S</div>


<div style="text-align: center;">a</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_chart_box_458_1122_601_1269.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A43Z%2F-1%2F%2F82dea730d50ae2d351cbbafc2da82191890851082a91beb7d912ba66b517bb2b" alt="Image" width="11%" /></div>


<div style="text-align: center;">a</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_chart_box_611_1123_756_1272.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A43Z%2F-1%2F%2F5f315e71446d90f3b416a4975aea69028d1f91f4a2601ad0476c5f6de8bcedc1" alt="Image" width="11%" /></div>


<div style="text-align: center;">CAM16-UCS Blue-NS</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_10/imgs/img_in_image_box_763_1124_909_1269.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A43Z%2F-1%2F%2F03a71caed13b20ec07d8471e4804f89ec81a1f9e9b8e20a251ded4153b200221" alt="Image" width="11%" /></div>


<div style="text-align: center;">a'</div>


<div style="text-align: center;">Fig. 10. Chromatic difference ellipses from the left to right: CIELAB S, CIELAB NS, CAM16-UCS S, and CAM16-UCS NS, and from top to bottom: the CIE color centers of grey, red, yellow, green, and blue, respectively. For each center, there are 4 FoV ellipses for  $ \Delta V $  values of 4 and 8, respectively. The thick red and blue circles in each space represent the constant sizes corresponding to  $ \Delta V $  values of 4 and 8, respectively.</div>


times for local uniformity and global uniformity respectively.

 $$ Local=\sqrt{\frac{1}{N}\sum_{i=1}^{N}\left(\frac{A_{i}}{B_{i}}-1\right)^{2}}\times100\%, $$ 

 $$ Global=\frac{\sqrt{\frac{1}{N}\sum_{i=1}^{N}\left(S_{i}-\bar{S}\right)^{2}}}{\bar{S}}\times100\%. $$ 

The F test was also conducted, i.e., the F value is considered to be significant when outside the range of  $ F_{C}=0.53, 1/F_{C}=1.89 $ . The results showed that for local uniformity, the S ellipses are significantly closer to circle than NS ellipses (F=2.10 and 3.61 for CIELAB and CAM16-UCS respectively). For global uniformity, the S ellipses were closer to the constant size than NS ellipses (F=2.08 and 2.00 for CIELAB and CAM16-UCS respectively). The differences of local and global uniformity between 4 and 8  $ \Delta E_{ab}^{*} $  groups are statistically insignificant (F=1.16, 1.17, 0.99 and 0.89 for CIELAB local, CAM16-UCS local, CIELAB global and CAM16-UCS global uniformity respectively).

Overall, CAM16-UCS performed significantly better in both local uniformity (F=3.46,  $ F_{C}=0.64 $ ,  $ 1/F_{C}=1.56 $ ) and global uniformity (F=1.79) than CIELAB.

Figure 11 is taken from Merjialili et al.'s paper  $ [19] $ . It shows a great similarity for each CIE center between 5 datasets: their own, Witt  $ [34] $ , Cheung and Rigg  $ [35] $ , RIT-DuPont  $ [32] $  and Cui and Luo's LMG0N  $ [15] $ . It can be seen in Fig. 11, the ellipses from all datasets had good agreement in terms of ellipse shape and orientation, but not in size. Very similar pattern as Fig. 11 can be found for all ellipses in Fig. 10 in CIELAB space.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_11/imgs/img_in_image_box_347_772_873_1290.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A44Z%2F-1%2F%2F318049358af9beee353526d03c10dadeccd8911898df00c3fbba24416b7c7c15" alt="Image" width="42%" /></div>


<div style="text-align: center;">Fig. 11. Comparing the ellipses obtained from various studies. (The figure comes from [19].)</div>


### 4. Comparing the performances of metrics formed by CMFs and color models

As noted earlier, 5 CMFs (CIE 1931  $ 2^{\circ} $ , CIE 1964  $ 10^{\circ} $ , CIE 2006  $ 2^{\circ} $ , CIE 2006  $ 10^{\circ} $ , CIE 2006  $ 4^{\circ} $ ) and 4 color models (CIELAB, CIEDE2000, CAM16-UCS and ZCAM-QMh) were investigated in this study. Note that a mean age of 24 years was used as a parameter to obtain the CIE 2006  $ 4^{\circ} $  CMFs. The name 'metric' is used here to represent a combination of CMFs and color model. The data were used to test the performance of each metric in terms of STRESS values. The results should reveal which CMFs and which model gave the best performance.

The testing follows the CIE specification to use  $ 2^{\circ} $  and  $ 10^{\circ} $  CMFs for the FoVs larger and smaller than  $ 4^{\circ} $ , respectively. For  $ 4^{\circ} $  FoV data, all 5 CMFs were tested. Table 4 lists the testing results of each metric. For each FoV, the best color models and the best CMFs are in bold and underlined, respectively. The results are summarized below:

• All metrics consistently performed better for the larger FoV ( $ 10^{\circ} $  and  $ 20^{\circ} $ ) than for the smaller FoV ( $ 2^{\circ} $  and  $ 4^{\circ} $ ) data.

• For each color model, the CMFs compared gave almost exactly the same performance regardless of color model. Also, there was no significant difference between CMFs according to the F-test  $ (F=0.86\sim1.17, F_{C}=0.79, 1/F_{C}=1.27) $ . Comparing the STRESS values, ZCAM-QMh outperformed CAM16-UCS and CIEDE2000, and CIELAB the worst. Only CIELAB performed significantly worse than the other models according to the F-test  $ (F=1.81\sim3.31, F_{C}=0.79, 1/F_{C}=1.27) $ .

<div style="text-align: center;">Table 4. Comparison of the performance of different color models using different CMFs in STRESS units.</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>CMFs (FoV data)</td><td style='text-align: center;'>CIELAB</td><td style='text-align: center;'>CIEDE2000</td><td style='text-align: center;'>CAM16-UCS</td><td style='text-align: center;'>ZCAM-QMh</td></tr><tr><td style='text-align: center;'>CIE 1931 (2°)</td><td style='text-align: center;'>48</td><td style='text-align: center;'>34</td><td style='text-align: center;'>35</td><td style='text-align: center;'>29</td></tr><tr><td style='text-align: center;'>CIE 2006-2° (2°)</td><td style='text-align: center;'>48</td><td style='text-align: center;'>34</td><td style='text-align: center;'>35</td><td style='text-align: center;'>30</td></tr><tr><td style='text-align: center;'>CIE 1931 (4°)</td><td style='text-align: center;'>48</td><td style='text-align: center;'>31</td><td style='text-align: center;'>33</td><td style='text-align: center;'>28</td></tr><tr><td style='text-align: center;'>CIE 1964 (4°)</td><td style='text-align: center;'>47</td><td style='text-align: center;'>30</td><td style='text-align: center;'>32</td><td style='text-align: center;'>29</td></tr><tr><td style='text-align: center;'>CIE 2006-2° (4°)</td><td style='text-align: center;'>48</td><td style='text-align: center;'>31</td><td style='text-align: center;'>33</td><td style='text-align: center;'>29</td></tr><tr><td style='text-align: center;'>CIE 2006-10° (4°)</td><td style='text-align: center;'>47</td><td style='text-align: center;'>30</td><td style='text-align: center;'>32</td><td style='text-align: center;'>28</td></tr><tr><td style='text-align: center;'>CIE 2006-4° (4°)</td><td style='text-align: center;'>48</td><td style='text-align: center;'>32</td><td style='text-align: center;'>33</td><td style='text-align: center;'>29</td></tr><tr><td style='text-align: center;'>CIE 1964 (10°)</td><td style='text-align: center;'>41</td><td style='text-align: center;'>25</td><td style='text-align: center;'>25</td><td style='text-align: center;'>29</td></tr><tr><td style='text-align: center;'>CIE 2006-10° (10°)</td><td style='text-align: center;'>41</td><td style='text-align: center;'>25</td><td style='text-align: center;'>25</td><td style='text-align: center;'>28</td></tr><tr><td style='text-align: center;'>CIE 1964 (20°)</td><td style='text-align: center;'>39</td><td style='text-align: center;'>25</td><td style='text-align: center;'>25</td><td style='text-align: center;'>23</td></tr><tr><td style='text-align: center;'>CIE 2006-10° (20°)</td><td style='text-align: center;'>39</td><td style='text-align: center;'>25</td><td style='text-align: center;'>24</td><td style='text-align: center;'>22</td></tr></table>

 $ ^{a} $ The best performance of color model is in bold.

### 5. Modelling the parametric color-difference formulae for sample pairs to have no-separation line

It is well known that more advanced recent color models that include color-difference equations and uniform color spaces were derived using surface colors with a separation line between pairs of samples. So, it is to be expected that the models should perform better with separation conditions than no-separation conditions. As found by Mirjalili et al.  $ [19] $ , their sample pairs, with no separation between the two samples in a pair, had a parametric effect due to the embedded lightness-difference in the total color-difference. As shown in Fig. 8, the NS group of sample pairs with a lightness difference had larger perceived color differences than the S group pairs with

a lightness difference, but for those chromatic pairs (without lightness difference), the results showed otherwise. Therefore, the typical color models performed worse for no-separation pairs than separation pairs. Efforts were made to reveal the parametric effect for the NS data and this is described below.

Equation (6) shows a generic color-difference formula.

 $$ \varDelta E_{0}=\sqrt{\left(\varDelta L\right)^{2}+\left(\varDelta C\right)^{2}+\left(\varDelta H\right)^{2}+R T}, $$ 

where RT is the rotation term and is set to zero except for CIEDE2000.

From Section 3.2.2, for no-separation sample pairs having the same color-difference in CIELAB units, the no-separation pairs having lightness differences should have larger predicted differences than those with chromatic differences. This agrees with the finding of Mirjalili et al. [19] who proposed a color-difference formula  $ \left(\Delta E_{1}\right) $  given in Eq. (7) by including a lightness weighting function  $ (D_{L}) $  to predict lightness difference.

 $$ \varDelta E_{1}=\sqrt{\left(\frac{\varDelta L}{D_{L}}\right)^{2}+(\varDelta C)^{2}+(\varDelta H)^{2}+R T}, $$ 

where  $ D_{L}=a\cdot\Delta E+b $ ; the a and b coefficients were obtained from the Mirjalili et al. dataset, and  $ \Delta E $  was calculated from the original equation, e.g., CIELAB. The function indicates both  $ D_{L} $  and  $ \Delta E_{0} $  values to have a positive correlation, and implies that for a larger color-difference, the separation line will show more clearly, and would lead to a smaller lightness difference compared with the chromatic difference. It was found that a values of 0.047, 0.079, 0.072, 0.065; and b values of 0.22, 0.27, 0.27, 0.61 for CIELAB, CIEDE2000, CAM16-UCS and ZCAM-QMh, respectively.

The Mirjalili et al.  $ D_{L} $  factor was derived using surface colors. Taking media into account, a media scaling factor (surface and self-luminous colors),  $ s_{M} $ , was introduced to form Eq. (8), to adjust the lightness difference for display colors.

 $$ \varDelta E_{2}=\sqrt{\left(\frac{\varDelta L}{D_{L}.s_{M}}\right)^{2}+\left(\varDelta C\right)^{2}+\left(\varDelta H\right)^{2}+R T}, $$ 

where a value around 0.5 was found to be appropriate for the factor  $ s_{M} $  for the self-luminous colors, i.e., values of 0.41, 0.66, 0.65, 0.47 were calculated for CIELAB, CIEDE2000, CAM16-UCS and ZCAM-QMh, respectively [31]. The factor  $ s_{M} $  was fixed at 0.5 for all models in the present work. Note that for surface colors, the  $ s_{M} $  value is set to one for all color models. This result shows strong evidence that there is a media effect.

Finally, a parametric factor to be introduced to account for the physical size (FoV) effect,  $ s_{S} $  (see Eq. (9)) to adjust the lightness difference for different FoVs.

 $$ \varDelta E_{3}=\sqrt{\left(\frac{\varDelta L}{D_{L}.s_{M}\varDelta s_{S}}\right)^{2}+\left(\varDelta C\right)^{2}+\left(\varDelta H\right)^{2}+R T}, $$ 

where factor  $ s_{S} $  was first optimized for individual physical sizes, and was then fitted to a function of FoV as given in Eq. (10).

 $$ \mathrm{s}_{S}=a\cdot e^{b\cdot F o V}+c, $$ 

where parameters a, b and c were optimized for each color model. These parameters are given in Table 5. Figure 12 shows the FoV scaling factor  $ s_{S} $  plotted as a function of FoV.

To compare the performance of the parametric formulae in predicting the visual results, the STRESS values were calculated and the F-test was applied to show the improvement between

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_14/imgs/img_in_chart_box_380_184_843_661.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A45Z%2F-1%2F%2Fecbc38b44155a6056cad014d860e80eadc43dc2175318eb54b709f3b6c614563" alt="Image" width="37%" /></div>


<div style="text-align: center;">Fig. 12. The FoV scaling factor  $ s_{S} $  plotted as a function of FoV.</div>


<div style="text-align: center;">Table 5. The parameters of the FoV scaling factor  $ s_{S} $  in Eq. (10)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>a</td><td style='text-align: center;'>b</td><td style='text-align: center;'>c</td></tr><tr><td style='text-align: center;'>CIELAB</td><td style='text-align: center;'>-0.95</td><td style='text-align: center;'>0.26</td><td style='text-align: center;'>1.60</td></tr><tr><td style='text-align: center;'>CIEDE2000</td><td style='text-align: center;'>-0.99</td><td style='text-align: center;'>0.29</td><td style='text-align: center;'>1.69</td></tr><tr><td style='text-align: center;'>CAM16-UCS</td><td style='text-align: center;'>-1.06</td><td style='text-align: center;'>0.28</td><td style='text-align: center;'>1.79</td></tr><tr><td style='text-align: center;'>ZCAM-QMH</td><td style='text-align: center;'>-0.89</td><td style='text-align: center;'>0.28</td><td style='text-align: center;'>1.53</td></tr></table>

different stages for each formula  $ (F_{C}=0.79, 1/F_{C}=1.27) $ . Table 6 lists the performance of the original  $ (\Delta E_{0}) $ ,  $ \Delta E_{1} $ ,  $ \Delta E_{2} $  and  $ \Delta E_{3} $  formulae in terms of STRESS values. From the table above, some conclusions can be drawn below:

• All the improved formulae from each color model performed better than their original formula.

• All models predicted the results of larger FoV ( $ 10^{\circ} $  and  $ 20^{\circ} $ ) more accurately than those of smaller FoV pairs ( $ 2^{\circ} $  and  $ 4^{\circ} $ ).

• Comparing  $ \Delta E_{0} $  and  $ \Delta E_{1} $  for all models, the lightness-difference parametric factor  $ D_{L} $  gave noticeable improvements except ZCAM-QMh. According to the F-test, all models showed significant improvements for all FoVs and the combined data ( $ F = 1.46 \sim 2.25 $ ) except ZCAM-QMh.

• The  $ \Delta E_{2} $  formulae including the  $ s_{M} $  parametric factor was found only slight improvement on  $ \Delta E_{1} $  formulae for all color models in terms of STRESS values. According to F-test, these differences between  $ \Delta E_{1} $  and  $ \Delta E_{2} $  formulae are significant only for  $ 2^{\circ} $  (all models) and  $ 4^{\circ} $  (ZCAM-QMh) ( $ F = 1.44 \sim 2.19 $ ).

• Including the factor  $ s_{S} $ , led to  $ \Delta E_{3} $  formula giving smaller STRESS values over the  $ \Delta E_{2} $  formula. This indicates the performance of all models consistently improved. There were significant improvements for  $ 10^{\circ} $  (CIEDE2000, CAM16-UCS and ZCAM-QMh) and  $ 20^{\circ} $  (CIEDE2000, CAM16-UCS and ZCAM-QMh) according to the F-test ( $ F = 1.36 \sim 1.88 $ ).

• For CIELAB, CIEDE2000 and CAM16-UCS, the  $ \Delta E_{3} $  formula outperformed  $ \Delta E_{0} $  significantly from the F-test ( $ F = 2.19 \sim 2.56 $ ), except for the ZCAM-QMh model, which only gave a small improvement (F = 1.19). When predicting color-difference using the  $ \Delta E_{3} $  formula, CIEDE2000 and ZCAM-QMh performed the best, followed by CAM16-UCS, with CIELAB the worst.

• Note that the  $ \Delta E_{3} $  formula for the NS group gave similar STRESS value to that of the  $ \Delta E_{0} $  formula for the S group. Considering the combined dataset, CIEDE2000 performed the best, followed by CAM16-UCS and ZCAM-QMh, with CIELAB the worst.

<div style="text-align: center;">Table 6. The performance of the new color models in terms of STRESS units for each FoV (CIE 1931 CMFs for 2° FoV and CIE 1964 CMFs for the other FoVs).$^{a}$</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="6">CIELAB</td><td style='text-align: center;'>FoV</td><td style='text-align: center;'>$ \Delta E_{0} $</td><td style='text-align: center;'>$ \Delta E_{1} $</td><td style='text-align: center;'>$ \Delta E_{2} $</td><td style='text-align: center;'>$ \Delta E_{3} $</td></tr><tr><td style='text-align: center;'>2°</td><td style='text-align: center;'>53</td><td style='text-align: center;'>37</td><td style='text-align: center;'>29</td><td style='text-align: center;'>29</td></tr><tr><td style='text-align: center;'>4°</td><td style='text-align: center;'>50</td><td style='text-align: center;'>35</td><td style='text-align: center;'>32</td><td style='text-align: center;'>31</td></tr><tr><td style='text-align: center;'>10°</td><td style='text-align: center;'>44</td><td style='text-align: center;'>33</td><td style='text-align: center;'>36</td><td style='text-align: center;'>33</td></tr><tr><td style='text-align: center;'>20°</td><td style='text-align: center;'>44</td><td style='text-align: center;'>30</td><td style='text-align: center;'>31</td><td style='text-align: center;'>28</td></tr><tr><td style='text-align: center;'>mean</td><td style='text-align: center;'>48</td><td style='text-align: center;'>34</td><td style='text-align: center;'>32</td><td style='text-align: center;'>30</td></tr><tr><td rowspan="5">CIEDE2000</td><td style='text-align: center;'>2°</td><td style='text-align: center;'>42</td><td style='text-align: center;'>32</td><td style='text-align: center;'>24</td><td style='text-align: center;'>24</td></tr><tr><td style='text-align: center;'>4°</td><td style='text-align: center;'>37</td><td style='text-align: center;'>28</td><td style='text-align: center;'>26</td><td style='text-align: center;'>23</td></tr><tr><td style='text-align: center;'>10°</td><td style='text-align: center;'>29</td><td style='text-align: center;'>22</td><td style='text-align: center;'>30</td><td style='text-align: center;'>22</td></tr><tr><td style='text-align: center;'>20°</td><td style='text-align: center;'>31</td><td style='text-align: center;'>21</td><td style='text-align: center;'>25</td><td style='text-align: center;'>19</td></tr><tr><td style='text-align: center;'>mean</td><td style='text-align: center;'>35</td><td style='text-align: center;'>26</td><td style='text-align: center;'>26</td><td style='text-align: center;'>22</td></tr><tr><td rowspan="5">CAM16-UCS</td><td style='text-align: center;'>2°</td><td style='text-align: center;'>41</td><td style='text-align: center;'>31</td><td style='text-align: center;'>25</td><td style='text-align: center;'>24</td></tr><tr><td style='text-align: center;'>4°</td><td style='text-align: center;'>37</td><td style='text-align: center;'>28</td><td style='text-align: center;'>28</td><td style='text-align: center;'>25</td></tr><tr><td style='text-align: center;'>10°</td><td style='text-align: center;'>29</td><td style='text-align: center;'>24</td><td style='text-align: center;'>32</td><td style='text-align: center;'>24</td></tr><tr><td style='text-align: center;'>20°</td><td style='text-align: center;'>30</td><td style='text-align: center;'>20</td><td style='text-align: center;'>26</td><td style='text-align: center;'>19</td></tr><tr><td style='text-align: center;'>mean</td><td style='text-align: center;'>34</td><td style='text-align: center;'>26</td><td style='text-align: center;'>28</td><td style='text-align: center;'>23</td></tr><tr><td rowspan="5">ZCAM-QMh</td><td style='text-align: center;'>2°</td><td style='text-align: center;'>28</td><td style='text-align: center;'>34</td><td style='text-align: center;'>23</td><td style='text-align: center;'>23</td></tr><tr><td style='text-align: center;'>4°</td><td style='text-align: center;'>26</td><td style='text-align: center;'>30</td><td style='text-align: center;'>25</td><td style='text-align: center;'>24</td></tr><tr><td style='text-align: center;'>10°</td><td style='text-align: center;'>23</td><td style='text-align: center;'>25</td><td style='text-align: center;'>28</td><td style='text-align: center;'>23</td></tr><tr><td style='text-align: center;'>20°</td><td style='text-align: center;'>20</td><td style='text-align: center;'>22</td><td style='text-align: center;'>21</td><td style='text-align: center;'>18</td></tr><tr><td style='text-align: center;'>mean</td><td style='text-align: center;'>24</td><td style='text-align: center;'>28</td><td style='text-align: center;'>24</td><td style='text-align: center;'>22</td></tr></table>

 $ ^{a} $ The best performing FoV data for each parametric formula is in bold, and the best performing formula for each FoV data is underlined.

Figures 13(a) and 13(b) show the performance of the parametric formula for each color model, and for the individual FoV subsets of CIEDE2000, respectively. CIEDE2000 is the present ISO/CIE standard, and is used here to represent the typical effect for all models. The results in Fig. 13 support the conclusion in Table 4. Comparing different models in Fig. 13(a), all models

outperformed CIELAB and in general  $ \Delta E_{3} $  performed the best, followed by  $ \Delta E_{2} $ ,  $ E_{1} $ , and the  $ \Delta E_{0} $  the worst. In Fig. 13(b), the larger the FoVs, CIEDE2000 performed the better.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_16/imgs/img_in_chart_box_230_254_582_484.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A46Z%2F-1%2F%2Fb90e5bd9e558394ddbbf9a5594a1a3131a5df944dbd54db7b0e83de5546b6543" alt="Image" width="28%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f82a5b3-283b-46d4-a4f3-9aca47461e55/markdown_16/imgs/img_in_chart_box_640_255_991_484.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-30T04%3A23%3A46Z%2F-1%2F%2F5f4e8bc393cdc6c6df8946dec5a79353743fb707862fc1697ef4adc3630706e8" alt="Image" width="28%" /></div>


<div style="text-align: center;">Fig. 13. The performance of the parametric formula (a) for different color models and (b) for individual FoVs using CIEDE2000.</div>


### 6. Conclusion

An experiment was conducted using display colors to investigate parametric color-difference effects, including separation, color-difference magnitude and field of view. The results revealed various parametric effects.

Different CMFs were tested to calculate color-differences using the visual results for different fields-of-view. The results showed that there was little difference between the data calculated using the different CMFs. A parametric formula was successfully developed to predict three parametric effects, the field-of-view, the media (surface or self-luminous colors) and the color-difference magnitude, for sample pairs that to have no-separation line.

Funding. National Natural Science Foundation of China (61775190).

Disclosures. The authors declare no conflicts of interest.

Data availability. Data underlying the results presented in this paper are not publicly available at this time but may be obtained from the authors upon reasonable request.

## References

1. CIE 015: 2018, "Colourimetry," (CIE, Vienna, 2018).

2. F. Clarke, “Modification to the JPC79 color-difference formula,” J.soc.dyers Colourists 100(1984).

3. M. R. Luo and B. Rigg, “BFD (l:c) colour-difference formula Part 1-Development of the formula,” J. Soc. Dyers Colour. 103(2), 86–94 (1987).

4. M. R. Luo and B. Rigg, “BFD (l:c) colour-difference formula Part 2-Performance of the formula,” J. Soc. Dyers Colour. 103(3), 126–132 (1987).

5. CIE, “Industrial Colour-Difference Evaluation,” (1995).

6. D. H. Kim and J. H. Nobbs, “New weighting functions for the weighted CIELAB colour difference formula,” in Proceedings of the AIC, 1997, 446–449.

7. M. R. Luo, G. Cui, and B. Rigg, “The development of the CIE 2000 colour-difference formula: CIEDE2000,” Color Res. Appl. 26(5), 340–350 (2001).

8. CIE, "Improvement to Industrial Colour Difference Equation," (2001).

9. M. R. Luo, G. Cui, and C. Li, "Uniform colour spaces based on CIECAM02 colour appearance model," Color Res. Appl. 31(4), 320–330 (2006).

10. CIE 159: 2004, "A colour appearance model for colour management systems: CIECAM02," (CIE, Vienna, 2004).

11. C. Li, Z. Li, Z. Wang, Y. Xu, M. R. Luo, G. Cui, M. Melgosa, M. H. Brill, and M. Pointer, “Comprehensive color solutions: CAM16, CAT16, and CAM16-UCS,” Color Res Appl 42(6), 703–718 (2017).

12. M. Safdar, J. Y. Hardeberg, and M. Ronnier Luo, “ZCAM, a colour appearance model based on a high dynamic range uniform colour space,” Opt. Express 29(4), 6036–6052 (2021).

13. CIE 101-1993, "Parametric effects in colour-difference evaluation," (1993).

14. K. M. R. Ho, G. Cui, M. R. Luo, and B. Rigg, "A Lightness Difference Formula for Predicting Crispening Effects," in The Tenth Color Imaging Conference: Color Science and Engineering Systems, Technologies, Applications, CIC 2002, November 12, 2002, Scottsdale, Arizona, USA, 2002).

15. G. H. Cui, M. R. Luo, B. Rigg, and W. Li, "Colour-difference evaluation using CRT colours. Part I: Data gathering and testing colour difference formulae," Color Res. Appl. 26(5), 394–402 (2001).

16. G. Cui, M. R. Luo, B. Rigg, and W. Li, “Colour-difference evaluation using CRT colours. Part II: Parametric effects,” Color Res. Appl. 26(5), 403–412 (2001).

17. R. Huertas, M. Melgosa, and E. Hita, “Influence of random-dot textures on perception of suprathreshold color differences,” J. Opt. Soc. Am. A 23(9), 2067–2076 (2006).

18. H. Wang, G. Cui, M. R. Luo, and H. Xu, “Evaluation of colour-difference formulae for different colour-difference magnitudes,” Color Res. Appl. 37(5), 316–325 (2012).

19. F. Mirjalili, M. R. Luo, G. Cui, and J. Morovic, “Color-difference formula for evaluating color pairs with no separation:  $ \Delta E $  NS,” J. Opt. Soc. Am. A 36(5), 789–799 (2019).

20. CIE 199:2011, “Methods for evaluating colour differences in images,” (Commission Internationale de l’E ‘clairage, Vienna, Austria, 2011).

21. M. R. Luo and B. Rigg, “A colour-difference formula for surface colours under illuminant A,” J. Soc. Dyers Colour. 103, 161–167 (1987).

22. CIE 170-1:2006, “Fundamental chromaticity diagram with physiological axes - Part 1,” (Commission Internationale de l’E’clairage, Vienna, Austria, 2006).

23. CIE 170-2:2015, “Fundamental Chromaticity Diagram with Physiological Axes – Part 2: Spectral Luminous Efficiency Functions and Chromaticity Diagrams,” (CIE, 2016).

24. R. S. Berns, “Methods for characterizing CRT displays,” Displays 16(4), 173–182 (1996).

25. ISO/CIE, “Colorimetry – Part 6: CIEDE2000 colour-difference formula,” in ISO/CIE 11664-6:2014(E) (ISO/CIE, 2014), (2014), pp. 11664–11666.

26. M. Melgosa, "Request for existing experimental datasets on color differences," Color Res. Appl. 32(2), 159 (2007).

27. A. Robertson, “CIE guidelines for coordinated research on color-difference evaluation,” Color Res Appl 3, 33–39 (1978).

28. 105-A02, “Textiles - Tests for colour fastness - Part A02: Grey scale for assessing change in colour,” (ISO, Geneva, 1993).

29. CIE 217:2016, “Recommended Method for Evaluating the Performance of Colour-Difference Formulae,” (2016).

30. B. Zhao, Q. Xu, and M. R. Luo, “Color difference evaluation for wide-color-gamut displays,” J. Opt. Soc. Am. A 37(8), 1257–1265 (2020).

31. Q. Xu, B. Zhao, G. Cui, and M. R. Luo, “Testing uniform colour spaces using colour differences of wide colour gamut,” Opt. Express 29(5), 7778 (2021).

32. R. S. Berns, D. H. Alman, L. Reniff, G. D. Snyder, and M. R. Balonon-Rosen, “Visual determination of suprathreshold color-difference tolerances using probit analysis,” Color Res. Appl. 16(5), 297–316 (1991).

33. K. Witt, “Geometric relations between scales of small colour differences,” Color Res. Appl. 24(2), 78–92 (1999).

34. K. Witt, “Parametric effects on surface color-difference evaluation at threshold,” Color Res. Appl. 15(4), 189–199 (1990).

35. M. Cheung and B. Rigg, “Colour-difference ellipsoids for five CIE colour centres,” Color Res. Appl. 11(3), 185–195 (1986).

