# oop
# Exceptions handling  

from typing import List, NoReturn, Union


# class EvenOnly(List[int]):
#     def append(self, value: int) -> None:
#         if not isinstance(value, int):
#             raise TypeError('Only integers can be added')
#         if value % 2 != 0:
#             raise ValueError('Only even numbers can be added')
#         super().append(value)


# def never_returns() -> NoReturn:
#     print('I am about to raise an exception')
#     raise Exception('This is always raised')
#     print('this line will never executed')
#     return 'I won"t be returned'


# def call_exceptor() -> None:
#     print('Call_exceptor starts here...')
#     never_returns()
#     print('An exception was raised...')
#     print('...so these lines dont run')


# def handle() -> None:
#     try:
#         never_returns()
#         print('Never executed')
#     except Exception as ex:
#         print(f'I caught an exception: {ex!r}')
#     print('Executed after the exception')


# def funny_division(divisor: float) -> Union[str, float]:
#     try:
#         if divisor == 13:
#             raise ValueError('13 is an unlucky number')
#         return 100 / divisor
#     except ZeroDivisionError:
#         return 'Zero is not a good idea!'


from decimal import Decimal


class InvalidWithdrawal(ValueError):
    def __init__(self, balance: Decimal, amount: Decimal) -> None:
        super().__init__(f'account doesn"t have GHS{amount}')
        self.amount = amount
        self.balance = balance

    def overage(self) -> Decimal:
        return self.amount - self.balance


# driver code 
# never_returns()
# e = EvenOnly()
# e.append('a string')
# e.append(3)
# e.append(2)
# print(funny_division(0))
# print(funny_division(50.0))
# print(funny_division('hello'))
# for val in (0, 'hello', 50.0, 13):
#     print(f'Testing {val!r}')

# raise InvalidWithdrawal(Decimal('25.00'), Decimal('50.00'))
try:
    balance = Decimal('25.00')
    raise InvalidWithdrawal(balance, Decimal('50.00'))
except InvalidWithdrawal as ex:
    print(f'I"m sorry, but your withdrawal is more than your balance by GHS{ex.overage()}')