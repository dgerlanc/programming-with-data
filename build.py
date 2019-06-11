#!/usr/bin/env python3

import logging
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)

# TODO: Only update files changed since last run
# TODO: Add conversion tool from existing answer notebooks

def answer2exercise(infile, outfile):
    """
    Convert answer notebooks to exercise notebooks
    
    TODO: Fail if output notebook is empty?

    """
    cmd = 'jupyter nbconvert --config config.py --to notebook --output'.split()
    cmd.extend([outfile, infile])
    subprocess.run(cmd)


def slide2html(infile):
    """
    Convert slide notebooks to reveal.js

    """
    cmd = ('jupyter nbconvert'
           ' --to slides'
           ' --reveal-prefix=reveal.js'
           ' --SlidesExporter.file_extension=.html'
           ' --output-dir build').split()
    cmd.append(str(infile))
    subprocess.run(cmd)


def run_slide(infile):
    cmd = 'jupyter nbconvert --to notebook --inplace --execute'.split()
    cmd.append(str(infile))

    devnull = subprocess.DEVNULL
    subprocess.run(cmd, check=True, stdout=devnull, stderr=devnull)


def main():
    p = Path('.')

    # TODO: add test for errors
    slide_fns = p.glob('*slides.ipynb')
    for slide_fn in sorted(slide_fns):
        run_slide(slide_fn)

    logger.info('ipynb slides -> reveal.js html')
    slide_fns = p.glob('*slides.ipynb')
    for slide_fn in sorted(slide_fns):
        slide2html(slide_fn)
    
    logger.info('Convert exercises to answers')
    answers = p.glob('*answers.ipynb')
    for answer_nb in sorted(answers):
        exercise_nb = str(answer_nb).replace('answer', 'exercise')
        # print(f'{answer_nb} -> {exercise_nb}')
        answer2exercise(str(answer_nb), exercise_nb)

    # copy over assets

    # html slides -> pdf


               
if __name__ == '__main__':
    main()
