class Solution:
    def isValid(self, s: str) -> bool:
        stringP = {"(":")", "{":"}", "[": "]"}
        lst = []
        if s == "":
            return False
        for each in s:
            if each in stringP:
                lst.append(each)
            else:
                if not lst:
                    return False
                top = lst.pop()
                if stringP[top] != each:
                    return False
        return len(lst) == 0


            



                
        

        