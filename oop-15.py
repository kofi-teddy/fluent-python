# oop
# More advance concepts oop   
# adding behavior to class data with properties

class Color:
    def __init__(self, rgb_value: int, name: str) -> None:
        self._rgb_value = rgb_value
        self._name = name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

    def set_rgb_value(self, rgb_value: int) -> None:
        self._rgb_value = rgb_value

    def get_rgb_value(self) -> int:
        return self._rgb_value


class Color_Py:
    def __init__(self, rgb_value: int, name: str) -> None:
        self.rgb_value = rgb_value
        self.name = name


class Color_V:
    def __init__(self, rgb_value: int, name: str) -> None:
        self._rgb_value = rgb_value
        if not name: 
            raise ValueError(f'Invalid name {name!r}')
        self._name = name
    
    def set_name(self, name: str) -> None:
        if not name:
            raise ValueError(f'Invalid name {name!r}')
        self._name = name

# converting methods to properties
class Color_VP:
    def __init__(self, rgb_value: int, name: str) -> None:
        self._rgb_value = rgb_value
        if not name: 
            raise ValueError(f'Invalid name {name!r}')
        self._name = name

    def _set_name(self, name: str) -> None:
        if not name: 
            raise ValueError(f'Invalid name {name!r}')
        self._name = name

    def _get_name(self) -> str:
        return self._name

    name = property(_get_name, _set_name)

# driver code 
# c = Color(0xff0000, 'bright red')
# print(c.get_name())
# c.set_name('red')
# print(c.get_name())

# c = Color_Py(0xff0000, 'bright red')
# print(c.name)
# c.name = 'red'
# print(c.name)

c = Color_VP(0xff0000, 'bright red')
print(c.name)
c.name = 'red'
print(c.name)
# c.name = ''
