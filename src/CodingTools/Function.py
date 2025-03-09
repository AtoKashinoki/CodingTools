"""
    Function tools

This file contains the Function-relate tools used for developing in Python.
"""


""" imports """


from typing import Callable, Any, KeysView
from .Error.Other import CancelledError

from .Inheritance import DataClass

import os


"""
    Functions
"""


""" Caveat functions """


class ConsoleCaveat(DataClass):
    """ Functions about caveat """

    """ Constants """
    ANNOTATION: type = Callable[[dict[str, Any]], bool]

    class Message:
        """ Caveatting message """
        ALREADY_EXISTS: str ="'{path}' already exists.\nOverwrite it?"
        ...

    """ Function tools """

    @staticmethod
    def create(
            message: str = "Are you sure?",
            choices: dict[str, bool] = {"Y": True, "n": False}
    ) -> Callable[[dict[str, Any]], bool]:
        """ Create function that caveat in console. """

        def caveat(formats: dict[str, Any] = {}) -> bool:
            """
                Caveat function
            :return bool: True if the user was approved.
            """
            user_reply = input(
                f"{message.format(**formats)} "
                f"[{'|'.join(choices.keys())}]: ")
            if not user_reply in choices:
                return False
            return choices[user_reply]

        return caveat

    ...


""" Validators """

""" Validate function """


class Validator:
    """ Validate functions """

    """ Validators """
    @staticmethod
    def extension(
            name: str,
            extension: str,
            **kwargs: Any,
    ) -> TypeError | None:
        """ Validate extension """
        if not name.split(".")[-1] == extension:
            return TypeError(
                "File '{}' is not a extension of meta file.".format(name),
            )
        return None

    @staticmethod
    def path_is_file(
            file_path: str,
            **kwargs: Any,
    ) -> FileNotFoundError | None:
        """ Validate path is a file """
        if not os.path.isfile(file_path):
            return FileNotFoundError(
                "Path '{}' is not found.".format(file_path)
            )
        return None

    @staticmethod
    def exists(
            file_path: str,
            exists_caveat: ConsoleCaveat.ANNOTATION,
            **kwargs: Any,
    ) -> IsADirectoryError | CancelledError | None:
        """ Validate exists file """
        if os.path.exists(file_path):

            # is not file
            if not os.path.isfile(file_path):
                return IsADirectoryError(
                    "Path '{}' is not a file.".format(file_path)
                )

            # exists file
            if not exists_caveat({"path": file_path}):
                return CancelledError("Writing of metafile")

            ...

        return None

    """ Validate execute """

    @staticmethod
    def execute(
            _validators: list[Callable],
            **kwargs: Any,
    ) -> Exception | None:
        """ validate path function of reading meta """
        for validator in _validators:
            result = validator(**kwargs)
            if result is not None: return result
        return None

    ...


""" Assignment and Get function """


class SetAttr:
    """ Functions about assignment """

    @staticmethod
    def dict(_target: object, _dict: dict) -> None:
        """ Assignment dictionary datas in target """
        for key, value in _dict.items():
            setattr(_target, key, value)
            continue
        return None

    ...


class GetAttr:
    """ Functions about get """

    @staticmethod
    def keys(
            _target: object,
            _keys: tuple[str] | list[str] | KeysView[str]
    ) -> tuple[Any, ...]:
        """ Get value from target """
        return tuple(
            getattr(_target, key)
            for key in _keys
        )

    ...
