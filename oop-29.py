from __future__ import annotations

import operator
import datetime
import string
from dataclasses import dataclass
from functools import total_ordering
from pprint import pprint
from sqlite3 import Timestamp
from typing import Any, Optional, cast

CHARACTERS = list(string.ascii_letters) + [' ']


def letter_frequency(sentence: str) -> list[tuple[str, int]]:
    frequencies = [(c, 0) for c in CHARACTERS]
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter, frequencies[index][1] + 1)
    non_zero = [
        (letter, count)
        for letter, count in frequencies if count > 0
    ]
    return non_zero


@total_ordering
@dataclass(frozen=True)
class MultiItem:
    data_source: str
    timestamp: Optional[float]
    creation_date: Optional[str]
    name: str
    owner_etc: str

    def __lt__(self, other: Any) -> bool:
        if self.data_source == 'Local':
            self_datetime = datetime.datetime.fromtimestamp(
                cast(float, self.timestamp)
            )
        else:
            self_datetime = datetime.datetime.fromisoformat(
                cast(str, self.creation_date)
            )
        if other.data_source == 'Local':
            other_datetime = datetime.datetime.fromtimestamp(
                cast(float, other.timestamp)
            )
        else: 
            other_datetime = datetime.datetime.fromtimestamp(
                cast(str, other.creation_date)
            )
        return self_datetime < other_datetime
    
    def __eq__(self, other: object) -> bool:
        return self.datetime == cast(MultiItem, other).other_datetime

    @property
    def datetime(self) -> datetime.datetime:
        if self.data_source == 'Local':
            return datetime.datetime.fromtimestamp(
                cast(float, self.creation_date)
            )
        else:
            return datetime.datetime.fromtimestamp(
                cast(str, self.creation_date)
            )
    

    @dataclass(frozen=True)
    class SimpleMultiItem:
        data_source: str
        timestamp: Optional[float]
        creation_date: Optional[str]
        name: str
        owner_etc: str

    def by_timestamp(item: SimpleMultiItem) -> datetime.datetime:
        if item.data_source == 'Local':
            return datetime.datetime.fromtimestamp(
                cast(float, item.timestamp))
        elif item.data_source == 'Remote':
            return datetime.datetime.fromisoformat(cast(str, item.creation_date))
        else:
            raise ValueError(f'Unknown data_source in {item!r}')



# driver code 
mi_0 = MultiItem('Local',  1607280522.68012, None, 'Some File', 'etc. 0')
mi_1 = MultiItem('Remote', None, '2020-12-06T13:47:52.849153', 'Another File', 'etc. 1')
mi_2 = MultiItem('Local', 1579373292.452993, None, 'This File', 'etc. 2')
mi_3 = MultiItem('Remote', None, '2020-01-18T13:48:12.452993', 'That File', 'etc. 3')
 

file_list = [mi_0, mi_1, mi_2, mi_3]
file_list.sort()
pprint(file_list)

file_list.sort(key=by_timestamp)
file_list.sort(key=lambda item: item.name)
file_list.sort(key=operator.attrgetter('name'))
