'''
1-> adicionar em uma lista esses valores
2-> se seu opsto estiver la, retiro com pop
3-> se não estiver, adiciono com append
4-> se a lista estiver vazia tentaram fechar algo q nunca abriu
5-> se não combinar (ex: ch é ']' e o topo é '(') retorna falso
6 -> só qnd estiver vazia que podemos retornar true
'''
class Solution:
    def isValid(self, s: str) -> bool:
        opost = []
        for i in range(len(s)):
            ch = s[i]
            if ch == '(' or ch =='{' or ch == '[':
                opost.append(ch)
            else:
                if not opost: #4
                    return False
                if ch == ')' and opost[-1] == "(" :#2
                    opost.pop() 
                elif ch == ']' and opost[-1] == "[" :#2
                    opost.pop()
                elif ch == '}' and opost[-1] == "{" :#2
                    opost.pop()
                else: #5
                    return False
        if len(opost) == 0:
            return True
        else:
            return False
'''
TIME: O(n)
SPACE: O(n)
'''