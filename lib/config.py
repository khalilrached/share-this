import os
import platform
from lib.logger import LoggerBuilder

APP_NAME = "share-this"
LOG_LEVEL = "TRACE"

if platform.uname().system.lower() == "windows":  # log dir for windows
    log_path = fr"{os.environ['USERPROFILE']}\share-this"
else:
    log_path = fr"{os.environ['~']}\share-this"

# check if log folder exist
LOG_DIR = os.path.join(log_path, 'log')

if not os.path.exists(LOG_DIR):  # creating log_dir if it does not exist
    os.mkdir(LOG_DIR)

# init logger on import
LoggerBuilder.init(APP_NAME, LOG_DIR, LOG_LEVEL)

# add server path to env temporally
SERVER_HOME = os.path.dirname(os.path.dirname(__file__))
PUBLIC_SERVER_HOME = os.path.join(SERVER_HOME, "public")

os.environ.setdefault("SERVER_HOME", SERVER_HOME)
os.environ.setdefault("SERVER_PUBLIC", PUBLIC_SERVER_HOME)
