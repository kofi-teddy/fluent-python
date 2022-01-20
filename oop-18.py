# oop
# More advance concepts oop   
# Properties in detail
# Using decorators to create properties
# when to use properties
# chaching a web page example 
from urllib.request import urlopen
from typing import Optional, cast, List
import time

class WebPage:
    def __init__(self, url: str) -> None:
        self.url = url
        self._content: Optional[bytes] = None 

    @property
    def content(self) -> bytes:
        if self._content is None:
            print('Retrieving New Page...')
            with urlopen(self.url) as response:
                self._content = response.read()
        return self._content


# Driver code
# webpage = WebPage('https://kofiteddy.com')

# now = time.perf_counter()
# content1 = webpage.content
# first_fetch = time.perf_counter() - now

# now = time.perf_counter()
# content2 = webpage.content
# second_fetch = time.perf_counter() - now

# assert content2 == content1, 'Problem: Pages were different'
# print(f'Initial Request    {first_fetch:.5}')
# print(f'Subsequent Request {second_fetch:.5}')


# for attributes thats needs to be calculated on 
# the fly
class AverageList(List[int]):

    @property
    def average(self) -> float:
        return sum(self) / len(self)


a = AverageList([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
print(a.average)
