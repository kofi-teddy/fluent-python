# import the multiprocessing module 
import multiprocessing
import os

# def print_cube(num):
#     '''
#     function to print cube
#     '''
#     print(f'Cube: {num * num * num}')


# def print_square(num):
#     '''
#     function to print square of given num
#     '''
#     print(f'Square: {num * num}')


# if __name__ == '__main__':
#     # creating processes 
#     p1 = multiprocessing.Process(target=print_square, args=(10, ))
#     p2 = multiprocessing.Process(target=print_cube, args=(10, ))

#     # starting process 1
#     p1.start()
#     # starting process 2
#     p2.start()

#     # wait until process 1 is finished
#     p1.join()
#     # wait until process 2 is finished
#     p1.join()

#     # both process finished 
#     print('Done!')


def worker1():
    # printing process id
    print(f'ID of process running worker1: {os.getpid()}')


def worker2():
    # printing process id
    print(f'ID of process running worker2: {os.getpid()}')


if __name__ == '__main__':
    # printing main program process id
    print(f'ID of main process: {os.getpid()}')

    # creating processes
    p1 = multiprocessing.Process(target=worker1)
    p2 = multiprocessing.Process(target=worker2)

    # starting processes
    p1.start()
    p2.start()

    # process IDs
    print(f'ID of process p1: {p1.pid}')
    print(f'ID of process p2: {p2.pid}')

    # wait until processes are finished
    p1.join()
    p2.join()

    # both processes finished
    print('Both processes finished execution!')

    # check if processes are alive 
    print(f'process p1 is alive: {p1.is_alive()}')
    print(f'process p2 is alive: {p2.is_alive()}')