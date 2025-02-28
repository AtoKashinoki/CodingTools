"""
    Function tools

This file contains the Function-relate tools used for developing in Python.
"""


""" imports """


from typing import Callable


"""
    Functions
"""


""" Caveat functions """


class ConsoleCaveat:
    """ Functions about caveat """

    @staticmethod
    def create(
            message: str = "Are you sure?",
            choices: dict[str, bool] = {"Y": True, "n": False}
    ) -> Callable[[], bool]:
        """ Create function that caveat in console. """

        def caveat() -> bool:
            """
                Caveat function
            :return bool: True if the user was approved.
            """
            user_reply = input(f"{message} [{'|'.join(choices.keys())}]: ")
            if not user_reply in choices:
                return False
            return choices[user_reply]

        return caveat
    
    ...
