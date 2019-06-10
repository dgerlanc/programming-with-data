#!/usr/bin/env python3

import subprocess
from pathlib import Path


# TODO: Only update files changed since last run
# TODO: Add conversion tool from existing nbs

def answer2exercise(infile: Path, outfile: Path):
    """
    Convert answer notebooks to exercise notebooks
    
    TODO: Fail if output notebook is empty?

    """
    cmd = 'jupyter nbconvert --config config.py --to notebook --output'.split()
    cmd.extend([outfile, infile])
    subprocess.run(cmd)


def slide2html(infile: Path, outfile: Path):
    """
    Convert slide notebooks to reveal.js

    """
    cmd = ('jupyter nbconvert --to slides --reveal-prefix=reveal.js'
           '--output-dir build --output').split()
    cmd.extend([outfile, infile]
    subprocess.run(cmd)
               
    
def main():
    p = Path('.')

    # TODO: execute slides and make sure no errors

               
    # ipynb slides -> reveal.js html
    slide_fns = p.glob('*slides.ipynb')
    for slide_fn in sorted(slide_fns):
        html_slides = str(slide_fns).replace('ipynb', 'html')
        # print(f'{answer_nb} -> {exercise_nb}')
        slide2html(slide_nb, html_slides)
               
    # convert exercises to answers
    answers = p.glob('*answers.ipynb')
    for answer_nb in sorted(answers):
        exercise_nb = str(answer_nb).replace('answer', 'exercise')
        # print(f'{answer_nb} -> {exercise_nb}')
        answer2exercise(answer_nb, exercise_nb)

               
    # html slides -> pdf

               
if __name__ == '__main__':
    main()
