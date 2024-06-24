"""
    Descriptors test programs
"""

from CodingTools.Descriptor import (
    Skeleton,
)


class Test:
    skeleton: str = Skeleton()

    def __init__(self):
        self.skeleton = "testSkeleton"
        return


if __name__ == '__main__':
    test = Test()
    print(test.skeleton)
    ...
