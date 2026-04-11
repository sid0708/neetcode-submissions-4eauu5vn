class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for each in strs:
            z = ":)"
            s += each+z
        return s




    def decode(self, s: str) -> List[str]:
        parts = s.split(":)")
        if parts and parts[-1] == "":
            parts.pop()
        return parts

  
