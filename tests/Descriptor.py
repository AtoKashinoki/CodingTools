"""
    Descriptors test programs
"""

from CodingTools.Descriptor import (
    Skeleton,
    DataType,
    Constant,
)


class Test:
    skeleton: str = Skeleton()
    data_type: str = DataType(str)
    constant: str = Constant("testConstant")

    def __init__(self):
        self.skeleton = "testSkeleton"
        self.data_type = "testDataType"
        # self.constant = ""
        return


if __name__ == '__main__':
    test = Test()
    print(test.skeleton)
    print(test.data_type)
    print(test.constant)
    ...
