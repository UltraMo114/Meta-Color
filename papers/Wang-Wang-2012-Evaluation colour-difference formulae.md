# Evaluation of Colour-Difference Formulae for Different Colour-Difference Magnitudes

Han Wang, $ ^{1,2} $  Guihua Cui, $ ^{1} $  M. Ronnier Luo, $ ^{1*} $  Haisong Xu $ ^{2} $ 

 $ ^{1} $ Colour, Imaging and Design Research Centre, University of Leeds, Leeds LS2 9JT, United Kingdom

 $ ^{2} $ State Key Laboratory of Modern Optical Instrumentation, Department of Optical Engineering, Zhejiang University, Hangzhou 310027, China

Received 3 August 2009; revised 9 January 2011; accepted 13 January 2011

Abstract: Most of the colour-difference formulae were developed to fit data sets having a limited range of colour-difference magnitudes. Hence, their performances are uncertain when applying them to a range of colour differences from very small to very large colour differences. This article describes an experiment including three parts according to the colour-difference magnitudes: large colour difference (LCD), small colour difference (SCD), and threshold colour difference (TCD) corresponding to mean  $ \Delta E_{ab}^{*} $  values of 50.3, 3.5, and 0.6, respectively. Three visual assessment techniques were used: ratio judgement, pair comparison, and threshold for LCD, SCD, and TCD experiments, respectively. Three data sets were used to test six colour-difference formulae and uniform colour spaces (CIELAB, CIE94, CIEDE2000, CAM02-SCD, CAM02-UCS, and CAM02-LCD). The results showed that all formulae predicted visual results with great accuracy except CIELAB. CIEDE2000 worked effectively for the full range of colour differences, i.e., it performed the best for the TCD and SCD data and reasonably well for the LCD data. The three CIECAM02-based colour spaces gave quite satisfactory performance. © 2011 Wiley Periodicals, Inc. Col Res Appl, 37, 316–325, 2012; Published online 2 August 2011 in Wiley Online Library (wileyonlinelibrary.com). DOI 10.1002/col.20693

Key words: uniform colour space; colour-difference formula; colour-difference magnitude; pair comparison; ratio judgement; threshold method

## I NTRODUCTION

Colour-difference formulae are widely used to evaluate the colour difference between two samples. The ideal colour-difference formula is a single number pass/fail formula, i.e., a single colour-difference value to determine pass or fail for the shade of a product.

Most modern colour-difference formulae, such as CIE94 $ ^{1} $  and CIEDE2000, $ ^{2} $  were developed to fit visual assessment data sets of small colour difference typically under five CIELAB colour difference  $ (\Delta E_{\mathrm{ab}}^{*}) $  units. $ ^{3} $  However, in practice, a large range of colour differences are encountered in many application areas. For example, when estimating colour difference between an original image and its reproduction, the colour differences could cover a large range. Luo et al. $ ^{4} $  found that colour-difference formulae performed significantly different when applied to estimate large and small colour differences. Hence, they extended the CIE recommended colour appearance model, CIECAM02, $ ^{5} $  to form three new uniform colour spaces, CAM02-SCD, CAM02-LCD, and CAM02-UCS, for estimating small-, large-, and overall ranges of colour differences respectively.

Guan and Luo $ ^{6} $  conducted a visual experiment using sample pairs with large colour difference of around  $ 12\Delta E_{ab}^{*} $ . They developed a colour-difference formula, GLAB, for evaluating large colour differences. Hence, it is not clear which formula should be used according to different magnitudes in industrial applications. Or, there is a need to use hybrid system to deal with different colour difference ranges.

With this in mind, CIE Technical Committee (1–63) Validity of the Range of CIEDE2000 was established to investigate the application of the CIEDE2000 equation. $ ^{7} $  The question to be answered is whether the equations developed to fit small size colour difference can perform within a range of colour differences, from threshold up to

<div style="text-align: center;">TABLE I. Experimental conditions for the three data sets studied.</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Data set</td><td style='text-align: center;'>No. of pairs</td><td style='text-align: center;'>Psychophysical method</td><td style='text-align: center;'>No. of observers</td><td style='text-align: center;'>No. of observations</td><td style='text-align: center;'>No. of assessments</td><td style='text-align: center;'>Max.  $ \Delta E^{*}_{ab} $</td><td style='text-align: center;'>Min.  $ \Delta E^{*}_{ab} $</td><td style='text-align: center;'>Mean  $ \Delta E^{*}_{ab} $</td></tr><tr><td style='text-align: center;'>LCD</td><td style='text-align: center;'>60</td><td style='text-align: center;'>Ratio judgment</td><td style='text-align: center;'>18</td><td style='text-align: center;'>23</td><td style='text-align: center;'>1380</td><td style='text-align: center;'>107.8</td><td style='text-align: center;'>22.4</td><td style='text-align: center;'>50.3</td></tr><tr><td style='text-align: center;'>SCD</td><td style='text-align: center;'>10</td><td style='text-align: center;'>Pair comparison</td><td style='text-align: center;'>22</td><td style='text-align: center;'>27</td><td style='text-align: center;'>1215</td><td style='text-align: center;'>6.8</td><td style='text-align: center;'>2.1</td><td style='text-align: center;'>3.5</td></tr><tr><td style='text-align: center;'>TCD</td><td style='text-align: center;'>100</td><td style='text-align: center;'>Threshold</td><td style='text-align: center;'>21</td><td style='text-align: center;'>26</td><td style='text-align: center;'>2600</td><td style='text-align: center;'>1.4</td><td style='text-align: center;'>0.2</td><td style='text-align: center;'>0.6</td></tr></table>

 $ \Delta E_{ab}^{*} $  greater than 5. In addition, most of the advanced colour-difference formulae were developed based on the modification of CIELAB. They do not have an associated colour space, and the equations are being more complicated. Hence, CIE TC (1–55) Uniform colour space for industrial colour difference evaluation was established. The data gathered from the present work directly contribute to the above two TCs.

In this study, visual assessment experiments were specially designed for investigating threshold, small and large colour differences. The STRESS (Standardized Residual Sum of Squares) $ ^{8} $  measure and  $ F-test^{8} $  were used to evaluate the performance of the six colour-difference formulae tested, including the three CIE formulae, CIELAB, CIE94, and CIEDE2000, and the three CIECAM02-based uniform colour spaces, CAM02-SCD, CAM02-LCD, and CAM02-UCS. The results reveal the effective range of these formulae.

## EXPERIMENTAL

In this study, colour-difference pairs covering a larger range of magnitudes were prepared. Psychophysical experiments were designed for evaluating threshold, small, and large colour differences (named TCD, SCD, and LCD respectively hereafter) using physical printed or paint samples. Table I summarizes the experimental conditions for the three data sets studied.

