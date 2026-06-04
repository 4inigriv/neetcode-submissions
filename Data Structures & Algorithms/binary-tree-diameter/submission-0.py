# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
1-> percorrer a arvore
2-> CASO BASE: arvore vazia
3-> diametro -> caminho mais longo dentre quaisquer dois nos 
altura esqueda = no.esquerd + 1
altura direita =no direita +1
d = alturas

'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0 
        def dfs(node):
            nonlocal diameter 
            if node is None:
                return 0 
            high_left = dfs(node.left)
            high_right = dfs(node.right)
            diameter = max(diameter,high_left + high_right)
            return  1 + max(high_left,high_right)
        dfs(root)
        return diameter
           