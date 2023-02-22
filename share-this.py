import os
import platform
import sys

from lib import Logger

if platform.uname().system.lower() == "windows":  # log dir for windows
    log_path = fr"{os.environ['USERPROFILE']}\share-this"
else:
    log_path = fr"{os.environ['~']}\share-this"

# check if log folder exist
log_dir = os.path.join(log_path, 'log')

if not os.path.exists(log_dir):  # creating log_dir if it does not exist
    os.mkdir(log_dir)

Logger.init(os.path.basename(__file__).removesuffix(".py"), log_dir)
# init logger
logger = Logger()

# main
if __name__ == '__main__':
    logger.info("welcome")
