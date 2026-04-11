class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = ""
        for c in s:
            if c.isalnum():
                m += c.lower()
        return m == m[::-1]
        

        
