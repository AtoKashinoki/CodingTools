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


class ALL(object):
    """ ALL object """
    ...


class Default(object):
    """ Default object """
    ...


class NULL(Exception):
    """ NULL object """
    __message: str
    @property
    def message(self) -> str: return self.__message
    __error: Exception
    @property
    def error(self) -> Exception: return self.__error

    def __init__(self, _error: str | Exception) -> None:
        """ Initialize message """
        Exception.__init__(
            self,
            f"NULL[{_error.__class__.__name__}: {_error}]"
        )
        self.__error = _error
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
