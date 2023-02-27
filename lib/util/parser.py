import re
import types

ALIES = {
    'port': ['P', 'port'],
    'host': ['H', 'hostname'],
    'target': ['t', 'target'],
    'source': ['s', 'source']
}

TYPES = {
    'host': 'str',
    'port': 1,
    'target': 'str',
    'source': 'str'
}


def get_name(key: str):
    for _key in ALIES:
        for alias in ALIES[_key]:
            if alias == key:
                return _key


def parse_options(options):
    # inputs  = ["--key","value","--key=value"]
    # outputs = <key,value>
    temp_options_map = {}
    for _index, key in enumerate(options):
        if key == "--verbose":
            temp_options_map["verbose"] = True
        elif key == "--silent":
            temp_options_map["silent"] = True
        elif type(re.match(r"--(\w+)$", key)) is not types.NoneType:
            key_name = get_name(key.removeprefix("--"))
            if key_name is None:
                raise Exception(f"invalid option name {key}.")
            value = options[_index + 1]
            _type = type(TYPES[key_name])
            if _type.__name__ == "int":
                # try to parse the values to int
                value = int(value)
            temp_options_map[key_name] = value
            options.pop(_index+1)
        elif type(re.match(r"-(\w+)$", key)) is not types.NoneType:
            key_name = get_name(key.removeprefix("-"))
            if key_name is None:
                raise Exception(f"invalid option name {key}.")
            value = options[_index + 1]
            _type = type(TYPES[key_name])
            if _type.__name__ == "int":
                # try to parse the values to int
                value = int(value)
            temp_options_map[key_name] = value
            options.pop(_index+1)
        elif type(re.match(r"--\w+=\w+$", key)) is not types.NoneType:
            key_name = get_name(key.split("=")[0].removeprefix("--"))
            if key_name is None:
                raise Exception(f"invalid option name {key}.")
            value = key.split("=")[1]
            _type = type(TYPES[key_name])
            if _type.__name__ == "int":
                # try to parse the values to int
                value = int(value)

            temp_options_map[key_name] = value
        else:
            raise Exception(f"invalid passed option {key}.")
    return temp_options_map
