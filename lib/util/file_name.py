import os.path


def get_file_name(file: str):
    if file[-3:] == ".py":
        return os.path.basename(file).removesuffix(".py")
