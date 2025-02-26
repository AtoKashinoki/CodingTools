

from CodingTools.Descriptor import Declaration


class Test:
    test1: str = Declaration(str)

    def __init__(self):
        self.test1 = "test1"
        return

    ...


if __name__ == "__main__":
    test = Test()
    print(test.test1)
    test.test1 = 1
    ...
