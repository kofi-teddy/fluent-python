from contextlib import contextmanager
from types import TracebackType
from typing import List, Literal, Optional, Type


class StringJoiner(List[str]):
    def __enter__(self) -> 'StringJoiner':
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType],) -> Literal[False]:
        self.result = ''.join(self)
        return False


class StringJoiner2(List[str]):
    def __init__(self, *args: str) -> None:
        super().__init__(*args)
        self.result = ''.join(self)


@contextmanager
def joiner(*args: Any) -> Iterator[StringJoiner2]:
    string_list = StringJoiner2(args)
    try:
        yield string_list
    finally:
        string_list.result = ''.join(string_list)
        

