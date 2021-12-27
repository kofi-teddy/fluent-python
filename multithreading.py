# python program to illustrate the concept
# of threading 

import threading


def print_cube(num):
    '''
    function to print cube of a given num
    '''
    print(f'Cube: {num * num * num}')


def print_square(num):
    '''
    function to print square of given num
    '''
    print(f'Square: {num * num}')


if __name__ == '__main__':
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # starting thread 1
    t1.start()
    # starting thread 2 
    t2.start()

    # wait until thread 1 is completely exexuted
    t1.join()
    # wait until thread 2 is completely exexuted
    t2.join()

    # both threads completely executed
    print('Done!')