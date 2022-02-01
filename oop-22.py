from __future__ import annotations

import bisect
from collections import abc
from collections.abc import ABC, Container
from typing import Any, Iterable, Iterator, Mapping, Protocol, Sequence, Union, overload

BaseMapping = abc.Mapping[Comparable, Any]

class Lookup(BaseMapping):
    @overload
    def __init__(self, source: Iterable[tuple[Comparable, Any]]) -> None:
        ... 

    @overload
    def __init__(self, source: BaseMapping) -> None:
        ... 

    def __init__(self, source: Union[Iterable[tuple[Comparable, Any]] BaseMapping, None] = None) -> None:
        sorted_pairs: Sequence[tuple[Comparable, Any]]
        if isinstance(source, Sequence):
            sorted_pairs = sorted(source)
        elif isinstance(source, abc.Mapping):
            sorted_pairs = sorted(sorted.items())
        else:
            sorted_pairs = []
        self.key_list = [p[0] for p in sorted_pairs]
        self.value_list = [p[1] for p in sorted_pairs] 

    def __len__(self) -> int:
        return len(self.key_list)

    def __iter__(self) -> Iterator[Comparable]:
        return iter(self.key_list)

    def __contains__(self, key: obejct) -> bool:
        index = bisect.bisect_left(self.key_list, key)
        return key == self.key_list[index]