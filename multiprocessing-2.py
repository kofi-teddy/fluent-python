# data sharing and communication between multiple 
# processes
import multiprocessing


# empty lis with global scope
# result = []


# def square_list(my_list):
#     '''
#     function to square a given list
#     '''
#     global result
#     # append squares of mylist to global list results
#     for num in my_list:
#         result.append(num * num)
#     # print global list results
#     print(f'Result(in process p1): {result}')


# if __name__ == '__main__':
#     # input list 
#     my_list = [1, 2, 3, 4]

#     # creating new process
#     p1 = multiprocessing.Process(target=square_list, args=(my_list,))
#     # starting process
#     p1.start()
#     # wait until process is finished
#     p1.join()

#     # print global result list
#     print('Result(in manin program): {result}')


# # python code demonstrate sharing data between processes
# def square_list(my_list, result, square_sum):
#     '''
#     function to square a given list
#     '''
#     # append squares of mylist to result array
#     for idx, num in enumerate(my_list):
#         result[idx] = num * num

#     # square_sum value
#     square_sum.value = sum(result)

#     # print result array
#     print(f'Result(in process p1: {result[:]})')

#     # print square_sum value
#     print(f'sum of squares(in process p1): {square_sum.value}')


# if __name__ == '__main__':
#     # input lists
#     my_list = [1,2,3,4]

#     # creating array of int data with space for 4 integers
#     result = multiprocessing.Array('i', 4)

#     # creating value of int data type 
#     square_sum = multiprocessing.Value('i')

#     # creating new process
#     p1 = multiprocessing.Process(target=square_list, args=(my_list, result, square_sum))

#     # starting process
#     p1.start()

#     # wait until the process is finished
#     p1.join()

#     # print result array
#     print(f'Result(in main program): {result[:]}')

#     # print square_sum value
#     print(f'Sum of square(in main program) {square_sum.value}')


'''
Server process managers are more flexible than using shared
memory objects because they can be made to support arbitrary 
object types like lists, dictionaries, Queue, Value, Array, 
etc. Also, a single manager can be shared by processes on 
different computers over a network. They are, however, 
slower than using shared memory.
'''
# def print_records(records):
#     '''
#     function to print record(tuples) in records(list)
#     '''
#     for record in records:
#         print(f'Name:  {record[0]} \nScore: {record[1]}\n')


# def insert_record(record, records):
#     '''
#     function to add a new record to records(list)
#     '''
#     records.append(record)
#     print('New record added! \n')


# if __name__ == '__main__':
#     with multiprocessing.Manager() as manager:
#         # creating a lis in server process memory
#         records = manager.list([('Teddy', 10), ('Felix', 9), ('Robert', 9)])
#         # new record to be inserted in records
#         new_record = ('Michael', 8)

#         # creating new processes
#         p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
#         p2 = multiprocessing.Process(target=print_records, args=(records,))

#         # running process p1 to insert new record
#         p1.start()
#         p1.join()

#         # running process p2 to print records
#         p2.start()
#         p2.join()


# def square_list(mylist, q):
#     '''
#     function to square a given list
#     '''
#     # append squares of mylist to queue
#     for num in mylist:
#         q.put((num * num))


# def print_queue(q):
#     '''
#     fucntion to print queue elements
#     '''
#     print('Queue elements')
#     while not q.empty():
#         print(q.get())
#     print('Queue is now empty!')


# if __name__ == '__main__':
#     # input list
#     mylist = [1, 2, 3, 4]

#     # creating multiprocessing Queue
#     q = multiprocessing.Queue()

#     # creating new processes
#     p1 = multiprocessing.Process(target=square_list, args=(mylist, q))
#     p2 = multiprocessing.Process(target=print_queue, args=(q,))

#     # running process p1 to square list
#     p1.start()
#     p1.join()

#     # running process p2 to get queue elements
#     p2.start()
#     p2.join()


def sender(conn, msgs):
    '''
    function to send messages to other end of pipe
    '''
    for msg in msgs:
        conn.send(msg)
        print(f'sent the message: {msg}')
    conn.close()


def receiver(conn):
    '''
    function to print the message received from other 
    end of pipe
    '''
    while 1:
        msg = conn.recv()
        if msg == 'END':
            break
        print(f'Received the message: {msg}')


if __name__ == '__main__':
    # message to sent
    msgs = ['hello', 'hey', 'hru?', 'END']

    # creating a pipe 
    parent_conn, child_conn = multiprocessing.Pipe()

    # creating new processes
    p1 = multiprocessing.Process(target=sender, args=(parent_conn, msgs))
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

    # running processes
    p1.start()
    p2.start()

    # wait untill process finish
    p1.join()
    p2.join()