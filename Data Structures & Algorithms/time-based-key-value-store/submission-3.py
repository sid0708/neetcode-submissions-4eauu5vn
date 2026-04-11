from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)
       
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # extract the list of values
        res, values = "", self.cache.get(key, [])
        print(values)
        # use binary search
        L, R = 0, len(values) -1
        while L <=R:
            mid = (L+R)//2
            ts = values[mid][1]
            print("Ts is", ts)
            if ts <= timestamp:
                res = values[mid][0]
                L = mid +1
            else:
                R = mid -1
        return res


        
