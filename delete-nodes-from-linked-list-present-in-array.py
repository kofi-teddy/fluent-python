# You are given an array of integers nums and the 
# head of a linked list. Return the head of the 
# modified linked list after removing all nodes 
# from the linked list that have a value that 
# exists in nums.


# Example 1:
# Input: nums = [1,2,3], head = [1,2,3,4,5]
# Output: [4,5]
# Explanation:
# Remove the nodes with values 1, 2, and 3.

# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# All elements in nums are unique.
# The number of nodes in the given list is in the range 
# [1, 105].
# 1 <= Node.val <= 105
# The input is generated such that there is at least one 
# node in the linked list that has a value not present 
# in nums.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

def remove_nodes(head: ListNode, nums: list[int]) -> ListNode:
    # function to remove nodes present in the nums array 
    # create a set from the array for fast lookup
    nums_set = set(nums)

    # create a dummy node to handle edge cases 
    # (like deleting the head node)
    dummy = ListNode()
    dummy.next = head
    current = dummy

    # Travers the linked list
    while current and current.next:
        # if the next nodes value is in the nums_set, 
        # remove it 
        if current.next.val in nums_set:
            current.next = current.next.next
        else:
            current = current.next

    # return the modified list starting from dummy.next 
    # (since dummy is a placeholder)
    return dummy.next


# def list_to_linkedlist(arr):
#     if not arr:
#         return None
    
#     head = ListNode(arr[0])
#     current = head
    
#     for val in arr[1:]:
#         current.next = ListNode(val)
#         current = current.next
#     return head


# def linkedlist_to_list(head):
#     # helper function to convert a linked 
#     # list back to a list
#     result = []
#     current = head
#     while current:
#         result.append(current.val)
#         current = current.next
#     return result


# def remove_nodes_from_linked_list(nums, head_list):
#     head = list_to_linkedlist(head_list)
#     modified_head = remove_nodes(head, nums)
#     return list_to_linkedlist(modified_head)


# nums = [1, 2, 3] 
# head = [1, 2, 3, 4, 5]
# print(remove_nodes_from_linked_list(nums, head))

