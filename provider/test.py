import requests
import unittest

import provider


class TestAgainstConsumer1(unittest.TestCase):
    def setUp(self):
        self.stub_host_port = 'http://localhost:4545'
        self.actual_host_port = 'http://localhost:1912'

    def test_contract(self):
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
        path = '/record'
        record = {"a": 123, "b": 222, "c": 333}

        contractual_response = requests.post(
            self.stub_host_port+path,
            json=record
        )
        actual_response = requests.post(
            self.actual_host_port+path,
            json=record
        )

        self.assertEqual(
            actual_response.status_code,
            contractual_response.status_code
        )
        # The consumer shouldn't mind if the provider returns some
        # extra data.=`=jedi=0, =`=  (*_*expr*_*, msg=None) =`=jedi=`=
        self.assertDictContainsSubset(
            contractual_response.json(),
            actual_response.json()
        )


if __name__ == '__main__':
    unittest.main()
