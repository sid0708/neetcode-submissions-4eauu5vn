class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        match = {'[': ']',
                  '{': "}",
                  '(': ")"}
        if not s:
            return False
        for chars in s:
            if chars in match:
                res.append(chars)
            else:
                # char is a closng
                # pop from list
                if res:
                    close = res.pop()
                    if match[close] != chars:
                        return False
                else:
                    return False
        if len(res) == 0:
            return True
        else:
            return False
