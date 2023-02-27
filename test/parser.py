import types

from lib import *


key_test = ['H', 'h', 'hostname', 'P', 'p']
args = [
    ["--hostname=localhost", "-p", "5000"],  # --hostname=localhost -p 5000
    ["-H=localhost", "-P", "5000"],  # -H=localhost -P 5000
    ["-H", "localhost", "-P", "5000"],  # -H localhost -P 5000
    ["-s", "3245", "-P", "509"],  # -H localhost -P 5000
    ["-P", "5000", "--silent"]  # -P 5000 --silent
]


def test_parser(_arg):
    try:
        options = parse_options(_arg)
        print(f"arg: {_arg}, result: {options}")
    except Exception as ex:
        print(f"{ex}")


def test_get_name(_key,index):
    key = get_name(_key)
    print(f"#test n°:{index} [{_key} selected {key}]")


if __name__ == "__main__":
    # for index, t in enumerate(key_test):
    #     test_get_name(t, index)
    for arg in args:
        test_parser(arg)
