import logging

from FileLoader import FileLoader
from PyScopeSettings import PyScopeSettings

class PyScope(object):

    def __init__(self):
        # Logging Parameters
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        # self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logging.WARNING)


        self.settings = PyScopeSettings()
        self.file_loader = FileLoader(self.settings.raw_files_dir)
        #self.file_loader.set_files_dir()
        self.file_loader.combine_xml_files_to_single()



xml_pyscope = PyScope()