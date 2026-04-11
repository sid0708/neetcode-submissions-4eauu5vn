class Solution:

    def encode(self, strs: List[str]) -> str:
        m = ""
        for each in strs:
            m += each + ":)"
        return m




    def decode(self, s: str) -> List[str]:
        return s.split(":)")[:-1]

        
   

  
