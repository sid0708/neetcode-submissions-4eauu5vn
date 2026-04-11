from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res, value = "",self.cache.get(key, [])
        # binary search
        L, R = 0 , len(value) -1
        while L <=R:
            mid = (L+R) //2
            ts = value[mid][1]
            if ts <= timestamp:
                res = value[mid][0]
                L = mid+1
            else:
                R = mid -1
        return res



        
