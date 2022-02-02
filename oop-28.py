# oop
# using defauldict
from __future__ import annotations

from collections import defaultdict, Counter
from dataclasses import dataclass
from pprint import pprint



def letter_frequency(sentence: str) -> dict[str, int]:
    frequencies: dict[str, int] = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies


def letter_frequency_2(sentence: str) -> defaultdict[str, int]:
    frequencies: defaultdict[str, int] = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


def letter_frequency_3(sentence: str) -> Counter[str]:
    return Counter(sentence)



@dataclass
class Prices:
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0


responses = [
    'vanilla',
    'vanilla',
    'vanilla',
    'vanilla',
    'chocolate',
    'caramel',
    'strawberry',
]


# driver code
# print(Prices())
# portfolio = defaultdict(Prices)
# print(portfolio['GHS'])
# portfolio['USD'] = Prices(current=122.25, high=137.98, low=53.15)
# pprint(portfolio)
favorites = Counter(responses).most_common(1)
name, frequency = favorites[0]
print(name)



