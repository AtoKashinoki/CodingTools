

from CodingTools.Inheritance import DataClass


class TestDataClass(DataClass):
    """
        Test data class
    """
    
    test1 = "test1"
    test2 = "test2"
    __test6 = "test6"
    _test7 = "test7"

    def __init__(self):
        """ initializer """
        self.test3 = "test3"
        self.test4 = "test4"
        self.__test5 = "test5"
        self._test8 = "test8"
        return

    ...


if __name__ == "__main__":
    test = TestDataClass()
    test.test9 = "test9"
    print(test)
    test2 = DataClass()
    test2.test10 = "test10"
    print(test2)
    ...
