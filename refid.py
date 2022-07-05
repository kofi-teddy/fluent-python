import random
import string
from django.utils.text import slugify
from io import BytesIO

    
# def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))


# random_string_generator()


# def unique_key_generator():
  
#     size = random.randint(30, 45)
#     key = random_string_generator(size=size)
#     return key

# unique_key_generator()

# def random_number_generator(size=15, chars=string.digits):
#     number = (''.join(random.choice(chars) for _ in range(size)))
#     wt_number = 'WT' + number
#     print(wt_number)
#     return wt_number

# random_number_generator()
# amount=100 
# rate = 2
# def compute_fee(rate, amount):
#     fee = rate/100 * amount
#     print(fee)
#     return fee

# compute_fee(1, 1000)


def otp_generator():
    otp = random.randint(99999, 999999)
    print(otp)
    return otp



otp_generator()
