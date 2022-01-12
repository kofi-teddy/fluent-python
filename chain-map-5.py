# putting python ChainMap into action 
from collections import ChainMap

# fruits_prices = {'apple': 0.80, 'grape': 0.40, 'orange': 0.50}
# veggies_prices = {'tomato': 1.20, 'pepper': 1.30, 'onion': 1.25}
# prices = ChainMap(fruits_prices, veggies_prices)

# order = {'apple': 4, 'tomato': 8, 'orange': 4}

# for product, units in order.items():
#     price = prices[product]
#     subtotal = units * price
#     print(f'{product:6}: GHS{price:.2f} x {units} = GHS{subtotal:.2f}')



# real world scenario
class User:
    def __init__(self, name, user_id, role):
        self.name = name
        self.user_id = user_id
        self.role = role


class CRMUser(User):
    def __init__(self, name, component, **kwargs):
        defualts = {'user_id': next(component.user_id), 'role': 'read'}
        super().__init__(name, **ChainMap(kwargs, defualts))