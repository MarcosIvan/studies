#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif i == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif i == ']':
                if not stack or stack.pop() != '[':
                    return False
            else:
                stack.append(i)

        return len(stack) == 0