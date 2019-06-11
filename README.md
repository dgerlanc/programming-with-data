# Programming with Data: Python and Pandas

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dgerlanc/programming-with-data/master)

This repository contains the slides, exercises, and answers for Parts I and II
of *Programming with Data: Python and Pandas*.

## Installation

The easiest way to view the slides and try the exercises is to use the
above Binder link.

If you're taking the course and may not have Internet access, download and
install the Anaconda Python 3 distribution and `conda` package manager
ahead of time.

```
https://www.anaconda.com/download/
```

Download the latest version of the course materials
[here](https://github.com/dgerlanc/programming-with-data/archive/master.zip).

Alternatively, you may clone the course repository using `git`:

```
$ git clone https://github.com/dgerlanc/programming-with-data.git
```

To complete the workshop exercises, you must use `conda` to install the
dependencies specified in the `environment.yml` file in the repository:

```
$ conda env create -f environment.yml
```

This will create an `conda` environment called `pydata` which may be
"activated" with the following commands:

* Windows: `activate pydata`
* Linux and Mac: `conda activate pydata` or `source activate pydata`

The entire course is designed to use `jupyter` notebooks. Start the
notebook server to get started:

```
(pydata) $ jupyter notebook
```

## Programming with Data: Foundations of Python and Pandas

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

## Feedback

Your feedback on the course helps to improve it for future students.
Please leave feedback [here](https://danielgerlanc.typeform.com/to/RyB6AJ).
