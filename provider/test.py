import requests
import unittest


class TestProvider(unittest.TestCase):
    def test_contract(self):
        contractual_response = requests.get('http://localhost:4545/an-item-slug')
        actual_response = requests.get('http://localhost:1912/an-item-slug')
        contractual_response_json = contractual_response.json()
        actual_response_json = actual_response.json()
        self.assertEqual(actual_response.status_code, contractual_response.status_code)
        self.assertDictContainsSubset(contractual_response_json, actual_response_json)


if __name__ == '__main__':
    unittest.main()
