"""
    This file contain inheritance classes.
"""

# import process
# this module
from .Descriptor import (DataType, Constant)
from .Function import get_variable_name

# other
from abc import (ABC, abstractmethod)


""" DataClassInheritanceClass """


class DataClass(ABC):
    """
        DataClass inheritance class.

    This class is inheritance class.
    The class manage datas and descriptors.
    """

    # constant variables
    __PRINT_DATAS: str = Constant("{}{}")
    __DESCRIPTORS: set[type] = Constant({DataType, Constant})

    def __set_values__(self, **kwargs):
        """
            Initialize datas.
        :param kwargs: key -> value name : value to assign.
        """
        [
            setattr(
                self,
                get_variable_name(self.__class__, key),
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
