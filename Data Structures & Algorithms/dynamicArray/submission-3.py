class DynamicArray:
    
    def __init__(self, capacity: int):
        # Constructor start with the size = 0
        self.size = 0
        self.capacity = capacity 
        self.arr = [0] * self.capacity


    def get(self, i: int) -> int:
        # Get the value at index, i
        if i > self.size:
            raise "Inavlid Index"
        return self.arr[i]
        


    def set(self, i: int, n: int) -> None:
        # Set value n at index i
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        # Push back the value n at the last index
        # check if already at capacity
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size +=1


    def popback(self) -> int:
        if self.size > 0:
            # decerese the size by one
            self.size -= 1
        return self.arr[self.size]
 

    def resize(self) -> None:
        # Create a new array double the capacity
        # Also copy over the content of the original array to new array
        # assign the new array to the old array
        self.capacity = 2 * self.capacity
        # initialize new array with twice 
        new_arr = [0] * self.capacity
        
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        # new_arr has been copied over and double the size
        self.arr = new_arr


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity