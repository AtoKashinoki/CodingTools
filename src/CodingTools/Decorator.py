"""
    This file contain decorator classes.
"""

# import process
# this module

# other
from abc import (ABC, abstractmethod)


""" DecoratorSkeleton """


class Skeleton(ABC):
    """
        DecoratorSkeleton

    This class is inheritance class for creating decorator classes.
    """

    @abstractmethod
    def __init__(self, *args, **kwargs): ...
    @abstractmethod
    def __call__(self, *args, **kwargs): ...

    ...
