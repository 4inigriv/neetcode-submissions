'''
->ponteiro next rapido e next lento
-> no momento q eles forem iguais significa q ele ja pasou por ali antes
-> n preciso armazenar nd so fzr comparações
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
'''
TIME: O(n)
SPACE: O(1)
'''