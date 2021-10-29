import unittest
import yaml
import gzip
import json
import os
import re
from urllib.request import urlretrieve


class TestTargetedKGX(unittest.TestCase):
    json_attributes_schema = {}
    test_edge_lines = []
    test_node_lines = []
    test_line_count = 50
    targeted_edges_file_url = "https://storage.googleapis.com/translator-text-workflow-dev-public/kgx/UniProt/edges.tsv.gz"
    targeted_nodes_file_url = "https://storage.googleapis.com/translator-text-workflow-dev-public/kgx/UniProt/nodes.tsv.gz"
    edge_tsv_regex_list = [r'\w+:\w+', r'biolink:\w+', r'\w+:\w+', r'\w{27,}', r'biolink:\w+', r'0\.\d+',
                           r'tmkp:\w+(|tmkp:\w+)*', r'PMID:\d{7,8}(|PMID:\d{7,8})*']
    node_tsv_regex_list = [r'\w+:\w+', r'.+', r'\w+:\w+']

    @classmethod
    def setUpClass(cls) -> None:  # pragma: no cover
        if 'testing' not in os.getcwd():
            os.chdir(f'{os.getcwd()}/testing/validation')
        with open('targeted_json_attributes.yml', 'r') as infile:
            cls.json_attributes_schema = yaml.safe_load(infile)
        if not os.path.isfile("targeted_edges.tsv.gz"):
            urlretrieve(cls.targeted_edges_file_url, 'targeted_edges.tsv.gz')
        with gzip.open('targeted_edges.tsv.gz', 'rb') as edge_file:
            for i in range(cls.test_line_count):
                cls.test_edge_lines.append(edge_file.readline().decode('utf-8'))
        if not os.path.isfile("targeted_nodes.tsv.gz"):
            urlretrieve(cls.targeted_nodes_file_url, 'targeted_nodes.tsv.gz')
        with gzip.open('targeted_nodes.tsv.gz', 'rb') as node_file:
            for i in range(cls.test_line_count):
                cls.test_node_lines.append(node_file.readline().decode('utf-8'))

    def test_node_tsv_columns(self):
        for line in self.test_node_lines:
            cols = line.split('\t')
            self.assertEqual(len(cols), len(self.node_tsv_regex_list))
            for i in range(len(cols)):
                self.assertIsNotNone(re.match(self.node_tsv_regex_list[i], cols[i]))

    def test_edge_tsv_columns(self):
        for line in self.test_edge_lines:
            cols = line.split('\t')
            self.assertEqual(len(cols), len(self.edge_tsv_regex_list) + 1)
            for i in range(len(self.edge_tsv_regex_list)):
                self.assertIsNotNone(re.match(self.edge_tsv_regex_list[i], cols[i]))

    def test_edge_json_attributes(self):
        for attribute in self.json_attributes_schema:
            for line in self.test_edge_lines:
                cols = line.split('\t')
                json_blob = json.loads(cols[-1])
                json_object = get_attribute_object(json_blob, attribute["attribute_type_id"])
                for property_key, property_value in attribute.items():
                    if type(property_value) == list:
                        for inner_attribute in property_value:
                            inner_json_object = get_attribute_object(json_object[property_key], inner_attribute["attribute_type_id"])
                            for inner_key, inner_value in inner_attribute.items():
                                text = str(inner_json_object[inner_key]).strip()
                                if inner_value.startswith('<') and inner_value.endswith('>'):
                                    regex = re.compile(inner_value[1:-1])
                                    self.assertIsNotNone(regex.match(text))
                                else:
                                    self.assertEqual(text, inner_value)
                    elif property_value.startswith('<') and property_value.endswith('>'):
                        regex = re.compile(property_value[1:-1])
                        self.assertIsNotNone(regex.match(str(json_object[property_key])))
                    else:
                        self.assertEqual(json_object[property_key], property_value)


def get_attribute_object(blob, atrribute_type_id) -> dict:
    for obj in blob:
        if obj['attribute_type_id'] == atrribute_type_id:
            return obj


def get_attribute_list(blob, attribute_type_id) -> list:
    object_list = []
    for obj in blob:
        if obj['attribute_type_id'] == attribute_type_id:
            object_list.append(obj)
    return object_list


if __name__ == '__main__':
    unittest.main()
