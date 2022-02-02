# Operator overloading
'''
We can apply Python operators more widely than the built-in numbers and
collection types. Doing this can be called "overloading" the operators: letting them
work with more than the built-in types.
'''
from types import new_class
from typing import Type


class DDice:
    def __init__(self, *die_class: Type[Die]) -> None:
        self.dice = [dc() for dc in die_class]
        self.adjust: int = 0

    def plus(self, adjust: int = 0) -> 'DDice':
        self.adjust = adjust
        return self

    def roll(self) -> None:
        for d in self.dice:
            d.roll()

    @property
    def total(self) -> int:
        return sum(d.face for d in self.dice) + self.adjust

    def __add__(self, die_class: Any) -> 'DDice':
        if isinstance(die_class, type) and issubclass(die_class, Die):
            new_classes = [type(d) for d in self.dice] +[die_class]
            new = DDice(*new_classes).plus(self.adjust)
            return new
        elif isinstance(die_class, int):
            new_classes = [type(d) for d in self.dice]
            new = DDice(*new_classes).plus(die_class)
            return new
        else:
            return NotImplemented

    def __radd__(self, die_class: Any) -> 'DDice':
        if isinstance(die_class, type) and issubclass(die_class, Die):
            new_classes = [die_class] + [type(d) for d in self.dice]
            new = DDice(*new_classes).plus(self.adjust)
            return new 
        elif isinstance(die_class, int):
            new_classes = [type(d) for d in self.dice]
            new = DDice(*new_classes).plus(die_class)
            return new
        else:
            return NotImplemented

    def __mul__(self, n: Any) -> 'DDice':
        if isinstance(n, int):
            new_classes = [type(d) for d in self.dice for _ in range(n)]
            return DDice(*new_classes).plus(self.adjust)
        else:
            return NotImplemented

    def __rmul__(self, n: Any) -> 'DDice':
        if isinstance(n, int):
            new_classes = [type(d) for d in self.dice for _ in range(n)]
            return DDice(*new_classes).plus(self.adjust)
        else:
            return NotImplemented

    def __iadd__(self, die_class: Any) -> 'DDice':
        if isinstance(die_class, type) and issubclass(die_class, Die):
            self.dice += [die_class()]
            return self
        elif isinstance(die_class, int):
            self.adjust += die_class
            return self
        else:
            return NotImplemented