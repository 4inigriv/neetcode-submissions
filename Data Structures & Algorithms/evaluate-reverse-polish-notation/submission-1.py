class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for i in range(len(tokens)):
            token = tokens[i]

            if token == "+":
                a = result.pop()
                b = result.pop()
                result.append(a+b)

            elif token == "-":
                a = result.pop()
                b = result.pop()
                result.append(b-a) #ordem import

            elif token == "*":
                a = result.pop()
                b = result.pop()
                result.append(a*b)

            elif token == "/":
                a = result.pop()
                b = result.pop()
                result.append(int(b/a))
            else: #its a number token == number
                result.append(int(token))
        return result[0]
                
        