import logging

class WazuhRules(object):

    def __init__(self, filenames):
        # Logging Parameters
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        # self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logging.WARNING)

        self.file_path_list = filenames
        self.logger.debug('FilePaths: %s' % self.file_path_list)


    def combine_into_single_file(self):
        all_content = ''
        for file_path in self.file_path_list:
            with open(file_path, 'r') as my_wazuh_rule_file:
                self.logger.debug('TYPE: %s' %(type(my_wazuh_rule_file)))
                all_content += my_wazuh_rule_file.read()

        well_formed_agg_xml_string = '<rules>\n' + all_content + '</rules>'
        #well_formed_agg_xml_string = all_content
        self.logger.debug('All Wazuh Rules in ONE: %s' % well_formed_agg_xml_string)

        return well_formed_agg_xml_string