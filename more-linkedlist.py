# creating linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# linking the nodes together: node1 -> node2 -> node3
node1.next = node2
node2.next = node3

#  head of the linked list points to the first node
head = node1


# tranversing a linked list
def traverse(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# traversing the linked list
# traverse(head)


# inserting a node into a linked list
def insert_at_end(head, value):
    new_node = ListNode(value)

    if not head:
        return new_node
    
    current = head
    while current.next:
        current = current.next

    # insert the new at the end
    current.next = new_node
    return head


# insert node with value 4 at the end
head = insert_at_end(head, 4)
# traverse(head)


# deleting a node from a linked list
def delete_node(head, value):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next:
        if current.next.val == value:
            current.next = current.next.next

        else:
            current = current.next

    return dummy.next


head = delete_node(head, 3)
# traverse(head)


# removing multiple nodes from a linklist list
def remove_nodes_in_nums(head, nums):
    nums_set = set(nums)
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next:
        if current.next.val in nums_set:
            current.next = current.next.next
        else:
            current = current.next
    
    return dummy.next


# nums = [1, 2]
# head = remove_nodes_in_nums(head, nums)
# traverse(head)


# reversing a linked List
def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev 
        prev = current 
        current = next_node
    
    return prev


# test reversing the list
# reversed_head = reverse_linked_list(head)
# traverse(reversed_head)


# converting an array to a linked list
def array_to_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
linked_list = array_to_linked_list(arr)
# traverse(linked_list)


# converting a linked list to an array
def linked_list_to_array(head):
    arr = []
    current = head

    while current:
        arr.append(current.val)
        current = current.next

    return arr


# result_array = linked_list_to_array(linked_list)
# print(result_array)


# checking for a cycle in a linked list
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False


# cycle_exists = has_cycle(linked_list)
# print(cycle_exists)


# merging two sorted linked lists
# def merge_two_lists(l1, l2):
#     dummy = ListNode(0)
#     current = dummy

#     while l1 and l2:
#         if l1.val < l2.val:
#             current.next = l1
#             l1 = l1.next
#         else:
#             current.next = 12
#             l2 = l2.next

#         current = current.next

#     current.next = l1 if l1 else l2
#     return dummy.next

def merge_two_lists(l1, l2):
    dummy = ListNode(0)  
    current = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 if l1 else l2
    
    return dummy.next  


l1 = array_to_linked_list([1, 3, 5])
l2 = array_to_linked_list([2, 4, 6])
merged_list = merge_two_lists(l1, l2)
traverse(merged_list)
