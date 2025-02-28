"""
    os tools

This file contains the os-relate tools for used for developing in python.
"""


""" imports """


import os


""" os processes """


def mkdir(_path: str) -> bool:
    """
        Make directory
    :return bool: True if the directory was created.
    """
    if os.path.exists(_path): return False
    os.mkdir(_path)
    return True
