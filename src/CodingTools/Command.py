"""
    Command tools

This file contains the command-related tools used for developing in Python.
"""
from idlelib.undo import Command

""" imports """


import sys
from abc import abstractmethod
from typing import Any

from .Inheritance import InheritanceSkeleton
from .Wrapper import initialize


""" Command Skeleton """


class CommandSkeleton(InheritanceSkeleton):
    """ Command class skeleton """

    """ Initialize  """
    def __init__(self, help_message: str = None):
        """ Initialize method """
        self.__name = self.__class__.__name__
        self.__help: Help = (
            Help(help_message)
            if help_message is not None else
            None
        )
        return

    """ name """
    __name: str
    @property
    def name(self) -> str: return self.__name

    """ help command """
    @property
    def help(self): return self.__help

    """ Command process """
    @abstractmethod
    def __command__(self, argv: tuple[str, ...]) -> Any | None: ...

    """ Call command """
    def __call__(self, argv: tuple[str] = tuple(sys.argv)) -> Any | None:
        """ Call command """
        return self.__command__(tuple(argv))

    """ debug """

    ...


class Help(CommandSkeleton):
    """ Help command """

    """ Initializer """
    def __init__(self, message: str):
        super().__init__()
        self.__message = message
        return

    """ message """
    __message: str
    @property
    def message(self) -> str: return self.__message

    """ command """
    def __command__(self, argv: tuple[str, ...]) -> Any | None:
        """ Display help message """
        print(self.__message)
        return

    """ debug """
    def __repr__(self) -> str:
        return self.__message

    ...


""" CodingTools command """


@initialize(
    ()
)
class CodingTools(CommandSkeleton):
    """ CodingTools command """

    __help_massage__: str = (
        "Test"
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

        """ validate and run command """
        for command in (*self.__commands, self.help):
            if not command_argv[0] == command.name:
                continue

            result = command()
            break

        else:
            self.help()
            ...

        return None

    ...
