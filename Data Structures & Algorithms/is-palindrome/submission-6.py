class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        L = 0
        R = len(s) -1
        while L < R:
            # move when not a charcater
            while L <R and not s[L].isalnum():
                L +=1
            # move when not a character
            while L<R and not s[R].isalnum():
                R -=1
            if s[L].lower() !=s[R].lower():
                return False
            L +=1
            R -= 1
        return True
