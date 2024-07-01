"""
    This module contains tools that you can use for development.
"""

"""
    This file Initialize other file of this module.
"""

""" Import process """

""" Initialize process """

__self_name__: str = "CodingTools"

if not __name__ == __self_name__:
    raise SystemError()


try:
    from . import ErrorClass
    ...
except ImportError as e:
    ErrorClass = ImportError(e)
    ...

try:
    from . import Function
    ...
except ImportError as e:
    Function = ImportError(e)

try:
    from . import Descriptor
    ...
except ImportError as e:
    Descriptor = ImportError(e)
    ...

try:
    from . import Inheritance
    ...
except ImportError as e:
    Inheritance = ImportError(e)
    ...

try:
    from . import Decorator
    ...
except ImportError as e:
    Decorator = ImportError(e)
    ...

try:
    from . import DataType
    ...
except ImportError as e:
    DataType = ImportError(e)
    ...
