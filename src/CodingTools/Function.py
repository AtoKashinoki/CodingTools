"""
    Function tools

This file contains the Function-relate tools used for developing in Python.
"""


""" imports """


from typing import Callable, Any, KeysView

from CodingTools.Inheritance import DataClass


"""
    Functions
"""


""" Caveat functions """


class ConsoleCaveat(DataClass):
    """ Functions about caveat """

    class Message:
        """ Caveatting message """
        ALREADY_EXISTS: str ="'{path}' already exists.\nOverwrite it?"
        ...

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
