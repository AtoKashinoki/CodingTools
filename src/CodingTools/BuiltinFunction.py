"""
     CodingTools builtin

This file contains the CodingToolsBuiltin-relate tools.
"""


""" imports """


from .Function import ConsoleCaveat as ConsoleCaveatTools


"""
    Builtins
"""


""" """


class ConsoleCaveat:
    """ Builtin console caveats """

    already_exists = ConsoleCaveatTools.create(
        ConsoleCaveatTools.Message.ALREADY_EXISTS
    )

    ...