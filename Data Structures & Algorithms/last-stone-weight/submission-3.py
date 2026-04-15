class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        total, stack = 0, []
        while len(stones) > 1:
            stones.sort()
            x,y = stones.pop(), stones.pop()
            if x == y:
                total = 0
            if y >x:
                total = y-x
            else:
                total = x-y
            stones.append(total)
        return stones[0]
        