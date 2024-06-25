"""
    This file contain inheritance classes.
"""

# import process
# this module
from .Descriptor import (DataType, Constant)

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
    __DESCRIPTORS: set = Constant({DataType, Constant})

    def __repr__(self):
        return self.__PRINT_DATAS.format(
            self.__class__.__name__,
            {
                key: getattr(self, key)
                for key, value in self.__class__.__dict__.items()
                if type(value) in self.__DESCRIPTORS
            }
        )
