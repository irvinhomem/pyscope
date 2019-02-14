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

        self.base_dir = self.set_files_dir()

        #return

    def set_files_dir(self):
        # if base_location is None:
        # Check for config file
        base_conf_file = 'base_loc_config.conf'
        p = pathlib.Path(os.getcwd() + '/config/')

        # Check if config directory exists
        if not os.path.exists(p):
            # If it does not exist, create it
            os.makedirs(p)

        self.logger.debug('CONFIG Directory Absolute Path: %s' % p.resolve())
        self.logger.debug('Base Config DIRECTORY exists: %s' % p.exists())

        try:
            # If current working directory has path and file size is empty
            self.logger.debug('File path: %s' % os.stat(str(p)))
            if os.stat(str(p)).st_size == 0:
                self.logger.warning("base_config file is empty")
                self.base_loc == filedialog.askdirectory(initialdir='', title='Select Base Location home-dir')
                with p.open('a+') as f:
                    f.write(self.base_loc)
                    f.close()
            else:
                with p.open('r') as rf:
                    for line in rf:
                        self.base_loc = line.strip()
                        if self.base_loc == '':
                            self.base_loc == filedialog.askdirectory(initialdir='',
                                                                     title='Select Base Location home-dir')
                        else:
                            self.logger.debug("Loaded CapBase path: %s", self.base_loc)
                            # self.logger.info("test info")
                            # self.logger.warning("test warning")
                            # print('test')
        except:
            self.logger.warning("base_loc_config does not exist. Create base_loc_config file")
            # If config file doesn't exist create it
            self.base_loc = filedialog.askdirectory(initialdir='')
            with p.open('a+') as f:
                f.write(self.base_loc)
                f.close()

        return

        def load_file(self):
            self.logger.debug('In File Load')

        def load_all_files_from_dir(self):
            return