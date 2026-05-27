class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def ints():
            token = tokens.pop()#5
            if token not in "+-*/":
                return int(token)#
            right = ints()#4
            left =  ints()#

            if token == "+":
                return right + left#2 + 1 = 3
            elif token == "*":
                return right * left
            elif token == "-":
                return left - right#9-4=5
            elif token == "/":
                return int(left/right)
        return ints()

#-,4,*,3,+,2,1