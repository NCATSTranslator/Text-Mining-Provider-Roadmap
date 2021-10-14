import unittest

import jsonschema.exceptions
import requests
import json
from reasoner_validator import validate
from jsonschema import ValidationError


class TestTextMiningTargetedAssociation(unittest.TestCase):
    base_url_smartapi = 'https://api.bte.ncats.io/v1/smartapi/978fe380a147a8641caf72320862697b'
    payload = {
        "message": {
            "query_graph": {
                "edges": {
                    "e00": {
                        "subject": "n00",
                        "object": "n01"
                    }
                },
                "nodes": {
                    "n00": {
                        "ids": [
                            "DRUGBANK:DB00215",
                            "DRUGBANK:DB01175",
                            "DRUGBANK:DB00472",
                            "DRUGBANK:DB00176",
                            "DRUGBANK:DB00715",
                            "DRUGBANK:DB01104"
                        ],
                        "categories": ["biolink:SmallMolecule"]
                    },
                    "n01": {
                        "categories": ["biolink:Gene"]
                    }
                }
            }
        }
    }

    def test_query_results(self):
        passed_validation = True
        res = requests.post(self.base_url_smartapi + '/query/', json=self.payload)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers['Content-Type'], 'application/json')
        json_response = res.json()
        self.assertTrue("workflow" in json_response)
        self.assertTrue("message" in json_response)
        self.assertTrue("query_graph" in json_response["message"])
        self.assertTrue("knowledge_graph" in json_response["message"])
        self.assertTrue("results" in json_response["message"])
        try:
            validate(json_response["message"], "Message", "1.2.0")
        except jsonschema.exceptions.ValidationError as v:
            print(v.message)
            passed_validation = False
        self.assertTrue(passed_validation)

    def test_message(self):
        passed_validation = True
        with open('message.json', 'r') as message_file:
            message = message_file.read()
        try:
            validate(json.loads(message), "Message", "1.2.0")
        except ValidationError as v:
            print(v.message)
            passed_validation = False
        self.assertTrue(passed_validation)


if __name__ == '__main__':
    unittest.main()
