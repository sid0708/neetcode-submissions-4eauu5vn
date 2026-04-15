class MedianFinder:

    def __init__(self):
        self.arr = []
        
    def addNum(self, num: int) -> None:
        self.arr.append(num)
        
    def findMedian(self) -> float:
        self.arr.sort()
        n =len(self.arr)
        if n %2 == 0:
            mid1 = n//2
            mid2 = mid1-1
            mid = (self.arr[mid1]+ self.arr[mid2]) /2
            return mid     
        else:
            mid = n//2
            return self.arr[mid]

        
        