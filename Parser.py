import logging
from xml.etree import ElementTree as et
import rdflib

class Parser(object):

    def __init__(self, incoming_string):
        # Logging Parameters
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        # self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logging.WARNING)

        self.string_to_parse = incoming_string

    def parse_wazuh_XML(self):
        xml_tree_root = et.fromstring(self.string_to_parse)

        #for rule_group in xml_tree_root
        xml_rdf_graph = rdflib.Graph()
        xml_rdf_graph.parse(data=self.string_to_parse, format='xml')




