import BaseHTTPServer
import json
import time


# References:
# https://wiki.python.org/moin/BaseHttpServer
HOST_NAME = 'localhost'
PORT_NUMBER = 1912


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        """Respond to a GET request."""
        if self.path == '/record/100':
            record_id = '100'
            record = DataStore.get_record(record_id)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(record))
            return
        self.send_response(404)


class DataStore(object):
    @staticmethod
    def get_record(record_id):
        with open(record_id, 'r') as f:
            record = json.load(f)
        return record


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
