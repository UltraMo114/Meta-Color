#!/bin/bash
# Convert Markdown report to professional PDF using Pandoc

pandoc Audit_Report_v2.md \
  -o Audit_Report_v2.pdf \
  --pdf-engine=xelatex \
  --template=eisvogel \
  --listings \
  --number-sections \
  --toc \
  --toc-depth=2 \
  -V colorlinks=true \
  -V linkcolor=blue \
  -V urlcolor=blue \
  -V toccolor=gray \
  --bibliography=references.bib \
  --csl=color-research-and-application.csl \
  -M date="`date "+%B %Y"`"

echo "PDF generated: Audit_Report_v2.pdf"
