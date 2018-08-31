# Programming with Data: Python and Pandas

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

## Prerequisites:

Workshop assumes that participants have intermediate-level programming ability
in Python. Participants should know the difference between a `dict`, `list`, and
`tuple`. Familiarity with control-flow (`if/else/for/while`) and error handling
(`try/catch`) are required.

No statistics background is required.

Each participant should have a laptop with the Anaconda Python 3 distribution
and `conda` package manager installed:

```
https://www.anaconda.com/download/
```

The slides and exercises that accompany the workshop are available on Github:

```
$ git clone https://github.com/dgerlanc/programming-with-data.git
```

Downloading them prior to the workshop is required as Internet access may not be
available during the workshop.

To complete the workshop exercises, you must use `conda` to install the
dependencies specified in the `environment.yml` file in the repository:

```
$ conda env create -f environment.yml
```

This will create an `conda` environment called `pydata` which may be
"activated" with the following commands:

* Windows: `activate pydata`
* Linux and Mac: `source activate pydata`

