# Python Data Structures
from typing import NamedTuple


class Stock(NamedTuple):
    symbol: str
    current: float
    high: float
    low: float

    @property
    def middle(self) -> float:
        return (self.high + self.low)/2


# drive code
s = Stock('AAP', 123.52, 137.98, 53.15)
print(s.middle)
# print(s.current)
# print(s[2])
# symbol, current, high, low = s
# print(current)

# t = ('kofi', ['kobi', 'ama'])
# t[1].append('yaa')
# print(t)
