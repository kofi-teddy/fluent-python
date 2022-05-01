# Calculating elevy
from decimal import Decimal


rate = 1.5

amount = 5000

def get_tax(amount):
    tax = amount * (rate / 100)
    print(tax)
    return tax


if amount > 100: 
    get_tax(amount)

    
