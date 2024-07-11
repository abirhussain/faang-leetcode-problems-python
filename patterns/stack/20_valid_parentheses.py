class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = {')':'(', ']':'[', '}':'{'}

        for ch in s:
            if ch in brackets_map:
                opening_bracket = stack.pop() if stack else '#'
                if brackets_map[ch] != opening_bracket:
                    return False
            else:
                stack.append(ch)

        return False if stack else True
        