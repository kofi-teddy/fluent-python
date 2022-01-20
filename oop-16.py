# oop
# More advance concepts oop   
# Properties in detail


class Blue:
    def __init__(self, name: str) -> None:
        self._name = name
        self._state: str

    def _get_state(self) -> str:
        print(f'Getting {self._name}"s State') 
        return self._state

    def _set_state(self, state: str) -> None:
        print(f'Setting {self._name}"s State to {state!r}')
        self._state = state

    def _del_state(self) -> None:
        print(f'{self._name} is pushing up daisies!')
        del self._state

    silly = property(
        _get_state, _set_state, _del_state,
        'This is a silly property'
    )


# driver code 
p = Blue('Polly')
p.silly ='pining for the fjords'
print(p.silly)
del p.silly
help(Blue)