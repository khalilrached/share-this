import os
import platform
from sys import *

from lib import LoggerBuilder


# init logger
logger = LoggerBuilder.getLogger(__file__)

# main
if __name__ == '__main__':
    argv = argv[1:]
    if "--help" in argv:
        logger.info("help")
        exit(0)
    if "--version" in argv:
        logger.info("version")
        exit(0)
    if "server:start" in argv:
        raise Exception("server:start is not implemented. ")
    if "server:stop" in argv:
        raise Exception("server:stop is not implemented. ")
    if "files:list" in argv:
        raise Exception("files:list is not implemented. ")
    if "files:add" in argv:
        raise Exception("files:add is not implemented. ")
    if "files:remove" in argv:
        raise Exception("files:remove is not implemented. ")
    logger.info("no valid command")
    exit(0)
