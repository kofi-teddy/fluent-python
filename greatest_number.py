from typing import List

# def greatest_number(array: List[int]) -> int:
#     for i in array:
#         is_the_greatest_number = True

#         for j in array:
#             if j > i:
#                 is_the_greatest_number = False
        
#         if is_the_greatest_number:
#             return i
        

def greatest_number(array: List[int]) -> int:
    max_num = array[0]
    for i in array:
        if i > max_num:
            max_num = i
    return max_num


array = [100, 2, 3, 4, 5]

print(greatest_number(array))