It can be seen in Table I that the “large,” “small,” and “threshold” colour differences refer to the mean  $ \Delta E_{ab}^{*} $  values of 50.3, 3.5, and 0.6, respectively. These definitions of colour-difference maganitudes are not well defined, i.e., some consider a  $ \Delta E_{ab}^{*} $  less than five as small colour difference.

Each sample was measured using a GretagMacbeth CE7000A spectrophotometer with an exclusion of specular. The measured reflectance data were converted to XYZ tristimulus values under CIE D65 illuminant and 1931 Standard Colorimetric Observer for LCD data, and CIE 1964 Standard Colorimetric Observer for SCD and TCD data according to different sizes of the samples used. Each sample pair was assessed in a GretagMacbeth SpectraLight II viewing cabinet. The light booth had a light grey background with an  $ L^{*} $  of about 70 and was equipped with a filtered tungsten source having a luminance value of 350 cd/ $ m^{2} $  and a colour temperature of 6455 K. The source is a very high quality daylight simulator, i.e., having a CIE colour rendering index $ ^{9} $  of 97 and CIE metamerism index of A in the visual range. $ ^{10} $  The illumination/viewing geometry was  $ 0^{\circ}/45^{\circ} $  at a viewing distance about 60 cm.

Eighteen to 22 normal colour vision observers, the students and staff members at the University of Leeds, participated in the experiment according to the Ishihara Vision Test, within which five randomly selected observers assessed each pair twice for studying the intra-observer variation. Although five observers with two repeats are somewhat limited to reveal the degree of repeatability, it provides some information on observer precision.

The details of the sample distributions and visual experiments are given in the following sections.

## Large Colour Difference (LCD)

Sixty sample pairs were chosen from the printed samples used in the Kittelmann's study. $ ^{[11]} $  The samples were printed on a glossy paper with a gloss unit of about 55 units measured by a Sheen tri-micro Glossmeter at  $ 60^{\circ}/60^{\circ} $  geometry.

The original samples were printed in a paper as colour patches. Each patch was mounted onto a white card having a size of 1.5 by 1.5 cm square. Figures 1(a) and 1(b) show the distributions of all pairs in CIELAB  $ a^{*}b^{*} $  and  $ L^{*}C_{ab}^{*} $  planes, respectively. Each vector in Fig. 1 stands for a sample pair. It can be seen that the 60 pairs gave a good coverage of different directions in CIELAB space. The colour differences of these sixty sample pairs were ranged from 22.4 to 107.8  $ \Delta E_{ab}^{*} $  units with a mean of 50.3.

Ratio judgement method $ ^{12} $  as illustrated in Fig. 2 was used in the LCD experiment. The reference pair including a white patch  $ (L^{*}=94.00, a^{*}=0.31, b^{*}=0.13) $  and a grey patch  $ (L^{*}=40.64, a^{*}=0.33, b^{*}=-0.50) $  had a colour difference of  $ 53.39\ \Delta E_{ab}^{*} $  that is close to the mean colour difference of all LCD sample pairs. The sample pair in Fig. 2 was one of the 60 chosen pairs. The pairs were presented to observers following a random order in the visual experiment. Before each session, the following instruction was read to each observer.

“The colour difference of the reference pair is one unit. Please estimate the colour difference of the sample pair against that of the reference pair using a ratio (fractions or times). Can you give the number to one decimal point, e.g., 3.2.

For example, if the colour difference of the sample pair is the same as that of the reference pair, the answer is ‘1.0’; if the colour difference of the sample pair is twice as that of the reference pair, your answer is ‘2.0’; if the colour difference of the sample pair is half of that of the reference pair, you should give ‘0.5’.”

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//686f9b6d-3039-4488-b4cc-146f4d2a2155/markdown_2/imgs/img_in_image_box_233_108_601_496.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-03T10%3A44%3A53Z%2F-1%2F%2F637db58b690d5414abeb220f63c683ce8293b74275645b89031de1ba7df0353e" alt="Image" width="30%" /></div>


<div style="text-align: center;">(a)  $ a^{*}b^{*} $  plane</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//686f9b6d-3039-4488-b4cc-146f4d2a2155/markdown_2/imgs/img_in_chart_box_629_169_986_500.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-03T10%3A44%3A53Z%2F-1%2F%2Fdb793e2fa18d0704eeb85ca9762cf620053d16b1625988c40fc2f3d391c2febc" alt="Image" width="29%" /></div>


<div style="text-align: center;">(b)  $ L^{*}C_{ab}^{*} $  plane</div>


<div style="text-align: center;">FIG. 1. Distribution of LCD sample pairs in CIELAB (a)  $ a^{*}b^{*} $  plane and on (b)  $ L^{*}C_{ab}^{*} $  plane.</div>


Coats et al. $ ^{12} $  reported that observers tend to scale the ratio close to one when employ the ratio method. Hence, the raw results in ratio unit  $ (R_{R}) $  were adjusted to have the similar range and magnitude to a colour-difference formula using Eq. (1).

 $$ R_{M}=aR_{R}^{b} $$ 

where  $ R_{M} $  is the ratio between the CIEDE2000 colour differences  $ (\Delta E_{00}) $  of a tested pair and the reference pair; a is set to 42.67 correspond to the reference pair in  $ \Delta E_{00} $  units; b is a power factor obtained by linear fitting of the  $ \ln(R_{M}) $  and  $ \ln(R_{R}) $  using the least square method. Finally the raw visual data were transformed to visual colour differences  $ (\Delta V) $  using Eq. (2).

 $$ \Delta V=42.67R_{R}^{1.1322} $$ 

Note that although the range and magnitudes of the data were adjusted using Eq. (2), based on CIEDE2000 formula, the relative magnitudes between pairs are kept regardless the colour-difference formula used.

## Small Colour Difference (SCD)

Ten drawdown paint pairs having gloss unit of about 90 measured using 60°/60° geometry were specially pre-

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//686f9b6d-3039-4488-b4cc-146f4d2a2155/markdown_2/imgs/img_in_image_box_149_1263_556_1439.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-03T10%3A44%3A53Z%2F-1%2F%2F51eb02ccea0b7db7efbcee3ccc51695152ae1b0c46f0778a09f6fbdbd2b1267c" alt="Image" width="33%" /></div>


<div style="text-align: center;">FIG. 2. Ratio judgement method (Left: Reference pair; Right: Sample pair).</div>


pared by DuPont having a size of 4.5 by 9 cm². This set was designed to demonstrate the differences between CIE-LAB and CIEDE2000 formulae, for which each pair gives similar  $ \Delta E_{00} $  values but very different  $ \Delta E_{ab}^{*} $  values as shown in Table II. It can be seen that most of the pairs had about 3.0  $ \Delta E_{00} $  units, but varied in a large range from 2.1 to 6.8  $ \Delta E_{ab}^{*} $  units. These samples are plotted in Figs. 3(a) and 3(b) for CIELAB  $ a^{*}b^{*} $  and  $ L^{*}C_{ab}^{*} $  planes, respectively.

