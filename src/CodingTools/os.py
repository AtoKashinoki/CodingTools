"""
    os tools

This file contains the os-relate tools for used for developing in python.
"""


""" imports """


import os
import shutil

from typing import Callable, Any

from .Function import ConsoleCaveat, caveat


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


caveat_rmtree = ConsoleCaveat.create(
    "Are you sure you want to delete {path}?",
)


def rmtree(
        _path: str,
        caveat_process: Callable[[dict[str, Any]], bool] = caveat_rmtree
) -> bool:
    """
        Remove a directory and its contents

    :return bool: True if the directory and its contents were removed.
    """
    if not os.path.isdir(_path): return False
    if not caveat_process({"path": _path}): return False
    shutil.rmtree(_path)
    return True
