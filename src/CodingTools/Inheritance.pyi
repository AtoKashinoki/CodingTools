
from abc import (ABC, abstractmethod)


class DataClass(ABC):
    __PRINT_DATAS: str
    __DESCRIPTORS: set[type]

    def __set_values__(self, **kwargs) -> None: ...
    def __repr__(self) -> str: ...

    ...
