# read directory recursively
# compress all files in one directory with the name of the current directory
# move and remove files/directory
import os.path
import shutil
import webbrowser

from lib import LoggerBuilder,time_now

logger = LoggerBuilder.getLogger(os.path.basename(__file__).removesuffix(".py"))


def time_now_name():
    return time_now().replace('-', '_')


def compress_directory(_dir: str) -> str | None:
    if not os.path.isabs(_dir):
        _dir = os.path.abspath(_dir)
    logger.info(f"compressing {_dir}")
    # check if _dir exist
    if not os.path.exists(_dir):
        logger.error(f"cannot compress [{_dir}]. does not exist.")
        return
    if not os.path.isdir(_dir):
        logger.error(f"cannot compress [{_dir}]. is not valid directory")
        return
    # check if uploads exist in public
    uploads_dir = os.path.join(os.environ["SERVER_HOME"], "public", "uploads")
    if not os.path.exists(uploads_dir):  # create uploads folder under public
        os.mkdir(uploads_dir)
    folder_name = os.path.basename(_dir)
    shutil.make_archive(root_dir=_dir, base_name=folder_name, format='zip')
    move = shutil.move(f"{folder_name}.zip", os.path.join(uploads_dir, f"{folder_name}_{time_now_name()}.zip"))
    return move
