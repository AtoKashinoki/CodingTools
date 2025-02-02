"""
    Attribute error tools

This file contains AttributeError-related tools used for developing in Python.
"""


""" imports """


""" Error """


class DefinedError(AttributeError):
    """ Attribute define error """

    """ message """
    message: str = (
        "name '{name}' is not defined."
    )

    def __init__(self, name: str):
        """ Initialize message """
        super().__init__(
            self.message.format(
                name=name,
            )
        )
        return

    ...
