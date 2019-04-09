#!/bin/bash

set -e

# 1) Run all notebooks and check for errors
# jupyter nbconvert --inplace --to notebook --execute *-slides.ipynb

jupyter nbconvert --to slides --output-dir build *slides.ipynb

# add converting to pdf
# set query string to be ?print-pdf&pdfSeparateFragments=false&pdfMaxPagesPerSlide=1"

# add combining for classes
# pdfconcat --output programming-with-data-foundations.pdf 0[1-3]*pdf
