class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        setDict = {']': '[', '}': '{', ')': '('}
        if s == "":
            return True
        for c in s:
            if c not in setDict:
                lst.append(c)
            elif len(lst)!=0:
                m = lst.pop()
                if setDict[c] != m:
                    return False
            else:
                return False
        if not lst:
            return True
        return False