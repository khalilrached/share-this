import json
import mimetypes
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from lib import LoggerBuilder

logger = LoggerBuilder.getLogger(os.path.basename(__file__).removesuffix(".py"))

logger.trace(f"%SERVER_HOME%={os.environ['SERVER_HOME']}")
logger.trace(f"%SERVER_PUBLIC%={os.environ['SERVER_HOME']}")


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        mimetype, _ = mimetypes.guess_type(self.path)
        file_path = os.path.join(os.environ["SERVER_PUBLIC"], self.path.removeprefix("/"))
        if not os.path.exists(file_path):
            logger.debug(f"File does not exist: {file_path}")
            self.send_response(404)
            self.end_headers()
            return
        # check if file does exist in public folder
        if self.path[-3:] == ".py":
            logger.warn(f"cannot access py files.")
            self.send_response(403)
            self.end_headers()
            return
        # try to read the file and send it back
        file = open(file_path, 'rb').read()
        self.send_response(200)
        self.send_header('Content-type', mimetype)
        self.end_headers()
        self.wfile.write(file)


if __name__ == "__main__":
    SERVER = "localhost"
    PORT = 5000
    httpd = HTTPServer((SERVER, PORT), Server)
    httpd.serve_forever()
