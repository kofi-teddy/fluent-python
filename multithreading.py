# python program to illustrate the concept
# of threading 

import threading
import os


# def print_cube(num):
#     '''
#     function to print cube of a given num
#     '''
#     print(f'Cube: {num * num * num}')


# def print_square(num):
#     '''
#     function to print square of given num
#     '''
#     print(f'Square: {num * num}')


# if __name__ == '__main__':
#     # creating thread
#     t1 = threading.Thread(target=print_square, args=(10,))
#     t2 = threading.Thread(target=print_cube, args=(10,))

#     # starting thread 1
#     t1.start()
#     # starting thread 2 
#     t2.start()

#     # wait until thread 1 is completely exexuted
#     t1.join()
#     # wait until thread 2 is completely exexuted
#     t2.join()

#     # both threads completely executed
#     print('Done!')


def task1():
    print(f'Task 1 assigned to thread: {threading.current_thread().name}')
    print(f'ID of process running task 1: {os.getpid()}')


def task2():
    print(f'Task 2 assigned to thread: {threading.current_thread().name}')
    print(f'ID of process running task 2: {os.getpid()}')


if __name__ == '__main__':

    # print ID of current process
    print(f'ID of process running main program: {os.getpid()}')

    # print name of main thread
    print(f'Main thread name: {threading.current_thread().name}')

    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    # starting threads
    t1.start()
    t2.start()

    # wait until all threads finish
    t1.join()
    t2.join()