#!/bin/bash
# 批量重命名论文文件，按照 [数据集名称]-[作者]-[年份]-[标题].md 的格式
# 使用方法: ./scripts/rename_papers.sh

set -e  # 遇到错误立即退出

echo "开始重命名论文文件..."
echo "================================"

# 创建备份目录
BACKUP_DIR="papers_backup_$(date +%Y%m%d_%H%M%S)"
echo "创建备份目录: $BACKUP_DIR"
cp -r papers "$BACKUP_DIR"

cd papers

# ============================================================================
# OCR处理过的文件（需要重命名）
# ============================================================================

echo ""
echo "重命名 OCR 处理过的文件..."

if [ -f "Color Research   Application - October 1991 - Berns - Visual determination of suprathreshold color‐difference tolerances.pdf_by_PaddleOCR-VL.md" ]; then
    mv "Color Research   Application - October 1991 - Berns - Visual determination of suprathreshold color‐difference tolerances.pdf_by_PaddleOCR-VL.md" \
       "RIT-DuPont-Berns-1991-Visual determination suprathreshold.md"
    echo "✅ RIT-DuPont-Berns-1991"
fi

if [ -f "Color Research   Application - 2011 - Wang - Evaluation of colour‐difference formulae for different colour‐difference.pdf_by_PaddleOCR-VL.md" ]; then
    mv "Color Research   Application - 2011 - Wang - Evaluation of colour‐difference formulae for different colour‐difference.pdf_by_PaddleOCR-VL.md" \
       "Wang-Wang-2012-Evaluation colour-difference formulae.md"
    # 为 Wanghan-LCD 创建符号链接
    ln -sf "Wang-Wang-2012-Evaluation colour-difference formulae.md" \
           "Wanghan-LCD-Wang-2012-Evaluation colour-difference formulae.md"
    echo "✅ Wang & Wanghan-LCD-Wang-2012"
fi

if [ -f "BFD-P - Luo-Rigg-BFD colour-difference formula. Part 1 - Development of the formula.pdf_by_PaddleOCR-VL.md" ]; then
    mv "BFD-P - Luo-Rigg-BFD colour-difference formula. Part 1 - Development of the formula.pdf_by_PaddleOCR-VL.md" \
       "Leeds-Luo-1987-BFD colour-difference formula Part 1.md"
    echo "✅ Leeds-Luo-1987"
fi

if [ -f "CIC_2007_art00012_Kai-Man-Raymond-Ho.pdf_by_PaddleOCR-VL.md" ]; then
    mv "CIC_2007_art00012_Kai-Man-Raymond-Ho.pdf_by_PaddleOCR-VL.md" \
       "Raymond-Display-Ho-2007-Different coloured backgrounds.md"
    echo "✅ Raymond-Display-Ho-2007"
fi

if [ -f "Color Research   Application - 2023 - Luo - A comprehensive test of colour‐difference formulae and uniform colour spaces.pdf_by_PaddleOCR-VL.md" ]; then
    mv "Color Research   Application - 2023 - Luo - A comprehensive test of colour‐difference formulae and uniform colour spaces.pdf_by_PaddleOCR-VL.md" \
       "Comprehensive-Luo-2023-Test colour-difference formulae.md"
    echo "✅ Comprehensive-Luo-2023"
fi

# ============================================================================
# 已转换的 Markdown 文件（需要重命名）
# ============================================================================

echo ""
echo "重命名已转换的 Markdown 文件..."

if [ -f "Cui et al. (2001) - Colour‐difference evaluation using CRT colours. Part I - Data gathering and testing colour difference formulae.md" ]; then
    mv "Cui et al. (2001) - Colour‐difference evaluation using CRT colours. Part I - Data gathering and testing colour difference formulae.md" \
       "Cui-Cui-2001-Evaluation using CRT colours Part I.md"
    # 为 Cui-NS 和 Cui-S-All 创建符号链接
    ln -sf "Cui-Cui-2001-Evaluation using CRT colours Part I.md" \
           "Cui-NS-Cui-2001-Evaluation using CRT colours Part I.md"
    ln -sf "Cui-Cui-2001-Evaluation using CRT colours Part I.md" \
           "Cui-S-All-Cui-2001-Evaluation using CRT colours Part I.md"
    echo "✅ Cui (NS & S-All)-Cui-2001"
