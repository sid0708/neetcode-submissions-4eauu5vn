class Solution:
    def isValid(self, s: str) -> bool:
        closed = {")": "(", 
                  "]":"[", 
                  "}": "{"}
        openB = set(("(", "[", "{"))
        stack = []
        for each in s:
            if each in openB:
                stack.append(each)
            else:
                if not stack:
                    return False
                openb = stack.pop()
                if openb != closed[each]:
                    return False
        if not stack:
            return True
        else:
            return False

        
        
