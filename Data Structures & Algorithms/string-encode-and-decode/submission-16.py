class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for each in strs:
            s += each + ";;)"
        return s

    def decode(self, s: str) -> List[str]:
        return s.split(";;)")[:-1]

