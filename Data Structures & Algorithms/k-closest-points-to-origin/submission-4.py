class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for cor in points:
            distance = (cor[0]) ** 2 + (cor[1]) **2
            minHeap.append([distance, cor[0], cor[1]])
        heapq.heapify(minHeap)
        while k >0:
            dist,x,y = heapq.heappop(minHeap)
            res.append([x,y])
            k -=1
        return res
        