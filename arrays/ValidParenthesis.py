class ValidParenthesis:
    def isValid(self, s: str):
        stack = []
        closedDict = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in closedDict:
                if stack and stack[-1] == closedDict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True