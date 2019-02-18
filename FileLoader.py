import logging
from tkinter import filedialog
import pathlib
import os

class FileLoader(object):

    def __init__(self):
        # Logging Parameters
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        # self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logging.WARNING)

        base_location_file = 'base_loc.conf'
        self.base_loc = str(base_location).strip()
        self.base_dir = self.set_files_dir()

        #return

    def set_files_dir(self):
        # if base_location is None:
        # Check for config file
        #base_conf_file = 'base_loc_config.conf'
        p = pathlib.Path(os.getcwd() + '/config/')



        return

        def load_file(self):
            self.logger.debug('In File Load')

        def load_all_files_from_dir(self):
            return