Pair comparison method was used for scaling each colour-difference pair in the SCD experiment. Ten sample pairs made a total of  $ 45\ (=10\ \times\ 9/2) $  pair combinations for visual assessment. The 45 combinations were shown to each observer according to a random order. Observers were asked to select which pair had larger colour difference in the two pairs presented. The visual results were transformed to z-score according to Thurstone's Law of Comparative Judgements. $ ^{13} $  It is transformed via a series of matrices from the raw data represented by a frequency matrix, followed by proportional matrix, then z-score matrix, for which the average z-score was used to represent the visual results in an interval scale for each pair. Finally, an arbitrary off-set was added to the averaged z-scores to make all values to be positive.

## Threshold Colour Difference (TCD)

In the TCD experiment, the paint samples surrounding 10 colour centers were prepared by the drawdown method with a gloss unit at about 3 measured using  $ 60^{\circ}/60^{\circ} $  geometry. These samples were prepared in a previous study $ ^{[14]} $  including about 30 samples surrounding each of the 10 colour centers investigated. Each sample had a size of 7.5 by 12.7 cm square. Figures 4(a) and 4(b) show the distribution of the 10 colour centers in CIELAB  $ a^{*}b^{*} $  and  $ L^{*}C_{ab}^{*} $  planes, respectively.

<div style="text-align: center;">TABLE II. Colorimetric coordinates and colour differences of SCD sample pairs.</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">No.</td><td colspan="3">Sample A</td><td colspan="3">Sample B</td><td colspan="2">Colour difference</td></tr><tr><td style='text-align: center;'>L*</td><td style='text-align: center;'>a*</td><td style='text-align: center;'>b*</td><td style='text-align: center;'>L*</td><td style='text-align: center;'>a*</td><td style='text-align: center;'>b*</td><td style='text-align: center;'>CIELAB</td><td style='text-align: center;'>CIEDE2000</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>54.94</td><td style='text-align: center;'>-0.19</td><td style='text-align: center;'>0.66</td><td style='text-align: center;'>52.42</td><td style='text-align: center;'>-0.15</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>2.4</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>83.02</td><td style='text-align: center;'>-0.61</td><td style='text-align: center;'>1.22</td><td style='text-align: center;'>79.05</td><td style='text-align: center;'>-0.36</td><td style='text-align: center;'>0.98</td><td style='text-align: center;'>4.0</td><td style='text-align: center;'>2.8</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>42.60</td><td style='text-align: center;'>-0.04</td><td style='text-align: center;'>0.41</td><td style='text-align: center;'>40.05</td><td style='text-align: center;'>-0.06</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>2.6</td><td style='text-align: center;'>2.3</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>43.49</td><td style='text-align: center;'>26.46</td><td style='text-align: center;'>13.92</td><td style='text-align: center;'>43.58</td><td style='text-align: center;'>32.62</td><td style='text-align: center;'>16.82</td><td style='text-align: center;'>6.8</td><td style='text-align: center;'>2.8</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>52.91</td><td style='text-align: center;'>5.36</td><td style='text-align: center;'>-16.58</td><td style='text-align: center;'>53.35</td><td style='text-align: center;'>2.94</td><td style='text-align: center;'>-17.54</td><td style='text-align: center;'>2.6</td><td style='text-align: center;'>3.1</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>54.40</td><td style='text-align: center;'>-8.24</td><td style='text-align: center;'>-14.32</td><td style='text-align: center;'>54.67</td><td style='text-align: center;'>-5.78</td><td style='text-align: center;'>-16.25</td><td style='text-align: center;'>3.1</td><td style='text-align: center;'>2.8</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>38.51</td><td style='text-align: center;'>-0.15</td><td style='text-align: center;'>-25.93</td><td style='text-align: center;'>38.62</td><td style='text-align: center;'>3.98</td><td style='text-align: center;'>-28.86</td><td style='text-align: center;'>5.1</td><td style='text-align: center;'>2.6</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>38.04</td><td style='text-align: center;'>2.73</td><td style='text-align: center;'>-26.67</td><td style='text-align: center;'>38.17</td><td style='text-align: center;'>0.68</td><td style='text-align: center;'>-28.55</td><td style='text-align: center;'>2.8</td><td style='text-align: center;'>2.5</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>53.39</td><td style='text-align: center;'>-1.56</td><td style='text-align: center;'>1.78</td><td style='text-align: center;'>53.40</td><td style='text-align: center;'>-1.54</td><td style='text-align: center;'>4.67</td><td style='text-align: center;'>2.9</td><td style='text-align: center;'>2.5</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>53.90</td><td style='text-align: center;'>-1.32</td><td style='text-align: center;'>-2.02</td><td style='text-align: center;'>54.03</td><td style='text-align: center;'>-3.37</td><td style='text-align: center;'>-2.17</td><td style='text-align: center;'>2.1</td><td style='text-align: center;'>2.7</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>Max.</td><td style='text-align: center;'>6.8</td><td style='text-align: center;'>3.1</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>Min.</td><td style='text-align: center;'>2.1</td><td style='text-align: center;'>2.3</td></tr></table>

For each colour center, 10 pairs were chosen to give a good coverage of most directions and more attentions were paid to the pairs that have colour difference caused by either mainly lightness change, chroma change or hue change. Figures 5(a) and 5(b) show the distributions of 100 pairs in CIELAB  $ \Delta a^{*}\Delta b^{*} $  and  $ \Delta L^{*}\Delta C_{ab}^{*} $  planes respectively. In Fig. 5, different colour vectors correspond to different colour centers. Colour differences of these sample pairs were ranged from 0.20 to 1.36  $ \Delta E_{ab}^{*} $  units with a mean value of 0.55.

Threshold method was used in the TCD visual experiment. Each chosen pair was placed in the cabinet with a hairline gap according to a random order and each observer was asked to determine whether s/he can perceive colour difference between the two samples in a pair.

The raw visual data were in the form of perceptible percentage, i.e., the number of observations of which the colour difference is noticeable divided by the total num-

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//686f9b6d-3039-4488-b4cc-146f4d2a2155/markdown_3/imgs/img_in_image_box_268_997_624_1417.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-03T10%3A44%3A54Z%2F-1%2F%2F944b0d20e9142ab56c85e2cbaa6a7e2164d9be36484ac043aae96f84f333b98c" alt="Image" width="29%" /></div>


## RESULTS AND DISCUSSION

<div style="text-align: center;">(a)  $ a^{*}b^{*} $  plane</div>


ber of observations. These were then transformed to z-score values as an interval scale assuming a normal distribution. Finally the visual colour difference ( $ \Delta V $ ) values were adjusted linearly to have the same scale as CIEDE2000 colour-difference formula. Note that again CIEDE2000 was chosen to adjust the visual scale. Regardless which formula is used, only the average magnitudes are changed but the relative magnitudes between pairs in the data are preserved.

## Measure of Fit

