# Closures

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 4)
add_logger(5, 6)

sub_logger(10, 5)
sub_logger(20, 10)






# def outer_func(msg):
#     message = msg

#     def inner_func():
#         print(message)

#     return inner_func

# hi_func = outer_func('Hi')
# hello_func = outer_func('Hello')

# hi_func()
# hello_func()
