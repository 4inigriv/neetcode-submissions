# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current is not None:
            future = current.next #save future
            current.next = prev #current point to null now
            # [null] <- [current]   [future] -> [] -> []
            prev = current 
            current = future
        return prev 

