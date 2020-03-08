#!/bin/bash
#rm *.bbl *.blg *.bcf *.fls *.pdf *.toc *.aux *.out *.log
#find . -name "*.aux" -type f -delete
pdflatex main.tex
biber main
pdflatex main.tex
rm *.bbl *.blg *.bcf *.toc *.aux *.log
exit 0
