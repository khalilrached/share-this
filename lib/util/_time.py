import time


def toDay():
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def time_now():
    return time.strftime('%H-%M-%S', time.localtime(time.time()))