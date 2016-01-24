import BaseHTTPServer
import time


# References:
# https://wiki.python.org/moin/BaseHttpServer
HOST_NAME = 'localhost'
PORT_NUMBER = 1912


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        """Respond to a GET request."""
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        if s.path == '/record/100':
            s.send_response(200)
            s.send_header("Content-type", "application/json")
            s.end_headers()
            s.wfile.write("{\"a\": 111, \"b\": 222}")
            return
        s.send_response(404)


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
