"""
    Other error systems

This file contains the OtherError-relate tools.
"""


""" imports """


from CodingTools.Error.Skeleton import ErrorSkeleton, gen_skeleton


"""
    Other error systems
"""


Exception = gen_skeleton(Exception)


""" Cancelled """


class DirNotFoundError(Exception):
    """ Directory not found """

    __message__ = "Path '{path}' is not found."

    def __init__(self, _path: str) -> None:
        """ Initial message """
        super().__init__(path=_path)
        return

    ...


class CancelledError(Exception, ErrorSkeleton):
    """ Processes cancelled """

    __message__ = "{process} was cancelled."

    def __init__(self, _process: str) -> None:
        """ Initial message """
        super().__init__(process=_process)
        return

    ...
