# Programming with Data: Python and Pandas

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dgerlanc/programming-with-data/master?urlpath=lab)

This repository contains the slides, exercises, and answers for
*Programming with Data: Python and Pandas*. The goal of this tutorial is to teach you, someone with experience programming in Python, most of the features available in Pandas. The material from this course has been presented at conferences including ODSC and Battlefin Discovery Data and online through the O'Reilly platform.

## Why this course exists
Whether in R, MATLAB, Stata, or python, modern data analysis, for many
researchers, requires some kind of programming. The preponderance of tools and
specialized languages for data analysis suggests that general purpose
programming languages like C and Java do not readily address the needs of data
scientists; something more is needed.

In this workshop, you will learn how to accelerate your data analyses using the
Python language and Pandas, a library specifically designed for interactive data
analysis. Pandas is a massive library, so we will focus on its core
functionality, specifically, loading, filtering, grouping, and transforming
data. Having completed this workshop, you will understand the fundamentals of
Pandas, be aware of common pitfalls, and be ready to perform your own analyses.

### Prerequisites:

Workshop assumes that participants have intermediate-level programming ability
in Python. Participants should know the difference between a `dict`, `list`, and
`tuple`. Familiarity with control-flow (`if/else/for/while`) and error handling
(`try/catch`) are required.

No statistics background is required.

## Installation

### Binder

If you have a stable Internet connection and the free Binder service isn't under too much load, the easiest way to interactively run the slides and try the exercises is to click the
Binder badge (make sure you open in a new window). Keep in mind that Binder aggresively shuts down idle instances so you'll need to refresh the link if you're idle for too long.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dgerlanc/programming-with-data/master)

### Prerendered Notebooks

You may view the HTML versions of slides and the answers directly in your browser on Github
though you will not be able to run them interactively:

* [Lesson 1 - Series](https://github.com/dgerlanc/programming-with-data/blob/master/01-intro-to-pandas-part-1-slides.ipynb)
* [Lesson 2 - DataFrames](https://github.com/dgerlanc/programming-with-data/blob/master/02-intro-to-pandas-part-2-slides.ipynb)
* [Lesson 3 - Split, Apply, Combine](https://github.com/dgerlanc/programming-with-data/blob/master/03-group-apply-slides.ipynb)
* [Lesson 4 - Time Series](https://github.com/dgerlanc/programming-with-data/blob/master/04-time-series-slides.ipynb)
* [Lesson 5 - Merge and Concat](https://github.com/dgerlanc/programming-with-data/blob/master/05-merge-pivot-slides.ipynb)
* [Lesson 6 - Advanced Merge and Reshape](https://github.com/dgerlanc/programming-with-data/blob/master/06-advanced-merge-reshape-slides.ipynb)

### Local Installation

If you're taking the course, want to follow along with the slides and do the
exercises, and may not have Internet access, download and
install the Anaconda Python 3 distribution and `conda` package manager
ahead of time:

```
https://www.anaconda.com/download/
```

Download the latest version of the course materials
[here](https://github.com/dgerlanc/programming-with-data/archive/master.zip).

Alternatively, you may clone the course repository using `git`:

```
$ git clone https://github.com/dgerlanc/programming-with-data.git
```

The remainder of the installation requires that you use the command line.

To complete the course exercises, you must use `conda` to install the
dependencies specified in the `environment.yml` file in the repository:

```
$ conda env create -f environment.yml
```

This will create an `conda` environment called `progwd` which may be
"activated" with the following commands:

* Windows: `activate progwd`
* Linux and Mac: `conda activate progwd`

Once you've activated the environment your prompt will probably
look something like this:

```
(progwd) $
```

The entire course is designed to use `jupyter` notebooks. Start the
notebook server to get started:

```
(progwd) $ jupyter lab
```

## Feedback

Your feedback on the course helps to improve it for future students.
Please leave feedback [here](https://danielgerlanc.typeform.com/to/RyB6AJ).