fi

if [ -f "Guan & Luo (1999) - A colour-difference formula for assessing large colour differences.md" ]; then
    mv "Guan & Luo (1999) - A colour-difference formula for assessing large colour differences.md" \
       "Guan-LCD-Guan-1999-Formula large differences.md"
    echo "✅ Guan-LCD-Guan-1999"
fi

if [ -f "Huang Min et al. (2010) - Study on Small Color Difference Evaluation Using Printed Samples with Different Gloss.md" ]; then
    mv "Huang Min et al. (2010) - Study on Small Color Difference Evaluation Using Printed Samples with Different Gloss.md" \
       "BIGC-T2-Huang-2010-Small difference different gloss.md"
    # 为 BIGC-T2-M, BIGC-T2-SG, BIGC-T2-G 创建符号链接
    ln -sf "BIGC-T2-Huang-2010-Small difference different gloss.md" \
           "BIGC-T2-M-Huang-2010-Small difference different gloss.md"
    ln -sf "BIGC-T2-Huang-2010-Small difference different gloss.md" \
           "BIGC-T2-SG-Huang-2010-Small difference different gloss.md"
    ln -sf "BIGC-T2-Huang-2010-Small difference different gloss.md" \
           "BIGC-T2-G-Huang-2010-Small difference different gloss.md"
    echo "✅ BIGC-T2 (M & SG & G)-Huang-2010"
fi

if [ -f "Huang et al. (2011) - Testing uniform colour spaces and colour‐difference formulae using printed samples.md" ]; then
    mv "Huang et al. (2011) - Testing uniform colour spaces and colour‐difference formulae using printed samples.md" \
       "BIGC-S-SG-Huang-2011-Testing uniform colour spaces.md"
    echo "✅ BIGC-S-SG-Huang-2011"
fi

if [ -f "Huang et al. (2012) - Evaluation of threshold color differences using printed samples.md" ]; then
    mv "Huang et al. (2012) - Evaluation of threshold color differences using printed samples.md" \
       "BIGC-T1-SG-Huang-2012-Evaluation threshold differences.md"
    echo "✅ BIGC-T1-SG-Huang-2012"
fi

if [ -f "Liang et al. (2017) - Colour difference evaluation using display colours.md" ]; then
    mv "Liang et al. (2017) - Colour difference evaluation using display colours.md" \
       "Liang-Liang-2017-Evaluation using display colours.md"
    echo "✅ Liang-Liang-2017"
fi

if [ -f "Luo & Rigg (1986) - Chromaticity‐discrimination ellipses for surface colours.md" ]; then
    mv "Luo & Rigg (1986) - Chromaticity‐discrimination ellipses for surface colours.md" \
       "BFD-P-Luo-1986-Chromaticity discrimination ellipses.md"
    echo "✅ BFD-P-Luo-1986"
fi

if [ -f "MacAdam (1974) - Uniform color scales.md" ]; then
    mv "MacAdam (1974) - Uniform color scales.md" \
       "OSA-MacAdam-1974-Uniform color scales.md"
    echo "✅ OSA-MacAdam-1974"
fi

if [ -f "Newhall (1940) - Preliminary Report of the OSA Subcommittee on the Spacing of the Munsell Colors.md" ]; then
    mv "Newhall (1940) - Preliminary Report of the OSA Subcommittee on the Spacing of the Munsell Colors.md" \
       "Munsell-Newhall-1940-OSA Munsell spacing.md"
    echo "✅ Munsell-Newhall-1940"
fi

if [ -f "Pointer & Attridge (1997) - Some aspects of the visual scaling of large colour differences.md" ]; then
    mv "Pointer & Attridge (1997) - Some aspects of the visual scaling of large colour differences.md" \
       "Pointer-Pointer-1997-Visual scaling large differences.md"
    echo "✅ Pointer-Pointer-1997"
fi

if [ -f "Witt & Döring (1983) - Parametric variations in a threshold color‐difference ellipsoid for green painted samples.md" ]; then
    mv "Witt & Döring (1983) - Parametric variations in a threshold color‐difference ellipsoid for green painted samples.md" \
       "Witt-Witt-1983-Parametric variations threshold.md"
    echo "✅ Witt-Witt-1983"
