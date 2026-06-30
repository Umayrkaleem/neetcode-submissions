class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        keyMap ={
            "}":"{",
            ")":"(",
            "]":"["
        }

        for b in s:
            #if a closing bracket
            if b in keyMap:
                if stack and stack[-1] == keyMap[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        
        if stack:
            return False
        return True