# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:     
        dummy = result = head

        prev = None
        while dummy:
            #i dont wanna lose the rest of the linked list
            temp = dummy.next
            #point the node at the previous, aka flip the pointer
            dummy.next = prev
            #update pointer to the current node
            prev = dummy
            #update dummy to the next node
            dummy = temp 

        return prev