fi

# Xu et al. 的论文
if [ -f "Xu et al. (2019) - Assessing Colour Differences under a Wide Range of Luminance Levels Using Surface and Display Colours.md" ]; then
    mv "Xu et al. (2019) - Assessing Colour Differences under a Wide Range of Luminance Levels Using Surface and Display Colours.md" \
       "HDR-Xu-2019-Wide range luminance levels.md"
    # 为 HDR-Surface 和 HDR-Display 创建符号链接
    ln -sf "HDR-Xu-2019-Wide range luminance levels.md" \
           "HDR-Surface-Xu-2019-Wide range luminance levels.md"
    ln -sf "HDR-Xu-2019-Wide range luminance levels.md" \
           "HDR-Display-Xu-2019-Wide range luminance levels.md"
    echo "✅ HDR (Surface & Display)-Xu-2019"
fi

if [ -f "Xu et al. (2021) - Testing uniform colour spaces using colour differences of a wide colour gamut.md" ]; then
    mv "Xu et al. (2021) - Testing uniform colour spaces using colour differences of a wide colour gamut.md" \
       "WCG-Xu-2021-Testing uniform spaces wide gamut.md"
    echo "✅ WCG-Xu-2021"
fi

if [ -f "Xu et al. (2022) - Parametric effects in color-difference evaluation.md" ]; then
    mv "Xu et al. (2022) - Parametric effects in color-difference evaluation.md" \
       "Parametric-Xu-2022-Parametric effects evaluation.md"
    # 为 Parametric-NS 和 Parametric-S 创建符号链接
    ln -sf "Parametric-Xu-2022-Parametric effects evaluation.md" \
           "Parametric-NS-Xu-2022-Parametric effects evaluation.md"
    ln -sf "Parametric-Xu-2022-Parametric effects evaluation.md" \
           "Parametric-S-Xu-2022-Parametric effects evaluation.md"
    echo "✅ Parametric (NS & S)-Xu-2022"
fi

# ============================================================================
# 其他可能不在数据集中的论文（保持不变或重命名为标准格式）
# ============================================================================

echo ""
echo "重命名其他论文..."

if [ -f "Davidson & Friede (1953) - The Size of Acceptable Color Differences.md" ]; then
    mv "Davidson & Friede (1953) - The Size of Acceptable Color Differences.md" \
       "Davidson-Davidson-1953-Size acceptable color differences.md"
    echo "✅ Davidson-Davidson-1953"
fi

if [ -f "Mirjalili et al. (2019) - Color-difference formula for evaluating color pairs with no separation - ΔEsubNS-sub.md" ]; then
    mv "Mirjalili et al. (2019) - Color-difference formula for evaluating color pairs with no separation - ΔEsubNS-sub.md" \
       "Mirjalili-Mirjalili-2019-Color pairs no separation.md"
    echo "✅ Mirjalili-Mirjalili-2019"
fi

if [ -f "Morley et al. (1975) - Small and Moderate Colour Differences.md" ]; then
    mv "Morley et al. (1975) - Small and Moderate Colour Differences.md" \
       "Morley-Morley-1975-Small moderate differences.md"
    echo "✅ Morley-Morley-1975"
fi

cd ..

echo ""
echo "================================"
echo "重命名完成！"
echo "备份已保存至: $BACKUP_DIR"
echo ""
echo "📊 统计信息："
echo "  - 已重命名文件数: $(find papers -name "*.md" -type f | wc -l) 个"
echo "  - 符号链接数: $(find papers -name "*.md" -type l | wc -l) 个"
echo ""
echo "⚠️  注意事项："
echo "  - 部分论文对应多个数据集，已创建符号链接"
echo "  - 如需恢复原始文件名，请使用备份目录"
echo ""

# ============================================================================
# 之前遗漏的 OCR 文件
# ============================================================================

echo ""
echo "重命名之前遗漏的 OCR 文件..."

if [ -f "12.464669.pdf_by_PaddleOCR-VL.md" ]; then
    mv "12.464669.pdf_by_PaddleOCR-VL.md" \
       "Zhu-Zhu-2001-New experimental data AIC.md"
    echo "✅ Zhu-Zhu-2001"
fi

