"""
    Inheritance tools

This file contains the inheritance-related tools used for developing in Python.
"""


""" imports """


from abc import ABC, abstractmethod
from typing import Any

from .Error.Attribute import DefinedError


""" Skeleton """


class InheritanceSkeleton(ABC):
    """ Inheritance Skeleton """


""" Data class """


class DataClass(InheritanceSkeleton):
    """ DataClass Skeleton """

    """ access values """

    def __get_accessible_keys(self) -> tuple:
        """ validate and return keys """
        return tuple(
            key
            for key in (
                *self.__class__.__dict__.keys(),
                *self.__dict__.keys(),
            )
            if key[0] != "_"
        )

    def __validate_attribute(self, key: str) -> None:
        """ Validate attribute """
        if key not in self.__get_accessible_keys():
            raise DefinedError(key)
        return

    def __getitem__(self, key: str):
        """ Access and get value """
        self.__validate_attribute(key)
        return getattr(self, key)

    def __setitem__(self, key: str, value: Any):
        """ Access and set value """
        self.__validate_attribute(key)
        setattr(self, key, value)
        return

    """ debug """

    def __repr__(self):
        values: dict[str, Any] = {
            key: getattr(self, key)
            for  key in self.__get_accessible_keys()
        }
        return f"{self.__class__.__name__}{values}"

    ...
