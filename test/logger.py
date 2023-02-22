from lib import Logger


def test_path():
    Logger.init("test-app", r"C:\Users\Zoro\Desktop\www\share-this\log")
    logger = Logger("TRACE")
    logger.error("error")
    logger.warn("warn")
    logger.info("info")
    logger.debug("hello world")
    logger.trace("trace")


if __name__ == "__main__":
    try:
        test_path()
    except Exception as ex:
        print(ex.with_traceback())
