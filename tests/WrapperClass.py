import functools

from CodingTools.Wrapper import Wrapper, classtools_wraps
from typing import Callable


@Wrapper
def initialize(*args, **kwargs):

    if (
        isinstance(args[0], Callable) and
        len(args)+len(kwargs) == 1
    ):
        print("!")
        return args[0]()

    def wrapper(_target):
        return _target(*args, **kwargs)

    return wrapper



def wrap(_target):

    @classtools_wraps(_target)
    class WrapperClass(_target):
        """ test """

        def __init__(self):
            print("WrapperC")
            return

        ...

    return WrapperClass

@wrap
class Target:
    """ Target """

    def __init__(self, *args, **kwargs):
        return

    ...


if __name__ == '__main__':
    print(Target)
    ...
