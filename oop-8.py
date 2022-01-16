# oop
# extending built-ins 
from typing import Optional


class LongNameDict(dict[str, int]):
    def longest_key(self) -> Optional[str]:
        '''
        In effect, max(self, key=len), but less obscure
        '''

        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest


articles_read = LongNameDict()
articles_read['Teddy'] = 28
articles_read['Glenin'] = 29
articles_read['Steven'] = 7

print(articles_read.longest_key())
print(max(articles_read, key=len))
