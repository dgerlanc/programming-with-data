# coding: utf-8

import nbformat
from nbconvert import NotebookExporter
from nbconvert.preprocessors import Preprocessor
from traitlets.config import Config



def all_tags(nb):
    rv = set()
    for cell in nb.cells:
        tags = cell.metadata.get('tags')
        if tags:
            for tag in tags:
                rv.add(tag)
    return rv


class ExercisePreprocessor(Preprocessor):
    """A """
    keep_tags = ('setup', 'exercise')
    
    def preprocess(self, nb, resources):
        cells = []
        for cell in nb.cells:
            tags = cell.metadata.get('tags', tuple())
            
            if any(tag in self.keep_tags for tag in tags):
                cell.execution_count = None
                cell.outputs = []
                cells.append(cell)
        
        nb.cells = cells
        return nb, resources


class ExerciseExporter(NotebookExporter):
    preprocessors = [ExercisePreprocessor]


def main():
    nb = nbformat.read('04-merge-pivot-answers.ipynb', as_version=nbformat.NO_CONVERT)

    # In[5]:

    exporter = NotebookExporter()
    body, resources = exporter.from_notebook_node(nb)

    # In[6]:

    c = Config()
    c.NotebookExporter.preprocessors = [ExercisePreprocessor]
    exercise_exporter = NotebookExporter(config=c)
    # exercise_exporter.preprocessors

    # In[7]:

    body2, res2 = exercise_exporter.from_notebook_node(nb)

    # In[8]:

    nb2 = nbformat.reads(body2, 4)


    # In[9]:

    # nb3 = nbformat.read('04-merge-pivot-exercises.ipynb', as_version=nbformat.NO_CONVERT)

    # nb3