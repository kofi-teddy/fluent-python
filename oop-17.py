# oop
# More advance concepts oop   
# Properties in detail
# Using decorators to create properties

class Blue_P:
    def __init__(self, name: str) -> None:
        self._name = name
        self._state: str

    @property
    def silly(self) -> str:
        print(f'Getting {self._name}"s State')
        return self._state

    @silly.setter
    def silly(self, state: str) -> None:
        print(f'Setting {self._name}"s State to {state!r}')
        self._state = state

    @silly.delete
    def silly(self) -> None:
        print(f'{self._name} is pushing up daisies!')
        del self._state