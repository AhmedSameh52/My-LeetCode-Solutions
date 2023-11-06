class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]
        for i in range (0, len(s)):
            if s[i] == ')' and stack[-1] != '(':
                 return False                
            elif s[i] == '}' and stack[-1] != '{':
                return False
            elif s[i] == ']' and stack[-1] != '[':
                return False
            elif s[i] == ']' or s[i] == ')' or s[i] == '}':
                stack.pop()
            else:
                stack.append(s[i])
        if stack == [0]:
            return True
        else:
            return False