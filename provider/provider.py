import BaseHTTPServer
import json
import os
import re
import time


# References:
# https://wiki.python.org/moin/BaseHttpServer
HOST_NAME = 'localhost'
PORT_NUMBER = 1912


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        """Respond to a GET request."""
        matches = re.match(r'^/record/(\d+)$', self.path)
        if matches:
            record_id = matches.group(1)
            record = DataStore.get_record(record_id)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(record))
            return
        self.send_response(404)

    def do_POST(self):
        """Respond to a GET request."""
        if self.path == '/record':
            # TODO: Implement code to allocate id and save record.
            self.send_response(201)
            # TODO: Fix 'Transfer-Encoding' not found in headers
            # failure in test for consumer 3.
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({'id': 100}))
            return
        self.send_response(500)


class DataStore(object):
    @staticmethod
    def get_record(record_id):
        with open(record_id, 'r') as f:
            record = json.load(f)
        return record

    @staticmethod
    def save_record(record):
        file_name = str(record['id'])
        with open(file_name, 'w') as f:
            json.dump(record, f)

    @staticmethod
    def delete_record(record):
        file_name = str(record['id'])
        os.remove(file_name)


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
