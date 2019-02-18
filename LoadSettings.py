import logging
import pathlib
import os
from tkinter import filedialog


class LoadSettings(object):

    def __init__(self):
        # Logging Parameters
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        # self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logging.WARNING)

        self.config_dir = self.check_config_dir()
        self.logger.debug('Config Dir: --> \t %s' % self.config_dir)
        #self.base_config_file = 'base.conf'
        self.raw_files_config_file = 'base.conf'
        self.raw_files_dir = self.check_config_file()

    def check_config_dir(self):
        # if base_location is None:
        # Check for config file
        #base_conf_file = 'base_loc_config.conf'
        p = pathlib.Path(os.getcwd() + '/config/')

        # Check if config directory exists
        if not os.path.exists(p):
            # If it does not exist, create it
            os.makedirs(p)

        self.logger.debug('CONFIG Directory Absolute Path: %s' % p.resolve())
        self.logger.debug('Base Config DIRECTORY exists: %s' % p.exists())
        return p

    def check_config_file(self):
        expected_conf_file_loc = pathlib.Path(self.config_dir) / pathlib.Path(self.raw_files_config_file)
        self.logger.debug('Base Config File Loc: --> \t %s' % expected_conf_file_loc)
        #self.logger.debug('Base Config File Size: --> %s' % os.stat(str(expected_conf_file_loc)).st_size)
        the_raw_files_dir =''

        try:
            base_conf_size = os.stat(str(expected_conf_file_loc)).st_size
            self.logger.info('Base Config File Size: --> %d' % base_conf_size)
            if base_conf_size == 0:
                self.logger.warning('Base Config File is Empty')
                with expected_conf_file_loc.open('a+') as f:
                    the_raw_files_dir = filedialog.askdirectory(initialdir='',
                                                                     title='Select Directory where to Load Files to parse from')
                    f.write(the_raw_files_dir)
                    # f.write(self.raw_files_config_file)
                    f.close()
            else:
                # Open and read the config file
                with expected_conf_file_loc.open('r') as file_read:
                    for line in file_read:
                        the_raw_files_dir = line.strip()
                        if the_raw_files_dir == '':
                            the_raw_files_dir = filedialog.askdirectory(initialdir='',
                                                                     title='Select Directory where to Load Files to parse from')

        except:
            self.logger.debug('Hit Exception: --> something with the base config file not existing perhaps')
            # If config file does not exist, create it
            self.logger.info('Creating Raw Files Directory CONFIG File')
            #self.raw_files_config_file = filedialog.askdirectory(initialdir='')
            with expected_conf_file_loc.open('a+') as f:
                the_raw_files_dir = filedialog.askdirectory(initialdir='',
                                                              title='Select Directory where to Load Files to parse from')
                f.write(the_raw_files_dir)
                #f.write(self.raw_files_config_file)
                f.close()

        return the_raw_files_dir

