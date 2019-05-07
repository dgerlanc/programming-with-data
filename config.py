# coding: utf-8

from nbconvert.preprocessors import Preprocessor

def _all_tags(nb):
    rv = set()
    for cell in nb.cells:
        tags = cell.metadata.get('tags')
        if tags:
            for tag in tags:
                rv.add(tag)
    return rv


class ExercisePreprocessor(Preprocessor):
    """A """
    keep_tags = {'setup', 'exercise'}
    
    def preprocess(self, nb, resources):
        cells = []
        for cell in nb.cells:
            tags = cell.metadata.get('tags', tuple())
            
            if any(tag in self.keep_tags for tag in tags):
                # must check if cell.cell_type == 'code'
#                cell.execution_count = None
#                cell.outputs = []
                cells.append(cell)
        
        nb.cells = cells

        nb.metadata.pop('celltoolbar', None)
        nb.metadata.pop('toc', None)
        
        return nb, resources


c = get_config()
c.Exporter.preprocessors = [
    ExercisePreprocessor,
    'nbconvert.preprocessors.TagRemovePreprocessor',
    'nbconvert.preprocessors.ClearOutputPreprocessor'
]