Two measures are mainly used to measure the agreement or disagreement between two sets of data. The first one is STRESS $ ^{8} $  as given in Eq. (3).

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//686f9b6d-3039-4488-b4cc-146f4d2a2155/markdown_3/imgs/img_in_chart_box_640_910_956_1412.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-03T10%3A44%3A54Z%2F-1%2F%2F26c3af2e16fcbd53161770d8c4eb5f09e31ee9466fbac6a474130c9b7910e7bf" alt="Image" width="25%" /></div>


<div style="text-align: center;">(b)  $ L^{*}C_{ab}^{*} $  plane</div>


<div style="text-align: center;">FIG. 3. Distribution of the SCD sample pairs in CIELAB (a)  $ a^{*}b^{*} $  plane and (b)  $ L^{*}C_{ab}^{*} $  planes.</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//686f9b6d-3039-4488-b4cc-146f4d2a2155/markdown_4/imgs/img_in_chart_box_258_112_601_582.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-03T10%3A44%3A55Z%2F-1%2F%2F893f4ce75aefb1d8f679143ea61fc14b3f5fddffb9e03e7e1fdb695729cba55c" alt="Image" width="28%" /></div>


<div style="text-align: center;">(a)  $ a^{*}b^{*} $  plane</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//686f9b6d-3039-4488-b4cc-146f4d2a2155/markdown_4/imgs/img_in_chart_box_619_108_962_586.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-03T10%3A44%3A55Z%2F-1%2F%2Fec09a150f0e6b9ddb38fa7997037e5d21e579184da31cfdb308c05102e438e2f" alt="Image" width="28%" /></div>


<div style="text-align: center;">(b)  $ L^{*}C_{ab}^{*} $  plane</div>


<div style="text-align: center;">FIG. 4. Plot of the 10 TCD colour centres in CIELAB (a)  $ a^{*}b^{*} $  plane and (b)  $ L^{*}C_{ab}^{*} $  plane.</div>


 $$ \begin{aligned}STRESS&=\sqrt{\frac{\sum\left(X_{i}-fY_{i}\right)^{2}}{\sum X_{i}^{2}}\times100\%}\\ where\quad f&=\frac{\sum X_{i}Y_{i}}{\sum Y_{i}^{2}}\end{aligned} $$ 

where  $ X_{i} $  and  $ Y_{i} $  represent the two sets of data whose agreement will be tested. STRESS is given as a percentage in the range from 0 to 100%, of which 0 means perfect agreement and 100 the poorest. The higher STRESS value implies the poorer agreement.

Although STRESS can be considered as the percentage error between two sets of data, it cannot indicate the degree of statistical significance. The  $ F\ test^{4,8} $  is also employed here. The testing hypothesis is described below, for which  $ V_{M} $  given in Eq. (4) was calculated.

1. Define the null and alternate hypotheses (two-tailed)

 $ H_{0} $ :  $ V_{A} = V_{B} $  (e.g. two formulae A and B without significant difference)

 $ H_{A}: V_{A} \neq V_{B} $  (e.g. two formulae A and B with signifi- cant difference)

2. Calculate the F value as  $ F = V_{A}/V_{B} $  where

 $$ V_{M}=\sum_{i=1}^{N}\left(\Delta V_{i}-a_{M}\Delta E_{Mi}\right)^{2}/(N-1)\quad M\in\{A,B\} $$ 

or

 $$ F=\frac{V_{A}}{V_{B}}=\frac{\sum\left(\Delta V_{i}-a_{A}\Delta E_{Ai}\right)^{2}}{\sum\left(\Delta V_{i}-a_{B}\Delta E_{Bi}\right)^{2}}=\frac{STRESS_{A}^{2}}{STRESS_{B}^{2}} $$ 

3. Reject the hypothesis  $ (H_{0}) $  when  $ F < F_{C} $  or if  $ F > 1/F_{C} $  where  $ F_{C} = F(df_{A}, df_{B}, 0.975) $  is the lower critical value of two-tailed F distribution with 95% confidence level and  $ df_{A} $  and  $ df_{B} $  are the degrees of freedom,  $ F_{C} $  can be found from statistical textbooks or calculated using Microsoft Excel function FINV;  $ V_{A} $  and  $ V_{B} $  represent the residual error variances after scaling correction for Models A and B, respectively. The  $ a_{M} $  is calculated using f in Eq. (3) which is the slope between the visual results  $ \Delta V $  and the  $ \Delta E $  for Models A and B, respectively. Finally, N is the number of samples in the data set, and  $ df_{A} = df_{B} = N - 1 $  in this study. The results can be divided into five categories as shown below:

• Model A is significantly better than model B when $F < F_{C}$

• Model A is significantly worse than model B when  $ F > 1/F_{C} $ 

• Model A is insignificantly better than model B when  $ F_{C} \leq F < 1 $ 

• Model A is insignificantly worse than model B when  $ 1 < F \leq 1/F_{C} $ 

• Model A is equal to model B when F = 1.

## Observer Performances

Because of the three different scaling methods used, different measures were used to indicate the observer performances in terms of inter- and intra-observer variations. For LCD visual experiment, to investigate the interobserver variation, the  $ X_{i} $  and  $ Y_{i} $  in Eq. (3) represent one observer's and mean  $ \Delta V $  results, respectively. For studying the intra-observer variation for the five observers who repeated their experiment, the  $ X_{i} $  and  $ Y_{i} $  represent an

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//686f9b6d-3039-4488-b4cc-146f4d2a2155/markdown_5/imgs/img_in_image_box_200_106_1020_608.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-03T10%3A44%3A55Z%2F-1%2F%2F6d448102156b29a84ec63a05f41801c7c70c97d012ebe1f525606f676b98886b" alt="Image" width="66%" /></div>


 $$ \varDelta L^{*}\varDelta C_{a b}^{*} $$ 

<div style="text-align: center;">FIG. 5. Distributions of the TCD samples pairs in CIELAB (a)  $ \Delta a^{*}\Delta b^{*} $  plane and (b)  $ \Delta L^{*}\Delta C_{ab}^{*} $  planes.</div>


individual observer’s two repeated results. The observer variations in the LCD experiment are summarized in Table III.

It can be seen that inter- and intra-observer variability were about 37 and 42 STRESS values, respectively. These were similar to those found by Luo et al. $ ^{4} $  and somewhat smaller than those found from the experiments involving small colour differences. Furthermore, the mean standard deviation for all observers in each pair was also calculated. The mean value of 35.9 for all pairs was obtained. This corresponds to a standard error of about 7.5, i.e.,  $ 35.9/\sqrt{23} $  (for 23 observations).

