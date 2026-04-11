class Solution:
    def isValid(self, s: str) -> bool:
        closeKey = {")": "(", "}": "{", "]": "[" }
        stack = []

        for chars in s:
            if chars not in closeKey:
                # append
                stack.append(chars)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != closeKey[chars]:
                        return False
        return True if not stack else  False

                
        

        