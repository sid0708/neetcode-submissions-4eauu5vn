class MinStack:

    def __init__(self):
        self.res = []
        self.minval = []
        
    def push(self, val: int) -> None:
        self.res.append(val)
        val = min(val, self.minval[-1] if self.minval else val)
        self.minval.append(val)
  
        
    def pop(self) -> None:
        self.res.pop()
        self.minval.pop()
   
    def top(self) -> int:
        return self.res[-1]

     
    def getMin(self) -> int:
        return self.minval[-1]
     
    
        
