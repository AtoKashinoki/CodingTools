"""
    Inheritance classes test process.
"""

from CodingTools.Descriptor import (DataType, Constant)
from CodingTools.Inheritance import DataClass


class DataClassTest(DataClass):
    test1: str = DataType(str)
    test2: str = Constant("test2")
    ...


class Test:
    test_datas: DataClassTest = Constant(DataClassTest())

    def __init__(self):
        self.test_datas.test1 = "test1"
        # self.test_datas.test1 = 1
        # self.test_datas.test2 = ""
        return


if __name__ == '__main__':
    test = Test()
    print(test.test_datas)
    ...