For the SCD and TCD experiments, two methods were used to evaluate observer variability: WD% (Wrong Decision) $ ^{14} $  and Montag's method. $ ^{15} $  Wrong Decision method was first used to evaluate the observer variation. For examining intra-observer agreement, it is considered as a wrong decision for the sample pair if the two repeated judgements from an observer are disagreed with each other. For interobserver variation, the panel decision stands for the majority decision from all observations, and a wrong decision of an individual observer's decision is different from the panel decision. For example, the visual result of the threshold difference is 40%, i.e., 40% of the observers can detect the difference. The panel decision is then “above threshold,” because the other 60% (majority) of the observers cannot.

<div style="text-align: center;">TABLE III. Observer variation in the LCD data set.</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>Intra-variation</td><td style='text-align: center;'>Inter-variation</td></tr><tr><td style='text-align: center;'>Mean (STRESS)</td><td style='text-align: center;'>42.5</td><td style='text-align: center;'>37.0</td></tr><tr><td style='text-align: center;'>Minimum (STRESS)</td><td style='text-align: center;'>28.9</td><td style='text-align: center;'>26.1</td></tr><tr><td style='text-align: center;'>Maximum (STRESS)</td><td style='text-align: center;'>62.2</td><td style='text-align: center;'>56.9</td></tr><tr><td style='text-align: center;'>Standard Deviation</td><td style='text-align: center;'>12.4</td><td style='text-align: center;'>9.2</td></tr></table>

see the difference. Hence, if an observer reports “can see the difference” on the pair, it is counted as a wrong decision. WD% is the percentage of wrong decisions for all the sample pairs. Table IV lists the observer variations for the SCD and TCD visual experiments.

It can be seen from Table IV that overall inter- and intra-agreement results are quite similar. Typically, there is about 22% disagreement between each observer's two repeated assessments and 25% between each observer and the panel results.

Montag $ ^{15} $  developed an empirical formula to estimate the inter-observer variation for the pair comparison method based on Thurstone's law. It was found a standard deviation of 0.08 with a standard error of about 1.5% for the SCD experiment.

## Model Performance

Three CIELAB based colour-difference formulae were tested here: CIELAB, CIE94 and CIEDE2000. As mentioned earlier, the latter is currently recommended by the CIE for evaluating small colour differences less than 5 and was developed by fitting the four recommended databases, $ ^{16} $  RIT-DuPont, BFD, Witt and Leeds, which are

<div style="text-align: center;">TABLE IV. Observer variation in the SCD and TCD data sets.</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>Intra-variation</td><td style='text-align: center;'>Inter-variation</td></tr><tr><td rowspan="2">SCD</td><td style='text-align: center;'>Mean (WD%)</td><td style='text-align: center;'>23</td><td style='text-align: center;'>25</td></tr><tr><td style='text-align: center;'>Minimum (WD%)</td><td style='text-align: center;'>9</td><td style='text-align: center;'>7</td></tr><tr><td rowspan="4">TCD</td><td style='text-align: center;'>Maximum (WD%)</td><td style='text-align: center;'>38</td><td style='text-align: center;'>49</td></tr><tr><td style='text-align: center;'>Mean (WD%)</td><td style='text-align: center;'>35</td><td style='text-align: center;'>34</td></tr><tr><td style='text-align: center;'>Minimum (WD%)</td><td style='text-align: center;'>22</td><td style='text-align: center;'>18</td></tr><tr><td style='text-align: center;'>Maximum (WD%)</td><td style='text-align: center;'>49</td><td style='text-align: center;'>54</td></tr></table>

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//686f9b6d-3039-4488-b4cc-146f4d2a2155/markdown_6/imgs/img_in_chart_box_124_102_1093_758.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-03T10%3A44%3A56Z%2F-1%2F%2F8cf93db37ff6aa633426d80e1c200222e5adbb1c6d25a962b9861756c51420dc" alt="Image" width="79%" /></div>


<div style="text-align: center;">FIG. 6. The  $ \Delta V $  results plotted against  $ \Delta E $  values predicted from the six original colour-difference formulae for the LCD data.</div>


all small-size differences. The other three uniform colour spaces tested were the extension of the CIECAM02:CAM02-SCD, CAM02-LCD, and CAM02-UCS. (CIECAM02 is the CIE recommended colour appearance model which is widely used for colour management systems to achieve cross-media colour reproduction.) CAM02-SCD was developed by fitting the above four CIE recommended databases. $ ^{16} $ 

CAM02-LCD was developed to fit six datasets based on large sizes with an average of  $ 10 \Delta E_{ab}^{*} $ . CAM02-UCS was developed by fitting all the available data including large and small sizes.

## Large Colour Difference (LCD)

Figure 6 shows the plot of visual colour differences against measured colour differences from six original formulae, for which  $ k_{L} $ ,  $ k_{C} $ , and  $ k_{H} $  were set to one for the three CIE recommended formulae, and  $ k_{L} $  values of 1.24, 1.00, and 0.77 for CAM02-SCD, CAM02-UCS, and CAM02-LCD, respectively, as recommended in Ref. 4. In each plane, two best fitted lines are plotted, one to go through origin and the other to include an intercept. In addition, the best fitted equations are also given.

It can be seen from Fig. 6 that CIELAB performed poorest among all the formulae investigated as the points had the largest scatter; and CAM02-LCD had the smallest scatter. It also reveals that the intercept ranged from 10 to 20 for all formulae. The intercepts did not close to zero point because the ratio scaling method produces interval scale results without a true zero point.

In succession, all formulae were tested with their original form and the optimized  $ k_{L} $  form which gave the smallest STRESS values between calculated colour differences and visual colour differences. The results are given in Table V. Furthermore, the F-test described early was also

<div style="text-align: center;">TABLE V. Performance of the six formulae with original and optimized  $ k_{L} $  for LCD.</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Formula</td><td style='text-align: center;'>CIELAB</td><td style='text-align: center;'>CIE94</td><td style='text-align: center;'>CIEDE2000</td><td style='text-align: center;'>CAM02-SCD</td><td style='text-align: center;'>CAM02-UCS</td><td style='text-align: center;'>CAM02-LCD</td></tr><tr><td style='text-align: center;'>Original</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>STRESS</td><td style='text-align: center;'>21.4</td><td style='text-align: center;'>20.7</td><td style='text-align: center;'>21.1</td><td style='text-align: center;'>15.2</td><td style='text-align: center;'>14.5</td><td style='text-align: center;'>13.2</td></tr><tr><td style='text-align: center;'>Optimized  $ k_{L} $</td><td style='text-align: center;'>0.61</td><td style='text-align: center;'>0.86</td><td style='text-align: center;'>1.06</td><td style='text-align: center;'>0.97</td><td style='text-align: center;'>1.04</td><td style='text-align: center;'>1.01</td></tr><tr><td style='text-align: center;'>STRESS</td><td style='text-align: center;'>17.6</td><td style='text-align: center;'>20.2</td><td style='text-align: center;'>21.1</td><td style='text-align: center;'>15.2</td><td style='text-align: center;'>14.4</td><td style='text-align: center;'>13.2</td></tr><tr><td style='text-align: center;'>Fc = 0.60</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>F value</td><td style='text-align: center;'>0.67</td><td style='text-align: center;'>0.96</td><td style='text-align: center;'>0.99</td><td style='text-align: center;'>1.00</td><td style='text-align: center;'>0.99</td><td style='text-align: center;'>1.00</td></tr></table>

