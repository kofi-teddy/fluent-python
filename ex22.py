# Decorators

def logger(func):
    def wrapper():
        print("----Logging execution----")
        func()
        print("----Done logging----")
    return wrapper


@logger
def sample():
    print("----Inside a sample function----")


sample()