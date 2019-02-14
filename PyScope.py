import logging


class PyScope(object):

    def __init__(self):
        # Logging Parameters
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        # self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logging.WARNING)

        self.base_dir = ''

    def set_files_dir(self):


    def load_file(self):
        self.logger.debug('In File Load')


    def load_all_files_from_dir(self):