#!/bin/bash

set -e

jupyter nbconvert --to slides --output-dir build *slides.ipynb

# add converting to pdf
# set query string to be ?print-pdf&pdfSeparateFragments=false
