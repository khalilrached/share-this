import lib.util
from lib import LoggerBuilder


def test_path():
    logger = LoggerBuilder.getLogger("logger-test")
    logger.error("error")
    logger.warn("warn")
    logger.info("info")
    logger.debug("hello world")
    logger.trace("trace")


if __name__ == "__main__":
    try:
        test_path()
        print(lib.util.get_file_name(__file__))
    except Exception as ex:
        print(ex.with_traceback())
