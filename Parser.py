import logging
from xml.etree import ElementTree as et
import json
import xmltodict

import rdflib
import networkx as nx

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
        # Using RDFlib
        xml_rdf_graph = rdflib.Graph()
        self.logger.debug('Type expecting Graph: %s' % type(xml_rdf_graph))
        #xml_rdf_graph.parse(data=self.string_to_parse, format='xml')

        xml_dict = xmltodict.parse(self.string_to_parse)
        self.logger.debug('Type expecting DICT: %s' % type(xml_dict))
        # XML Dict to Simple JSON Format
        json_format = json.loads(json.dumps(xml_dict))
        self.logger.debug('Type expecting JSON: %s' % type(json_format))
        # Pretty Print the JSON
        self.logger.debug('JSON: %s' % json.dumps(json_format, indent=4, sort_keys=True))

        #Using Networkx
        #netx_graph = nx.readwrite.jit_data(json_format)
        #nx.read





