# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, current = None, head

        while current:
            #saves the next node
            temp = current.next
            #reverses the pointer
            current.next = prev
            #update prev node to current node
            prev = current
            #move to the next node
            current = temp
        
        return prev
            