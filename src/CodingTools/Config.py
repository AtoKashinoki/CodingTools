"""
    Config manage tools

This file contains the Config-relate tools used for developing in Python.
"""


""" imports """


import os
from typing import KeysView

from .Definition import NULL, ALL
from .Inheritance import DataClass
from .Function import GetAttr, SetAttr


""" Constants """


CNF_FILE = ".cnf"
NOT_FOUND = "is not found"
NOT_FILE = "is not a file"
NOT_CONFIG = "is not a config file"


""" Config I/O """


class Convert(DataClass):
    """ Convert functions """

    """ Initializer """
    def __init__(
            self,
            sep: str = "\n",
            linking: str = " = ",
    ):
        """ Initialize settings """
        self.__sep = sep
        self.__linking = linking
        return

    """ settings """
    __sep: str
    @property
    def sep(self) -> str: return self.__sep

    __linking: str
    @property
    def linking(self) -> str: return self.__linking

    """ Convert functions """
    def text_to_dict(self, _text: str) -> dict | Exception:
        """ Convert text to dict """
        key: str
        value: str
        try:
            return {
                key:
                    None if value is None else
                    value[1:-1] if sum([value[i] not in ('"', "'") for i in (0, -1)]) == 0 else
                    bool(value) if value.lower() in ("true", "false") else
                    float(value) if "." in value else
                    int(value)
                for key, value in map(
                    lambda line: line.split(self.__linking.replace(" ", "")),
                    [
                        line
                        for line in _text.replace(" ", "").split(self.__sep)
                        if not line == ""
                    ]
                )
            }
        except Exception as e:
            print(f"ConfigReadError['{e.__class__.__name__}{e}']")
            return NULL(f"{e.__class__.__name__}: {e}")

    def dict_to_text(self, _dict: dict) -> str:
        """ Convert dict to text """
        return self.__sep.join(
            f"{key}{self.__linking}" + (
                f"'{value}'" if isinstance(value, str) else
                f"{value}"
            )
            for key, value in _dict.items()
        )

    ...


def validate(_path: str) -> str  | None:
    """ Validate config file """
    *parents, name = os.path.split(_path)
    # is there directory
    try: contents = os.listdir(str(os.path.join(parents[0], *parents[1:])))
    except FileNotFoundError:
        print(f"\033[31mDirectory '{_path}' is not found.\033[0m")
        return NOT_FOUND
    # is not found
    if name not in contents:
        print(f"\033[31mFile '{name}' is not found.\033[0m")
        return NOT_FOUND
    # is not file
    if not os.path.isfile(_path):
        print(f"\033[31mFile '{_path}' is not file.\033[0m")
        return NOT_FILE
    # is not config file
    if not _path[-len(CNF_FILE):] == CNF_FILE:
        print(f"\033[31mFile '{_path}' is config file.\033[0m")
        return NOT_CONFIG
    return None


def read(
        _path: str,
        converter: Convert = Convert(sep="\n", linking=" = "),
        encoding: str = "utf-8"
) -> dict | NULL:
    """ Read config file """

    """ Validate """
    result = validate(_path)
    name = os.path.split(_path)[-1]
    if result is not None:
        if result == NOT_FOUND:
            return NULL(f"'{name}' is not found.")
        if result == NOT_FILE:
            return NULL(f"'{name}' is not a file.'")
        if result == NOT_CONFIG:
            return NULL(f"'{name}' is not a config file.")
        ...

    """ Read file """
    with open(_path, "r", encoding=encoding) as cnf_file:
        cnf_text = cnf_file.read()
        ...

    """ Convert text to dict """
    config = converter.text_to_dict(cnf_text)

    return config


def write(
        _path: str,
        _config: dict,
        converter: Convert = Convert(sep="\n", linking=" = "),
        encoding: str = "utf-8"
) -> bool:
    """ Write config file """

    """ Validate NULL """
    if not isinstance(_config, dict): return False

    """ Convert dict to text """
    text = converter.dict_to_text(_config)

    """ Write text in config file """
    try:
        with open(_path, "w", encoding=encoding) as cnf_file:
            cnf_file.write(text)
            ...
        ...
    except FileNotFoundError:
        print(f"\033[31mFile '{_path}' is not found.\033[0m")
        return False

    return True


""" Config manager """


class ConfigManager(object):
    """ Config manager """

    """ Initializer """
    def __init__(
            self,
            _path: str,
            converter: Convert = Convert(sep="\n", linking=" = "),
            encoding: str = "utf-8",
    ):
        """ Initialize settings """

        """ Settings and file """
        self.__path = _path
        self.__converter = converter
        self.__encoding = encoding

        """ Get data """
        config = read(_path, converter=converter, encoding=encoding)
        if isinstance(config, NULL):
            print(f"\033[31mFile '{_path}' create.\033[0m")
            result = write(
                _path, {}, converter=converter, encoding=encoding
            )
            if not result: raise FileNotFoundError(f"'{self.__path}' not found.")
            config = read(_path, converter=converter, encoding=encoding)
            ...
        self.__data = config
        return

    """ Settings """
    __converter: Convert
    @property
    def converter(self) -> Convert:  return self.__converter
    __encoding: str
    @property
    def encoding(self) -> str: return self.__encoding

    """ Config data """
    __data: dict
    @property
    def data(self) -> dict: return self.__data

    def __setitem__(
            self,
            key: str,
            value: str | int | float | bool
    ) -> None:
        """ Set key and value """
        self.__data[key] = value
        return

    def __getitem__(
            self,
            key: str
    ) -> str | int | float | bool:
        """ Get key value """
        return self.__data[key]

    def __eq__(self, other):
        """ Equal """
        if isinstance(other, ConfigManager):
            return self.__data == other.__data
        if isinstance(other, dict):
            return self.__data == other
        return NotImplemented

    def item(self):
        """ Get item """
        return self.__data.items()

    def keys(self):
        """ Get keys """
        return self.__data.keys()

    def values(self):
        """ Get values """
        return self.__data.values()

    def __iter__(self):
        """ Iterate """
        return self.__data.__iter__()

    """ Config file """
    __path: str
    @property
    def path(self) -> str: return self.__path

    def load(self) -> NULL | None:
        """ Load config file """
        result = read(self.path)
        if result is NULL: return result
        self.__data = result
        return None

    def save(self) -> bool:
        """ Save config file """
        result = write(self.path, self.__data, converter=self.__converter)
        return result

    """ Attr set and get """
    def getattr(
            self,
            _target: object,
            keys: tuple[str] | list[str] | str | ALL | KeysView = ALL,
    ) -> None:
        """ Get attribute """
        """ keys """
        if keys is ALL: keys = self.__data.keys()

        """ get values """
        values = GetAttr.keys(_target, keys)

        """ set value """
        for key, value in zip(keys, values):
            self.__data[key] = value
            continue

        return

    def setattr(
            self,
            _target: object,
            keys: tuple[str] | list[str] | str | ALL | KeysView = ALL,
    ) -> None:
        """ Set attribute """

        """ keys """
        if keys is ALL: keys = self.__data.keys()

        """ assignment values """
        assign_value: dict[str, str | int | float | bool] = {
            key: value
            for key, value in self.__data.items()
            if key in keys
        }

        """ set values """
        SetAttr.dict(_target, assign_value)

        return

    """ Debug """
    def __repr__(self):
        """ print text """
        if isinstance(self.__data, NULL):
            return f"ConfigNULL['{self.__data}']"
        return f"Config{self.__data}"

    ...