<div style="text-align: center;">TABLE VI. F-test of the six original colour-difference formulae for LCD (Fc: F critical value).</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Fc = 0.60</td><td colspan="6">1/Fc = 1.67</td></tr><tr><td style='text-align: center;'>F value</td><td style='text-align: center;'>CIELAB</td><td style='text-align: center;'>CIE94</td><td style='text-align: center;'>CIEDE2000</td><td style='text-align: center;'>CAM02-SCD</td><td style='text-align: center;'>CAM02-UCS</td><td style='text-align: center;'>CAM02-LCD</td></tr><tr><td style='text-align: center;'>CIELAB</td><td style='text-align: center;'></td><td style='text-align: center;'>0.93</td><td style='text-align: center;'>0.97</td><td style='text-align: center;'>0.51</td><td style='text-align: center;'>0.46</td><td style='text-align: center;'>0.38</td></tr><tr><td style='text-align: center;'>CIE94</td><td style='text-align: center;'>1.07</td><td style='text-align: center;'></td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>0.54</td><td style='text-align: center;'>0.49</td><td style='text-align: center;'>0.41</td></tr><tr><td style='text-align: center;'>CIEDE2000</td><td style='text-align: center;'>1.03</td><td style='text-align: center;'>0.96</td><td style='text-align: center;'></td><td style='text-align: center;'>0.52</td><td style='text-align: center;'>0.47</td><td style='text-align: center;'>0.39</td></tr><tr><td style='text-align: center;'>CAM02-SCD</td><td style='text-align: center;'>1.98</td><td style='text-align: center;'>1.84</td><td style='text-align: center;'>1.92</td><td style='text-align: center;'></td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.75</td></tr><tr><td style='text-align: center;'>CAM02-UCS</td><td style='text-align: center;'>2.20</td><td style='text-align: center;'>2.04</td><td style='text-align: center;'>2.14</td><td style='text-align: center;'>1.11</td><td style='text-align: center;'></td><td style='text-align: center;'>0.84</td></tr><tr><td style='text-align: center;'>CAM02-LCD</td><td style='text-align: center;'>2.63</td><td style='text-align: center;'>2.45</td><td style='text-align: center;'>2.56</td><td style='text-align: center;'>1.33</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'></td></tr></table>

performed to indicate the significance of the improvement with an optimized  $ k_{L} $ . The F value in Table V should be always smaller than or equal to one because this reflects the extent of the improvement from the original to the optimized formula.

In Table V, all STRESS values were less than that of observer inter-observer variability of 37 units. This implies that all the tested colour-difference formulae predicted quite accurately to the visual results.

Comparing the performance of the original formulae, CAM02-LCD performed the best among the six colour-difference formulae, and followed by CAM02-UCS, CAM02-SCD, CIE94, CIEDE2000, and CIELAB.

The performances of the six formulae slightly improved with an optimized  $ k_{L} $ . The F test was carried out to investigate the significance between the original and optimized formulae. It was found that all F values are close to one except CIELAB, indicating very little lightness parametric effect for all formulae except CIELAB. CIELAB did largely improve (but still statistically insignificant) comparing with the other five formulae and its performance surpassed CIE94 and CIEDE2000. Overall, CAM02-LCD gave the best performance, followed by CAM02-UCS, CAM02-SCD, CIELAB, CIE94, and CIEDE2000 for the  $ k_{L} $  optimized formulae. It is interesting that the optimized CIELAB formula, fitted well to the large colour difference datasets, performed worse than CAM02-SCD, developed to fit small colour difference datasets.

In the CIECAM02 family colour spaces, it is expected CAM02-LCD to perform best because it is the formula developed to fit the six large colour difference data sets including 2954 pairs of samples.⁴ CAM02-UCS is a formula developed to fit the combined all available large and small colour difference data sets. It also performed quite well. However, CAM02-SCD, developed only based on small colour difference data can give a reasonable result and outperformed CIEDE2000 in the LCD data set.

Again, the F test was conducted to indicate the difference of the performance between pairs of six original formulae. Table VI gives the results between each pair of formulae for the original formulae.

Table VI shows that the corresponding values above the diagonal were the reciprocal values of those under the diagonal. The bold italic values in the table indicated a significant difference between the two formulae located in the corresponding columns and rows. For example, CIELAB performed the worst among all the formulae tested (F values are larger than one in the first column), but these are only significant for the three CIECAM02 spaces.

In Table VI, CAM02-LCD, CAM02-UCS, and CAM02-SCD performed significantly better than the other three formulae (CIELAB, CIE94, and CIEDE2000).

It is also interesting to see that CIEDE2000 performed reasonably well for the LCD data because it was designed for applications including small colour differences.

## Small Colour Difference (SCD)

The SCD data were used to test different colour-difference formulae using the STRESS measure in this section. Table VII shows the results for the original colour-difference formulae and the formulae with optimized  $ k_{L} $  values.

Comparing the original and the optimized formulae, CAM02-SCD, CIEDE2000, and CAM02-UCS gave similar and the best performance, followed by CIE94, CAM02-LCD, and CIELAB the worst. There is no statistically significant improvement for the optimized formulae. It is surprising that CAM02-UCS can perform so well even slightly better than CIEDE2000, and CAM02-SCD, because the latter two were fitted to the experimental data with small colour difference datasets.

The F test was also conducted to compare the performance of all the original formulae and the results are shown in Table VIII. The results indicated that CAM02-UCS

<div style="text-align: center;">TABLE VII. Performance of the six formulae with original and optimized  $ k_{L} $  for SCD.</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Formula</td><td style='text-align: center;'>CIELAB</td><td style='text-align: center;'>CIE94</td><td style='text-align: center;'>CIEDE2000</td><td style='text-align: center;'>CAM02-SCD</td><td style='text-align: center;'>CAM02-UCS</td><td style='text-align: center;'>CAM02-LCD</td></tr><tr><td style='text-align: center;'>Original</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>STRESS</td><td style='text-align: center;'>40.7</td><td style='text-align: center;'>21.6</td><td style='text-align: center;'>17.2</td><td style='text-align: center;'>15.5</td><td style='text-align: center;'>15.3</td><td style='text-align: center;'>24.1</td></tr><tr><td style='text-align: center;'>Optimized  $ k_{L} $</td><td style='text-align: center;'>0.54</td><td style='text-align: center;'>1.00</td><td style='text-align: center;'>0.75</td><td style='text-align: center;'>0.78</td><td style='text-align: center;'>0.83</td><td style='text-align: center;'>0.78</td></tr><tr><td style='text-align: center;'>STRESS</td><td style='text-align: center;'>31.5</td><td style='text-align: center;'>21.6</td><td style='text-align: center;'>11.0</td><td style='text-align: center;'>10.2</td><td style='text-align: center;'>12.6</td><td style='text-align: center;'>21.3</td></tr><tr><td style='text-align: center;'>Fc = 0.25</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>F value</td><td style='text-align: center;'>0.60</td><td style='text-align: center;'>1.00</td><td style='text-align: center;'>0.41</td><td style='text-align: center;'>0.43</td><td style='text-align: center;'>0.67</td><td style='text-align: center;'>0.78</td></tr></table>

