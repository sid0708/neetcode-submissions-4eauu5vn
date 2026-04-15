class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) >1:
            first,second = heapq.heappop(stones), heapq.heappop(stones)
            heapq.heappush(stones, first-second)
        return -1 * stones[0]
                

        