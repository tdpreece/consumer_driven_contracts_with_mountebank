import json
import os
import requests
import unittest

import provider


class TestAgainstConsumer1(unittest.TestCase):
    def setUp(self):
        self.stub_host_port = 'http://localhost:4545'
        self.actual_host_port = 'http://localhost:1912'

    def test_contract(self):
        # TODO Extract test definition in contract and read in for test.
        # See consumer 3 tests for details.
        path = '/record/100'
        # The provider has state.  Data is setup for the test to avoid brittle
        # tests that depend on the output of other tests.
        # See discussion here:
        # https://github.com/realestate-com-au/pact/wiki/Provider-states
        record = {"id": 100, "a": 111, "b": 222, "c": 333}
        provider.DataStore.save_record(record)

        contractual_response = requests.get(self.stub_host_port+path)
        actual_response = requests.get(self.actual_host_port+path)

        self.assertEqual(
            actual_response.status_code,
            contractual_response.status_code
        )
        # The consumer shouldn't mind if the provider returns some
        # extra data.
        self.assertDictContainsSubset(
            contractual_response.json(),
            actual_response.json()
        )
        provider.DataStore.delete_record(record)


class TestAgainstConsumer2(unittest.TestCase):
        # TODO Extract test definition in contract and read in for test.
        # See consumer 3 tests for details.
    def setUp(self):
        self.stub_host_port = 'http://localhost:4546'
        self.actual_host_port = 'http://localhost:1912'

    def test_contract(self):
        path = '/record/100'
        record = {"id": 100, "a": 123, "b": 222, "c": 333}
        provider.DataStore.save_record(record)

        contractual_response = requests.get(self.stub_host_port+path)
        actual_response = requests.get(self.actual_host_port+path)

        self.assertEqual(
            actual_response.status_code,
            contractual_response.status_code
        )
        # The consumer shouldn't mind if the provider returns some
        # extra data.
        self.assertDictContainsSubset(
            contractual_response.json(),
            actual_response.json()
        )
        provider.DataStore.delete_record(record)


class TestAgainstConsumer3(unittest.TestCase):
    def setUp(self):
        self.stub_host_port = 'http://localhost:4547'
        self.actual_host_port = 'http://localhost:1912'

    def test_contract(self):
        # The tests could be configured to loop through all the request
        # definitions in a contracts dir.  Thus, the provider team would
        # not have to write as many new tests for changes to the consumer
        # contracts.
        request_definition_file = os.path.join(
            os.environ['CONSUMER_CONTRACTS_ROOT'],
            'contracts/includes/consumer3_expected_request.json'
        )
        with open(request_definition_file, 'r') as f:
            request_defintion = json.load(f)

        contractual_response = requests.patch(
            self.stub_host_port + request_defintion['path'],
            json=request_defintion['json']
        )
        actual_response = requests.patch(
            self.actual_host_port + request_defintion['path'],
            json=request_defintion['json']
        )

        self.assertEqual(
            actual_response.status_code,
            contractual_response.status_code
        )
        # Matching headers from Mountebank to headers from service import can
        # be difficult because Mountebank can add extra headers that aren't
        # important to the implementation, thus need to list the expected
        # headers here.  See also,
        # https://github.com/realestate-com-au/pact/wiki/Matching-gotchas
        # TODO: Read from Mountebank config so only in one place.
        expected_headers = ['Location']
        for header_key in expected_headers:
            self.assertIn(header_key, actual_response.headers.keys())


if __name__ == '__main__':
    unittest.main()