<div style="text-align: center;">TABLE VIII. F-test of the six original colour-difference formulae for SCD (Fc: F critical value).</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Fc = 0.25</td><td colspan="6">1/Fc = 4.03</td></tr><tr><td style='text-align: center;'>F value</td><td style='text-align: center;'>CIELAB</td><td style='text-align: center;'>CIE94</td><td style='text-align: center;'>CIEDE2000</td><td style='text-align: center;'>CAM02-SCD</td><td style='text-align: center;'>CAM02-UCS</td><td style='text-align: center;'>CAM02-LCD</td></tr><tr><td style='text-align: center;'>CIELAB</td><td style='text-align: center;'></td><td style='text-align: center;'>0.31</td><td style='text-align: center;'>0.18</td><td style='text-align: center;'>0.15</td><td style='text-align: center;'>0.14</td><td style='text-align: center;'>0.28</td></tr><tr><td style='text-align: center;'>CIE94</td><td style='text-align: center;'>3.18</td><td style='text-align: center;'></td><td style='text-align: center;'>0.57</td><td style='text-align: center;'>0.46</td><td style='text-align: center;'>0.45</td><td style='text-align: center;'>0.89</td></tr><tr><td style='text-align: center;'>CIEDE2000</td><td style='text-align: center;'>5.61</td><td style='text-align: center;'>1.77</td><td style='text-align: center;'></td><td style='text-align: center;'>0.82</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>1.58</td></tr><tr><td style='text-align: center;'>CAM02-SCD</td><td style='text-align: center;'>6.88</td><td style='text-align: center;'>2.17</td><td style='text-align: center;'>1.23</td><td style='text-align: center;'></td><td style='text-align: center;'>0.98</td><td style='text-align: center;'>1.94</td></tr><tr><td style='text-align: center;'>CAM02-UCS</td><td style='text-align: center;'>7.04</td><td style='text-align: center;'>2.22</td><td style='text-align: center;'>1.26</td><td style='text-align: center;'>1.02</td><td style='text-align: center;'></td><td style='text-align: center;'>1.98</td></tr><tr><td style='text-align: center;'>CAM02-LCD</td><td style='text-align: center;'>3.56</td><td style='text-align: center;'>1.12</td><td style='text-align: center;'>0.63</td><td style='text-align: center;'>0.52</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'></td></tr></table>

<div style="text-align: center;">TABLE IX. Performance of the six formulae with original and optimized  $ k_{L} $  for TCD.</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Formula</td><td style='text-align: center;'>CIELAB</td><td style='text-align: center;'>CIE94</td><td style='text-align: center;'>CIEDE2000</td><td style='text-align: center;'>CAM02-SCD</td><td style='text-align: center;'>CAM02-UCS</td><td style='text-align: center;'>CAM02-LCD</td></tr><tr><td style='text-align: center;'>Original</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>STRESS</td><td style='text-align: center;'>33.1</td><td style='text-align: center;'>30.9</td><td style='text-align: center;'>18.3</td><td style='text-align: center;'>21.2</td><td style='text-align: center;'>23.2</td><td style='text-align: center;'>27.1</td></tr><tr><td style='text-align: center;'>Optimized  $ k_{L} $</td><td style='text-align: center;'>0.82</td><td style='text-align: center;'>1.68</td><td style='text-align: center;'>1.15</td><td style='text-align: center;'>1.21</td><td style='text-align: center;'>1.27</td><td style='text-align: center;'>1.16</td></tr><tr><td style='text-align: center;'>STRESS</td><td style='text-align: center;'>32.1</td><td style='text-align: center;'>21.4</td><td style='text-align: center;'>17.4</td><td style='text-align: center;'>19.6</td><td style='text-align: center;'>20.8</td><td style='text-align: center;'>26.3</td></tr><tr><td style='text-align: center;'>Fc = 0.67</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>F value</td><td style='text-align: center;'>0.94</td><td style='text-align: center;'>0.48</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.94</td></tr></table>

and CAM02-SCD performed significantly better than CIELAB among the original formulae, while the original CIEDE2000 and CAM02-SCD gave very similar performance.

## Threshold Colour Difference (TCD)

The six colour-difference formulae were tested using the STRESS measure. The results are given in Table IX in terms of STRESS and F values.

Table IX shows that comparing both the original and the optimized formulae, CIEDE2000 performed the best, followed by CAM02-SCD, CAM02-UCS, CAM02-LCD and CIE94, and CIELAB the worst. All formulae slightly improved its performance from the original to the optimized  $ k_{L} $  formula. However, the improvement was only statistically significant for CIE94 having a  $ k_{L} $  value of 1.68. Note that CIE94 was proposed to have  $ k_{L} $  values of 1 and 2 for paint and textile materials, respectively. However, the present data is based on somewhat matte paint samples (having gloss unit of 5). This implies that the gloss may have a big impact on assessing colour differences. Further studies should be carried out to clarify this. Table X gives the F-test results for the six original formulae.

It can be seen in Table X that CIELAB performed significantly poorer than all formulae except CIE94, while CIEDE2000 performed significantly better except CAM02-SCD.

## CONCLUSION

