""" 
! PROMPT: Given head, the head of the linked list, determine if the list has a cycle. Does the next pointer of the tail node point to another element in the list

TODO: Understand
* Two-Pointer approach:
    - 1st pointer is the slow pointer, that iterates over the list once.
    - 2nd pointer is the fast pointer, that iterates over the list every time the 1st pointer changes positions

* If next pointer of tail points to the node the 1st pointer is at, return True. 

TODO: Problem Solving
If length of linked list == 1, return False

curr = head
while curr.next:
    sec = curr.next
    while sec:
        if sec == curr:
            return True
        sec = sec.next
    curr = curr.next
return False
"""

# def hasCycle(head):
#     if (not head) or (not head.next):
#         return False
    
#     curr = head
#     while curr.next:
#         second = curr.next
#         while second:
#             if second.val == curr.val:
#                 return True
#             second = second.next
#         curr = curr.next

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if (not head) or (not head.next):
            return False

        curr = head
        visited = set()
        visited.add(curr)
        while curr.next:
            if curr.next in visited:
                return True
            visited.add(curr.next)
            curr = curr.next
        return False
        




