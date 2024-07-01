"""
    This file contain function tools.
"""


""" about protect member """


def protect_member(cls, key: str) -> str:
    """
        Generate protect member.
    :param cls: class type.
    :param key: variable name.
    :return: protect member key.
    """
    return "_" + cls.__name__ + key


def get_variable_name(cls, key) -> str:
    """
    Check protect member and Return variable name.
    :param cls: class type.
    :param key: variable name.
    :return: variable name key.
    """
    if key[:2] == "__":
        return protect_member(cls, key)
    return key


""" about validate dtype """


def validate_dtype(target: any, dtypes: set[type]) -> bool:
    """
        Validate target with dtype.
    :param target: value to validate with dtypes.
    :param dtypes: dtypes to permission.
    :return: Results of the validating.
    """
    if any in dtypes:
        return True

    if target is None and None in dtypes:
        return True

    return type(target) in dtypes
