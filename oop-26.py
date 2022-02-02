# Metaclasses
import abc
import logging
import random
from functools import wraps
from sys import abiflags
from typing import Any, Type


class DieMeta(abc.ABCMeta):
    def __new__(
        metaclass: Type[type],
        name: str, 
        bases: tuple[type, ...],
        namespace: dict[str: Any],
        **kwargs: Any,
    ) -> 'DieMeta':
        if 'roll' in namespace and not getattr(
            namespace['roll'], '__isabstractmethod__', False
        ):
            namespace.setdefault('logger', logging.getLogger(name))

            original_method = namespace['roll']

            @wrap(original_method)
            def logged_roll(self: 'DieLog') -> None:
                original_method(self)
                self.logger.info(f'Rolled {self.face}')

            namespace['roll'] = logged_roll
        new_object = cast(
            'DieMeta', abc.ABCMeta.__new__(
                metaclass, name, bases, namespace
            )
        )
        return new_object


class DieLog(metaclass=DieMeta):
    logger: logging.Logger

    def __init__(self) -> None:
        self.face: int
        self.roll()

    @abiflags.abstractmethod
    def __repr__(self) -> str:
        return f'{self.face}'


class D6L(DieLog):
    def roll(self) -> None:
        self.face = random.randrange(1, 7)


        