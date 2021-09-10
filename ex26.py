from array import array

# Format for arrays
# arrayName = array(typecode, [Initializers])

'''
Typecode	Value
b	Represents signed integer of size 1 byte/td>
B	Represents unsigned integer of size 1 byte
c	Represents character of size 1 byte
i	Represents signed integer of size 2 bytes
I	Represents unsigned integer of size 2 bytes
f	Represents floating point of size 4 bytes
d	Represents floating point of size 8 bytes
'''

nums = array('i', [10, 20, 30, 40, 50])

# Accessing elements in an array
for x in nums:
    print(x)

print (nums[0])
print (nums[2])


# Insertion
nums.insert(1,60)


# Deletion
nums.remove(40)


# Search using index
print(nums.index(40))


