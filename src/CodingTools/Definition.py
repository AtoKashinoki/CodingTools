"""
    Coordinate definitions

This file contains coordinate definitions used for developing in Python.
"""


""" imports """


from .Inheritance import DataClass


"""
    Definitions
"""


""" System """


class NULL(Exception):
    """ NULL object """
    __message: str
    @property
    def message(self) -> str: return self.__message

    def __init__(self, _message: str | object = "NULL") -> None:
        """ Initialize message """
        Exception.__init__(self, _message)
        return

    ...


""" Coordinate """


class Coordinate(DataClass):
    """ Coordinate definitions """

    class IDX(DataClass):
        """ Coordinate list index definitions """
        X, Y, Z = range(3)
        ...

    ...
