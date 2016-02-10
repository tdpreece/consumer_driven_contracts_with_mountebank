import requests


class RecordService(object):
    longMessage = False

    def __init__(self, provider_host_port):
        self.provider_host_port = provider_host_port

    def get_record(self, record_id):
        record_url = '{host_port}/record/{id}'.format(
            host_port=self.provider_host_port,
            id=record_id
        )
        response = requests.get(record_url)
        return Record(response.json())


class Record(object):
    def __init__(self, record_dict):
        self.id = record_dict['id']
        self.a = record_dict['a']
        self.b = record_dict['b']
