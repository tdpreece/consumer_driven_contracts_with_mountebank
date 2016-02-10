import unittest

from consumer1 import RecordService


class TestConsumer1(unittest.TestCase):
    longMessage = False

    def setUp(self):
        self.provider_stub_host_port = 'http://localhost:4545'
        self.sample_record_id = 100

    def test_contract(self):
        recordService = RecordService(self.provider_stub_host_port)
        record = recordService.get_record(self.sample_record_id)
        self.assertEqual(record.id, self.sample_record_id)
        self.assertIs(type(record.a), int)
        self.assertIs(type(record.b), int)


if __name__ == '__main__':
    unittest.main()
