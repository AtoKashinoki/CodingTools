"""
    os tools

This file contains the os-relate tools for used for developing in python.
"""


""" imports """


import os
import shutil

from typing import Callable

from .Function import ConsoleCaveat


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


caveat_rmtree: Callable[[], bool] = ConsoleCaveat.create(
    "Are you sure you want to delete it?",
)


def rmtree(
        _path: str,
        caveat_process: Callable[[], bool] = caveat_rmtree
) -> bool:
    """
        Remove a directory and its contents

    :return bool: True if the directory and its contents were removed.
    """
    if not os.path.isdir(_path): return False
    if not caveat_process(): return False
    shutil.rmtree(_path)
    return True
