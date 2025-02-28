"""
    os tools

This file contains the os-relate tools for used for developing in python.
"""


""" imports """


import os
import shutil

from typing import Callable


""" os processes """

""" directory """


def mkdir(_path: str) -> bool:
    """
        Make directory
    :return bool: True if the directory was created.
    """
    if os.path.exists(_path): return False
    os.mkdir(_path)
    return True


def caveat_rmtree() -> bool:
    """
        Caveat from rmtree
    :return bool: True if the user was approved.
    """
    if not input("Are you sure you want to delete it? [Y|n]: ") in ("Y", ):
        return False
    return True


def rmtree(
        _path: str,
        caveat_process: Callable[[], bool] = caveat_rmtree
) -> bool:
    """
        Remove a directory and its contents

    :return bool: True if the directory and its contents were removed.
    """
    if not caveat_process():
        return False
    shutil.rmtree(_path)
    return True
