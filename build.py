#!/usr/bin/env python3

import subprocess
from functools import partial
from multiprocessing import Pool
from pathlib import Path

# TODO: Only update files changed since last run
# TODO: Add conversion tool from existing answer notebooks
# TODO: add test for errors when individual tasks fail


def answer2exercise(infile, outfile):
    """
    Convert answer notebooks to exercise notebooks

    TODO: Fail if output notebook is empty?

    """
    cmd = "jupyter nbconvert --config config.py --to notebook --output".split()
    cmd.extend([outfile, infile])
    subprocess.run(cmd)


def slide2html(infile):
    """
    Convert slide notebooks to reveal.js

    """
    cmd = (
        "jupyter nbconvert"
        " --to slides"
        " --reveal-prefix=reveal.js"
        " --SlidesExporter.file_extension=.html"
        " --output-dir build"
    ).split()
    cmd.append(str(infile))
    subprocess.run(cmd)


def run_slide(infile):
    cmd = "jupyter nbconvert --to notebook --inplace --execute".split()
    cmd.append(str(infile))

    devnull = subprocess.DEVNULL
    subprocess.run(cmd, check=True, stdout=devnull, stderr=devnull)


def main():
    p = Path(".")

    slide_fns = sorted(str(x) for x in p.glob("*slides.ipynb"))
    answer_nbs = sorted(str(x) for x in p.glob("*answers.ipynb"))
    exercise_nbs = [x.replace("answer", "exercise") for x in answer_nbs]

    with Pool(4) as pool:
        print("Running notebooks")
        pool.map(run_slide, slide_fns)

        print("ipynb slides -> reveal.js html")
        pool.map(slide2html, slide_fns)

        print("Convert answers to exercises")
        # print(f'{answer_nb} -> {exercise_nb}')
        pool.starmap(answer2exercise, zip(answer_nbs, exercise_nbs))

    # copy over assets

    # html slides -> pdf


if __name__ == "__main__":
    main()
