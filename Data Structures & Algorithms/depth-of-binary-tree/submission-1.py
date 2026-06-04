# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
''' solução iterativa
guardar os elementos [nó_Atual,altura desse nó] -> pilha = [[root, 1]]
tiar o ultimo nó -> no, altura_atual = pilha.pop()
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [[root,1]] # -> [no atual, altura dele]
        max_hight = 0
        while stack:
            no, nowhight = stack.pop() #tira os nós somente
            if no is not None:
                max_hight = max(max_hight,nowhight)
                stack.append([no.left, nowhight+1]) #filhos na pilha eles + 1
                stack.append([no.right, nowhight+1])

        return max_hight
            
'''
TIME: O(n)
SPACE: O(n)
'''