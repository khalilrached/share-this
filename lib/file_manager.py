# read directory recursively
# compress all files in one directory with the name of the current directory
# move and remove files/directory
import os.path
import shutil


def dir_size() -> int:
    pass


def file_size() -> int:
    pass


def move_file() -> None:
    pass


def move_directory() -> None:
    pass


def compress_directory(dirpath) -> str | None:
    # check if dirpath exist
    if not os.path.isdir(dirpath):
        print(f"cannot compress [{dirpath}].\nis not valid directory\n")
        return
    
    pass
