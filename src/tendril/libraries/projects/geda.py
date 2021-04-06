

from tendril.libraries.projects.base import FileSystemProjectLibraryBase
from tendril.libraries.projects.eda import EDAProjectLibraryMixin

from tendril.entities.projects.geda import gEDAProject

from tendril.config import GEDA_PROJECTS_ROOT


class gEDAProjectLibrary(FileSystemProjectLibraryBase, EDAProjectLibraryMixin):
    _project_classes = [gEDAProject]
    _exclusions = ['.git', '.svn', 'schematic']

    def __init__(self, vctx=None):
        super(gEDAProjectLibrary, self).__init__(vctx)


def load(manager):
    manager.install_library('geda', gEDAProjectLibrary(GEDA_PROJECTS_ROOT))
