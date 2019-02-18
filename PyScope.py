import logging

from FileLoader import FileLoader
from LoadSettings import LoadSettings

class PyScope(object):

    def __init__(self):
        # Logging Parameters
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        # self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logging.WARNING)


        self.settings = LoadSettings()
        #self.file_loader = FileLoader()
        #self.file_loader.set_files_dir()



xml_pyscope = PyScope()