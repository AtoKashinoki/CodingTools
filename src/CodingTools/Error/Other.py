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


class CancelledError(Exception, ErrorSkeleton):
    """ Processes cancelled """

    __message__ = "{process} was cancelled."

    def __init__(self, _process: str) -> None:
        """ Initial message """
        super().__init__(process=_process)
        return

    ...
