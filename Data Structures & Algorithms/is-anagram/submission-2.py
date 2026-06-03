'''
 é um jogo de palavras criado a partir da reorganização ou do embaralhamento das letras de uma palavra ou frase original. Para que seja um anagrama, é obrigatório:
 -> utilizar todas as letras originais 
 -> exatamente o mesmo número de vezes
'''

''' Oq quero fzr:
1-> percorrer a string s e string t
2-> guardar os valores q sao iguais 
3-> verificar a quantidade de letras q sao iguais
4-> verificar a quantidade de vezes q apareceu (ex: ratto, tem-> 1r,1a,2t,1o) dic
5-> verificar o tamanho das duas
6-> se a soma de repeat for = 0 é anagrama
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        repeat = {}

        if len(s) != len(t): #3
            return False

        for i in range(len(s)): #1
            if s[i] in repeat: #2
                repeat[s[i]] += 1 #4
            else:
                repeat[s[i]] = 1

        for j in range(len(t)):#1
            if t[j] in repeat: #2
                repeat[t[j]] -= 1#4
            else:
                repeat[t[j]] = -1

        for value in repeat.values(): #6
            if value != 0:
                return False

        return True
'''
TIME : O(n)
SPACE: O(n)
'''
