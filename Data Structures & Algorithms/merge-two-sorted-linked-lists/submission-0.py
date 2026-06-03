# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2: #percorrre
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next #anda
            else:
                current.next = list2
                list2 = list2.next #anda
            current = current.next
        #if they have large different 
        if list1:
            current.next = list1
        else:
            current.next= list2
        return dummy.next

