#!/bin/bash

# Merge the binder and dev dependencies into a single environment

conda-merge binder/environment.yml environment-dev.yml > environment.yml
