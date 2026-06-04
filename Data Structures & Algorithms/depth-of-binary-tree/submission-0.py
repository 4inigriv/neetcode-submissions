'''
1-> caso base: se o nó for vazio a altura é 0
2-> pegar os valores da altura 
3 -> retorna o maximo da esquerda e da direita chamando + o nó atual
4-> inicia a função a partir da raiz 
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depht(node):
            if node == None: #1
                return 0 
            else:
              hight_left = depht(node.left) #2
              hight_right= depht(node.right) #2
            return max(hight_left,hight_right) + 1# 3
        return depht(root) #4

        
        