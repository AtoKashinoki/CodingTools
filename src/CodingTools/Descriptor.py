"""
    This file contain descriptor classes.
"""

# this module

# other
from abc import ABC


""" DescriptorSkeleton """


class Skeleton(ABC):
    """
        DescriptorSkeleton

    This class is the inherited class for creating  descriptor classes.
    """

    # instance variables
    __owner: any = None
    __name: str = None

    def __set_name__(self, owner, name: str) -> None:
        """ Set owner class and variable name """
        self.__owner = owner
        self.__name = name
        return

    @property
    def owner(self) -> any: return self.__owner
    @property
    def name(self) -> str: return self.__name

    def __set__(self, instance, value: any) -> None:
        """ Set value in variable of instance """
        instance.__dict__[self.name] = value
        return

    def __get__(self, instance, owner) -> any:
        """ Get value from variable of instance """
        return instance.__dict__[self.name]

    ...
