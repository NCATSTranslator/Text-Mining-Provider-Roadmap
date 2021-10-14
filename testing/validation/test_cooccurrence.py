import unittest
import jsonschema
import requests
from reasoner_validator import validate


class TestTextMiningCooccurrence(unittest.TestCase):
    base_url_smartapi = 'https://api.bte.ncats.io/v1/smartapi/5be0f321a829792e934545998b9c6afe'
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


if __name__ == '__main__':
    unittest.main()
