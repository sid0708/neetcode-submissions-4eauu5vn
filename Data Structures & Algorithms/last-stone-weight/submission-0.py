class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) >1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # since we are delaing with negatives
            # and minimum heap we will do the inverse to
            # keep the negative
            if second > first:
                heapq.heappush(stones, first-second)
        # edge case if there is no stone append zero
        stones.append(0)
        return abs(stones[0])
         
        