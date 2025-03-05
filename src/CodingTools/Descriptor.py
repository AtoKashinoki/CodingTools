"""
    Descriptor tools

This file contains the descriptor-related tools used for developing in Python.
"""


""" imports """


from abc import ABC, abstractmethod
from typing import Any, Callable
from copy import deepcopy

from .Inheritance import InheritanceSkeleton
from .Error.Type import ValidError


""" Skeleton """


class DescriptorSkeleton(InheritanceSkeleton):
    """ Descriptor Skeleton """

    """ Common process """
    __owner: str
    @property
    def owner(self) -> str:  return self.__owner

    __name: str
    @property
    def name(self) -> str: return self.__name

    def __set_name__(self, owner: str, name: str) -> None:
        """ Set owner and name """
        self.__owner = owner
        self.__name = name
        return

    """ local process """
    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """ Initialize descriptor """
        return

    @abstractmethod
    def __set__(self, obj: object, value: Any) -> None:
        """ Set value """
        return

    @abstractmethod
    def __get__(self, obj: object, objtype: type) -> object:
        """ Get value """
        return Any

    ...


""" Type declarations """


class Declaration(DescriptorSkeleton):
    """ Type declarations descriptor """

    """ Initializer """
    def __init__(self, *permissions: type) -> None:
        """ Initialize permission dtyp """
        self.__permissions = set(permissions)
        return

    """ permission dtype and set """
    __permissions: set[type]
    @property
    def permission(self) -> set[type]: return deepcopy(self.__permissions)

    def __set__(self, obj: object, value: Any) -> None:
        """ Validate and set value """

        if type(value) not in self.__permissions:
            raise ValidError(value)

        obj.__dict__[self.name] = value
        return

    """ get """
    def __get__(self, obj: object, objtype: type) -> object:
        """ Get value """
        return obj.__dict__[self.name]

    ...


""" Update target descriptor  """


class Update(DescriptorSkeleton):
    """ Target Update descriptors """

    """ target and name """
    __target_name: str
    __attr_name: str

    """ Initializer """

    def __init__(
            self,
            _target_name: str,
            _attr_name: str = None
    ) -> None:
        """ Create descriptor """
        self.__target_name = _target_name
        self.__attr_name = _attr_name
        return

    """ Descriptor process """

    def __set_name__(self, owner, name):
        DescriptorSkeleton.__set_name__(self, owner, name)
        if self.__attr_name is not None: return
        self.__attr_name = name
        return

    def __set__(self, obj: object, value: Any) -> None:
        obj.__dict__[self.name] = value
        target = getattr(obj, self.__target_name)
        setattr(target, self.__attr_name, value)
        return

    def __get__(self, obj: object, objtype: type) -> object:
        target = getattr(obj, self.__target_name)
        value = getattr(target, self.__attr_name)
        obj.__dict__[self.name] = value
        return value

    ...


""" Run descriptor """


class RunFunc(DescriptorSkeleton):
    """ Run function descriptor """

    """ run """
    __func: Callable[[object, Any], None]

    """ Initializer """
    def __init__(self, func: Callable[[object, Any], None]) -> None:
        """ Initialize descriptor """
        self.__func = func
        return

    """ descriptor process """
    def __set__(self, obj, value: Any) -> None:
        obj.__dict__[self.name] = value
        self.__func(obj, value)
        return

    def __get__(self, obj: object, objtype: type) -> object:
        return obj.__dict__[self.name]

    ...
