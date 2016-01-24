import requests
import unittest


class TestAgainstConsumer1(unittest.TestCase):
    def setUp(self):
        self.stub_host_port = 'http://localhost:4545'
        self.actual_host_port = 'http://localhost:1912'

    def test_contract(self):
        path = '/record/100'
        contractual_response = requests.get(self.stub_host_port+path)
        actual_response = requests.get(self.actual_host_port+path)
        self.assertEqual(actual_response.status_code, contractual_response.status_code)
        contractual_response_json = contractual_response.json()
        actual_response_json = actual_response.json()
        self.assertDictContainsSubset(
            contractual_response_json,
            actual_response_json
        )


if __name__ == '__main__':
    unittest.main()
