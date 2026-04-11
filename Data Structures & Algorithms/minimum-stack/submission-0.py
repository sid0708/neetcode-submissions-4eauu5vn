class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        val = self.arr.pop()
        return val

        
    def top(self) -> int:
        if not self.arr:
            pass
        return self.arr[-1]
  
        
    def getMin(self) -> int:
        if not self.arr:
            pass
        return sorted(self.arr)[0]
