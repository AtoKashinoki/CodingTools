"""
    This file contain inheritance classes.
"""

# import process
# this module
from .Descriptor import (DataType, Constant)

# other
from abc import (ABC, abstractmethod)


""" DataClassInheritanceClass """


def protect_member(instance, key: str) -> str:
    """
        Generate protect member.
    :param instance: class instance.
    :param key: variable name.
    :return: protect member key.
    """
    return "_" + instance.__class__.__name__ + key


def get_variable_name(instance, key) -> str:
    """
    Check protect member and Return variable name.
    :param instance: class instance.
    :param key: variable name.
    :return: variable name key.
    """
    if key[:2] == "__":
        return protect_member(instance, key)
    return key


class DataClass(ABC):
    """
        DataClass inheritance class.

    This class is inheritance class.
    The class manage datas and descriptors.
    """

    # constant variables
    __PRINT_DATAS: str = Constant("{}{}")
    __DESCRIPTORS: set[type] = Constant({DataType, Constant})

    def set_values(self, **kwargs):
        """
            Initialize datas.
        :param kwargs: key -> value name : value to assign.
        """
        [
            setattr(
                self,
                get_variable_name(self, key),
                value
            )
            for key, value in kwargs.items()
        ]
        return

    def __repr__(self):
        return self.__PRINT_DATAS.format(
            self.__class__.__name__,
            {
                key: getattr(self, key)
                for key, value in self.__class__.__dict__.items()
                if type(value) in self.__DESCRIPTORS
            }
        )
