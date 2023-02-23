import os
from lib.util import *

Default = "\033[39m"
Black = "\033[30m"
Red = "\033[31m"
Green = "\033[32m"
Yellow = "\033[33m"
Blue = "\033[34m"
Magenta = "\033[35m"
Cyan = "\033[36m"
LightGray = "\033[37m"
DarkGray = "\033[90m"
LightRed = "\033[91m"
LightGreen = "\033[92m"
LightYellow = "\033[93m"
LightBlue = "\033[94m"
LightMagenta = "\033[95m"
LightCyan = "\033[96m"
White = "\033[97m"


class LoggerBuilder:
    @staticmethod
    def getLogger(class_name: str):
        return Logger(class_name)

    @staticmethod
    def init(app_name, log_dir, level="INFO"):
        LoggerBuilder.set_app_name(app_name)
        LoggerBuilder.set_log_path(log_dir)
        LoggerBuilder.set_level(level)

    @staticmethod
    def set_app_name(name):
        Logger.APP_NAME = name

    @staticmethod
    def set_level(level):
        Logger.LEVEL = level

    @staticmethod
    def set_log_path(_dir):
        if not os.path.isdir(_dir):
            raise Exception(f"{_dir} is not a directory.")
        file_name = f"{toDay()}_{Logger.APP_NAME}.log"
        Logger.LOG_PATH = os.path.join(_dir, file_name)


class Logger:
    LEVEL = ""
    LOG_PATH = ""
    APP_NAME = ""

    def __init__(self, class_name):
        if self.LOG_PATH == "":
            raise Exception("log path is not defined.\nuse Logger.set_log_path.")
        self.CONSOLE_FORMAT = "[{date}] [{appname}] [" + class_name + "] {color}[{level}]: {message} " + Default
        self.FILE_FORMAT = "[{date}] [{appname}] [" + class_name + "] [{level}]: {message} "
        if os.path.exists(self.LOG_PATH):
            # write on the same file
            self.__log_file = open(self.LOG_PATH, 'a')
            self.trace(f"log file already exist in => ( {self.LOG_PATH} )")
        else:
            # create new file
            self.__log_file = open(self.LOG_PATH, 'w')
            self.trace(f"creating new log file => ( {self.LOG_PATH} )")
        if self.APP_NAME == "":
            self.warn("app name is null.")

    def crash(self):
        pass

    def error(self, message):
        console = self.CONSOLE_FORMAT.format(date=time_now(), appname=self.APP_NAME, level="ERROR", color=Red,
                                             message=message)
        print(console)
        log = self.FILE_FORMAT.format(date=time_now(), appname=self.APP_NAME, level="ERROR", message=message)
        self.__log_file.write(f"{log}\n")

    def warn(self, message):
        if self.LEVEL in ['DEBUG', 'TRACE', 'INFO', 'WARN']:
            log = self.CONSOLE_FORMAT.format(date=time_now(), appname=self.APP_NAME, level="WARN", color=Yellow,
                                             message=message)
            print(log)
        log = self.FILE_FORMAT.format(date=time_now(), appname=self.APP_NAME, level="WARN", message=message)
        self.__log_file.write(f"{log}\n")

    def info(self, message):
        if self.LEVEL in ['DEBUG', 'TRACE', 'INFO', ]:
            log = self.CONSOLE_FORMAT.format(date=time_now(), appname=self.APP_NAME, color=Blue, level="INFO",
                                             message=message)
            print(log)
        log = self.FILE_FORMAT.format(date=time_now(), appname=self.APP_NAME, level="INFO", message=message)
        self.__log_file.write(f"{log}\n")

    def debug(self, message):
        if self.LEVEL in ['DEBUG', 'TRACE', ]:
            log = self.CONSOLE_FORMAT.format(date=time_now(), appname=self.APP_NAME, color=Green, level="DEBUG",
                                             message=message)
            print(log)
        log = self.FILE_FORMAT.format(date=time_now(), appname=self.APP_NAME, level="DEBUG", message=message)
        self.__log_file.write(f"{log}\n")

    def trace(self, message):
        if self.LEVEL == "TRACE":
            log = self.CONSOLE_FORMAT.format(date=time_now(), appname=self.APP_NAME, color=Cyan, level="TRACE",
                                             message=message)
            print(log)
        log = self.FILE_FORMAT.format(date=time_now(), appname=self.APP_NAME, level="TRACE", message=message)
        self.__log_file.write(f"{log}\n")
