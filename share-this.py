import os
import platform
from sys import *

from lib import LoggerBuilder, parse_options, ServerFactory


# init logger
logger = LoggerBuilder.getLogger(__file__)

def server_start_service(arg):
    options = parse_options(arg)
    hostname = "localhost"
    port = 6540
    if options.get("host") is not None:
        hostname = options.get("host")
    if options.get("port") is not None:
        port = options.get("port")
    server = ServerFactory.create_server(hostname, port)
    server.start_server()

def server_stop_service():
    server = ServerFactory.create_server()
    print(f"{server.httpd.server_port}, {server.httpd.server_name}")

# main
if __name__ == '__main__':
    argv = argv[1:]
    if "--help" in argv:
        logger.info("help")
        exit(0)
    if "--version" in argv:
        logger.info("version")
        exit(0)
    if "server:start" in argv:  # start the server
        argv = argv[1:]
        server_start_service(argv)
    if "server:stop" in argv:
        server_stop_service()
    if "files:list" in argv:
        raise Exception("files:list is not implemented. ")
    if "files:add" in argv:
        raise Exception("files:add is not implemented. ")
    if "files:remove" in argv:
        raise Exception("files:remove is not implemented. ")
    else:
        logger.info("no valid command")
    exit(0)
