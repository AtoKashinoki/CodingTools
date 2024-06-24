"""
    Descriptors test programs
"""

from CodingTools.Descriptor import (
    Skeleton,
    DataType,
)


class Test:
    skeleton: str = Skeleton()
    data_type: str = DataType(str)

    def __init__(self):
        self.skeleton = "testSkeleton"
        self.data_type = "testDataType"
        return


if __name__ == '__main__':
    test = Test()
    print(test.skeleton)
    print(test.data_type)
    ...
