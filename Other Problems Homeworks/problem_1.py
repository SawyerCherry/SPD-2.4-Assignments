#Given an array of k singly-linked lists, each of whose values are in sorted order, combine all nodes (do not create new nodes) into one singly-linked list with all values in order.

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_two_list(l1, l2):
    placeholder = Node()
    tail = placeholder
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return tail

def merge_list(lists):
    if not lists or len(lists) == 0:
        return None
    while len(lists):
        lists_array = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            lists_array.append(merge_list(l1, l2))
        lists = lists_array
    return lists[0]