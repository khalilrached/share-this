import mimetypes
import os
from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer
from lib import LoggerBuilder

logger = LoggerBuilder.getLogger(os.path.basename(__file__).removesuffix(".py"))


class ServerHandler(BaseHTTPRequestHandler):

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


class ServerFactory:
    host_name: str = None
    port: int = None

    @staticmethod
    def create_server(hostname='localhost', port=5000):
        ServerFactory.port = port
        ServerFactory.host_name = hostname
        Server.httpd = HTTPServer((hostname, port), ServerHandler)
        return Server()


class Server:
    httpd: HTTPServer = None
    thread: Thread = None

    @staticmethod
    def serve():
        try:
            Server.httpd.serve_forever()
        except Exception as ex:
            logger.error(type(ex))

    @staticmethod
    def start_server():
        logger.debug("starting the server. ")
        Server.thread = Thread(target=Server.serve)
        Server.thread.start()
        logger.info(f"server is ready http://{ServerFactory.host_name}:{ServerFactory.port}/.")

    @staticmethod
    def close_server():
        logger.debug("closing the server. ")
        Server.thread = None
        Server.httpd.server_close()
