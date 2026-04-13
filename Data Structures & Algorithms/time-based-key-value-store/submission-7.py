class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list) # (value, timestamp)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.cache.get(key, [])
        res= ""
        # [(happy, 4), (sad,5), (timestamp,6)]
        L = 0
        R = len(values) -1
        while L <= R:
            mid = (L + R)//2
            if values[mid][1] > timestamp:
                R = mid -1
            elif values[mid][1] <= timestamp:
                res = values[mid][0]
                L = mid+1
        return res

        
