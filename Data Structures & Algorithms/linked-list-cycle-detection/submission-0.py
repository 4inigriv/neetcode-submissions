# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
1-> passar por todos os nós
2-> armazenar os nós
3-> comparar com o no atual o nó armazenado
4-> se ja passou por aquele nó, retorne verdadeiro 
5-> se não, anda
6-> se n td isso falso
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nonow = head
        armazen = set() #2
        while nonow: #1
            if nonow in armazen: #3
                return True #4
            else:
                armazen.add(nonow) #2
                nonow = nonow.next #5
        return False #6

        