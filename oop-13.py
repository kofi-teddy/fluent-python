# oop
# Exceptions handling  

from typing import List, NoReturn, Union
from decimal import Decimal


# Sample Inventory application exception handling

class ItemType:
    def __init__(self, name: str) -> None:
        self.name = name
        self.on_hand = 0

class OutOfStock(Exception):
    pass


class InvalidItemType(Exception):
    pass


class Inventory:
    def __init__(self, stock: list[ItemType]) -> None:
        pass

    def lock(self, item_type: ItemType) -> None:
        '''
        Context Entry.
        Lock the item type so nobody else can manipulate the
        inventory while we're working.
        '''
        pass

    def unlock(self, item_type: ItemType) -> None:
        '''
        Context Exit.
        Unlock the item type.
        '''
        pass
    def purchase(self, item_type: ItemType) -> int:
        '''
        If the item is not locked, raise a ValueError
        because something went wrong. 
        If the item_type does not exist, raise
        InvalidItemType.
        If the item is currently out of stock, raise
        OutOfStock.
        If the item is available, 
        substract one item; return the number of items left.
        '''
        # Mocked results.
        if item_type.name == 'Widget':
            raise OutOfStock(item_type)
        elif item_type.name == 'Gadget':
            return 42
        else:
            raise InvalidItemType(item_type)





# driver code 
widget = ItemType('Widget')
gadget = ItemType('Gadget')
inv = Inventory([widget, gadget])

item_to_buy = widget
inv.lock(item_to_buy)

try:
    num_left = inv.purchase(item_to_buy)
except InvalidItemType:
    print(f'Sorry, we don"t sell {item_to_buy.name}')
except OutOfStock:
    print('Sorry, that item is out of stock.')
else:
    print(f'Purchase completed. There are {num_left} {item_to_buy.name}s left')
finally:
    inv.unlock(item_to_buy)

