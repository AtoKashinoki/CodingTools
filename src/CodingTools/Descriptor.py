"""
    This file contain descriptor classes.
"""

# import process
# this module
from .ErrorClass import AssignmentError
from .Function import validate_dtype

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


""" DataType Validator"""


class DataType(Skeleton):
    """
        DataTypeValidator

    This class is descriptor class.
    The class validates the data type of the Value.
    """

    # instance variables
    __permission: set[type or any or None] = None

    # constant variables
    __PERMISSION_MESSAGE: str = \
        "Not match permission dtypes -> {}({})"

    def __init__(self, *permission_dtypes: type | None):
        """
            Initialize permission dtypes and settings.
        :param permission_dtypes: The dtypes you want to allow.
        """
        if len(permission_dtypes) == 0:
            self.__permission = {any, None}
            ...
        else:
            self.__permission = set(permission_dtypes)
            ...

        return

    @property
    def permission(self) -> tuple: return tuple(self.__permission)

    def __set__(self, instance, value: any) -> None:
        # validate process
        if not validate_dtype(value, self.__permission):
            raise AssignmentError(
                self.__PERMISSION_MESSAGE.format(value, type(value))
            )

        # set process
        super().__set__(instance, value)
        return

    ...


""" Constant descriptor """


class Constant(Skeleton):
    """
        ConstantDescriptor

    This class is descriptor class.
    The class validates Assignment values.
    """

    # instance variables
    __value: any = None

    # constant variables
    __NOT_ASSIGNABLE_MESSAGE: str = \
        "Not assignable -> {}.{}"

    def __init__(self, constant_value: any):
        """
            Initialize constant value.
        :param constant_value: value to assign.
        """
        self.__value = constant_value
        return

    def __set__(self, instance, value: any) -> None:
        """ Not assignable """
        raise AssignmentError(
            self.__NOT_ASSIGNABLE_MESSAGE.format(
                self.owner.__name__, self.name
            )
        )

    def __get__(self, instance, owner) -> any:
        """ Get constant value """
        return self.__value

    ...
