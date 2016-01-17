import requests
import unittest


class TestProvider(unittest.TestCase):
    def test_contract(self):
        contractual_response = requests.get('http://localhost:4545/an-item-slug')
        actual_response = requests.get('http://localhost:1912/an-item-slug')
        # TODO Don't want to test that they're equal, just that the consumer
        # can use what's provided.
        self.assertEqual(actual_response.status_code, contractual_response.status_code)
        self.assertEqual(actual_response.text, contractual_response.text)


if __name__ == '__main__':
    unittest.main()
