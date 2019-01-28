#!/bin/bash

set -e

# 1) Run all notebooks and check for errors
# jupyter nbconvert --to notebook --execute *-slides.ipynb --inplace

jupyter nbconvert --to slides --output-dir build *slides.ipynb

# add converting to pdf
# set query string to be ?print-pdf&pdfSeparateFragments=false&pdfMaxPagesPerSlide=1"