An experiment was conducted to investigate the effective range of different colour-difference formulae. It was divided into three parts according to different colour-difference magnitudes (TCD: 0.2–1.4  $ \Delta E_{ab}^{*} $ , SCD: 2.1–6.8

<div style="text-align: center;">TABLE X. F-test of the six original colour-difference formulae for TCD (Fc: F critical value).</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">Fc = 0.67 F value</td><td colspan="6">1/Fc=1.49</td></tr><tr><td style='text-align: center;'>CIELAB</td><td style='text-align: center;'>CIE94</td><td style='text-align: center;'>CIEDE2000</td><td style='text-align: center;'>CAM02-SCD</td><td style='text-align: center;'>CAM02-UCS</td><td style='text-align: center;'>CAM02-LCD</td></tr><tr><td style='text-align: center;'>CIELAB</td><td style='text-align: center;'></td><td style='text-align: center;'>0.43</td><td style='text-align: center;'>0.31</td><td style='text-align: center;'>0.41</td><td style='text-align: center;'>0.49</td><td style='text-align: center;'>0.87</td></tr><tr><td style='text-align: center;'>CIE94</td><td style='text-align: center;'>2.31</td><td style='text-align: center;'></td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.95</td><td style='text-align: center;'>1.13</td><td style='text-align: center;'>2.01</td></tr><tr><td style='text-align: center;'>CIEDE2000</td><td style='text-align: center;'>3.28</td><td style='text-align: center;'>1.42</td><td style='text-align: center;'></td><td style='text-align: center;'>1.34</td><td style='text-align: center;'>1.61</td><td style='text-align: center;'>2.85</td></tr><tr><td style='text-align: center;'>CAM02-SCD</td><td style='text-align: center;'>2.44</td><td style='text-align: center;'>1.06</td><td style='text-align: center;'>0.74</td><td style='text-align: center;'></td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>2.12</td></tr><tr><td style='text-align: center;'>CAM02-UCS</td><td style='text-align: center;'>2.04</td><td style='text-align: center;'>0.88</td><td style='text-align: center;'>0.62</td><td style='text-align: center;'>0.84</td><td style='text-align: center;'></td><td style='text-align: center;'>1.77</td></tr><tr><td style='text-align: center;'>CAM02-LCD</td><td style='text-align: center;'>1.15</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.47</td><td style='text-align: center;'>0.56</td><td style='text-align: center;'></td></tr></table>

<div style="text-align: center;">TABLE XI. Performance of the six formulae (STRESS unit).</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Formula</td><td style='text-align: center;'>CIELAB</td><td style='text-align: center;'>CIE94</td><td style='text-align: center;'>CIEDE2000</td><td style='text-align: center;'>CAM02-SCD</td><td style='text-align: center;'>CAM02-UCS</td><td style='text-align: center;'>CAM02-LCD</td></tr><tr><td style='text-align: center;'>LCD</td><td style='text-align: center;'>21.4</td><td style='text-align: center;'>20.7</td><td style='text-align: center;'>21.1</td><td style='text-align: center;'>15.2</td><td style='text-align: center;'>14.5</td><td style='text-align: center;'>13.2</td></tr><tr><td style='text-align: center;'>SCD</td><td style='text-align: center;'>40.7</td><td style='text-align: center;'>21.6</td><td style='text-align: center;'>17.2</td><td style='text-align: center;'>15.5</td><td style='text-align: center;'>15.3</td><td style='text-align: center;'>24.1</td></tr><tr><td style='text-align: center;'>TCD</td><td style='text-align: center;'>33.1</td><td style='text-align: center;'>30.9</td><td style='text-align: center;'>18.3</td><td style='text-align: center;'>21.2</td><td style='text-align: center;'>23.2</td><td style='text-align: center;'>27.1</td></tr><tr><td style='text-align: center;'>Average</td><td style='text-align: center;'>31.8</td><td style='text-align: center;'>24.4</td><td style='text-align: center;'>18.9</td><td style='text-align: center;'>17.3</td><td style='text-align: center;'>17.7</td><td style='text-align: center;'>21.5</td></tr></table>

 $ \Delta E_{ab}^{*} $ , and LCD: 22.4–107.8  $ \Delta E_{ab}^{*} $ ). In total, 170 sample pairs were involved and 5195 estimations were made by a panel of about 20 observers. Each individual visual data set was used to test different colour-difference formulae.

Table XI summarizes the performance of the six formulae without  $ k_{L} $  optimization in terms of STRESS measure from the above study.

Table XI shows that all formulae gave quite satisfactory performance because they all had STRESS values less than that of inter-observer variability (37 STRESS units for the LCD data). There is no need to consider the hybrid formulae to cover different ranges.

In Table XI, CAM02-LCD, CAM02-UCS, and CIEDE2000 performed the best for the LCD, SCD, and TCD data sets, respectively. However, considering the average results from all three data sets, these three gave almost the similar performance. We like to propose the use of CAM02-UCS for all future applications when applying CIECAM02-based spaces. Although CAM02-UCS was fitted both the large and small colour-difference datasets, it was found that it has been performed quite robust comparing with the other two spaces in many other studies such as for predicting the other colour difference results, assessing the quality of light sources and predicting colour emotion and colour harmony. Furthermore, these spaces can be applied to different viewing conditions such as luminance levels, neutral backgrounds, surround conditions, and most importantly, illuminants, for example, to evaluate colour differences under illuminants significantly different from daylight illuminants, A, F11, F2, etc.

When selecting a conventional colour difference formula for predicting colour differences involving different magnitudes, CIEDE2000 should be used. It gave quite reasonable performance to the present dataset and should have no problem in applications involving a large range of colour differences.

## ACKNOWLEDGMENT

The authors would like to thank critical comments from both referees and to acknowledge all the observers attending the visual experiments in this study.

1. CIE Publ. 116:1995. Industrial colour-difference evaluation. Vienna: CIE Central Bureau; 1995.

2. CIE Publ. 142:2001. Improvement to industrial colour difference evaluation. Vienna: CIE Central Bureau; 2001.

3. CIE Publ. 15:2004. Colorimetry, 3rd edition. Vienna: CIE Central Bureau; 2004.

4. Luo MR, Cui G, Li C. Uniform colour spaces based on CIECAM02 colour appearance model. Color Res Appl 2006;31:320–330.

5. CIE Publ. 159:2004. A colour appearance model for colour management systems: CIECAM02. Vienna: CIE Central Bureau; 2004.

6. Guan SS, Luo MR. A colour-difference formula for assessing large colour difference. Color Res Appl 1999;24:344–355.

7. Richter K. Extended report for the members of the CIE technical committee TC 1–63 for 2005. 2005.

8. García PA, Huertas R, Melgosa M, Cui G. Measurement of the relationship between perceived and computed color difference. J Opt Soc Am A 2007;24:1823–1829.

9. CIE Publ. 13.3:1995. Method of measuring and specifying colour rendering properties of light sources. Vienna: CIE Central Bureau; 1995.

10. CIE Publ. 51.2:1999. A method for assessing the quality of daylight simulators for colorimetry. Vienna: CIE Central Bureau; 1999.

11. Kittelmann P. Visual assessment of large colour difference using 3 and 5 step colour series. Ph.D. Thesis, Technical University of Berlin, 2005.

12. Coats E, Day S, Provost JR, Rigg B. The measurement and assessment of colour differences for industrial use. III—Methods of scaling visual assessments. J Soc Dyers Colour 1972;88:186–190.

13. Thurstone LL. The measurement of values. Chicago: University of Chicago Press; 1959.

14. Luo MR, Minchew C, Kenyon P, Cui G. Verification of CIEDE2000 using industry data. Proceeding of Interim Meeting of the International Colour Association (AIC 2004 Colour and Paints), Porto Alegre, Brazil, November 3–5, 2004. p 97–102.

15. Montag ED. Empirical formula for creating error bars for the method of paired comparison. J Electron Imaging 2006;15:010502–1-3.

16. Luo MR, Cui G, Rigg B. The development of the CIE 2000 colour difference formula. Color Res Appl 2001;26:340–350.

