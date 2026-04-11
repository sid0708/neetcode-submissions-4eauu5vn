class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        open = ""
        seen = {"{": "}", 
                 "(": ")",
                 "[": "]"}
        if not s:
            return True
        for each in s:
            if each in seen:
                res.append(each)
            if each in seen.values():
                if res:
                    open = res.pop()
                    if seen[open] != each:
                        return False
                else:
                    return False
        if len(res) ==0:
            return True
        else:
            return False
        
