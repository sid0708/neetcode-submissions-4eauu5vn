class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        if not strs:
            return ""
        for each in strs:
            s += each + ";;)"
        return s

    def decode(self, s: str) -> List[str]:

        return s.split(";;)")[:-1]
