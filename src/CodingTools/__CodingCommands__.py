"""
    Coding commands

This file contains the CodingCommand-relate tools used for developing in Python.
"""


""" imports """


from typing import Any

from .Wrapper import initialize
from .Command import CommandSkeleton


"""  commands """


""" CodingTools command """


@initialize(
    ()
)
class CodingTools(CommandSkeleton):
    """ CodingTools command """

    __help_massage__: str = (
        "CodingTools command help\n"
        "   CodingTools [Command] [options]\n"
        "\n"
        "   Command\n"
        "       [Help] or [-h]\n"
        "       Print help of CodingTools command\n"
    )

    """ Initialize """
    def __init__(self, commands: tuple[CommandSkeleton, ...]):
        """ Initialize command list """
        super().__init__(self.__help_massage__)
        self.__commands = commands
        return

    """ command list """
    __commands: tuple[CommandSkeleton, ...]
    @property
    def commands(self) -> tuple[CommandSkeleton, ...]:
        return self.__commands

    """ command process """
    def __command__(self, argv: tuple[str, ...]) -> Any | None:
        """ Access process """
        command_argv = argv[1:]
        if len(command_argv) == 0:
            self.help()
            return None

        """ validate and run command """
        for command in (*self.__commands, self.help):
            if not command_argv[0] in command.names:
                continue

            result = command()
            if result is not None: print(result)

            break

        else:
            print(f"Command '{command_argv[0]}' is not found.")
            self.help()
            ...

        return None

    ...