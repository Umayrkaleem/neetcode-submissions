class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        temp = []
        
        operator ={"+","-","*","/"}

        for token in tokens:
            if token in operator:
                a = int(stack.pop())
                b = int(stack.pop())
                if token == "+":
                    stack.append(a + b)
                if token == "-":
                    stack.append(b-a)
                if token == "*":
                    stack.append(a*b)
                if token == "/":
                    stack.append(int(b/a))
                print("do math", a, token, b)
            else:
                stack.append(int(token))
                print("append digit", stack)

        return stack[0]
        