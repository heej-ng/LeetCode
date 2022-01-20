class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        res = True
        for value in s:
            if value == "(":
                stack.append(value)
            elif value == "[":
                stack.append(value)
            elif value == "{":
                stack.append(value)
            elif value == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    return False
            elif value == "]":
                if len(stack) == 0 or stack.pop() != "[":
                    return False
            elif value == "}":
                if len(stack) == 0 or stack.pop() != "{":
                    return False
        if(len(stack) != 0):
            return False
        return True        