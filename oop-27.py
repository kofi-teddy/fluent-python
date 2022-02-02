# Python Data Structures
from typing import NamedTuple
from dataclasses import dataclass


@dataclass
class StockOrdinary:
    def __init__(self, name: str, current: float, high: float, low: float) -> None: 
        self.name = name
        self.current = current
        self.high = high 
        self.low = low


# @dataclass
# class Stock:
#     symbol: str
#     current: float
#     high: float
#     low: float

#     @property
#     def middle(self) -> float:
#         return (self.high + self.low)/2


# class Stock(NamedTuple):
#     symbol: str
#     current: float
#     high: float
#     low: float

#     @property
#     def middle(self) -> float:
#         return (self.high + self.low)/2


# drive code
s_ord = StockOrdinary('AAP', 123.52, 137.98, 53.15)
# print(s_ord)

s_ord_2 = StockOrdinary('AAP', 123.52, 137.98, 53.15)
print(s_ord == s_ord_2)


# s = Stock('AAP', 123.52, 137.98, 53.15)
# print(s.middle)
# print(s.current)
# print(s[2])
# symbol, current, high, low = s
# print(current)

# t = ('kofi', ['kobi', 'ama'])
# t[1].append('yaa')
# print(t)
