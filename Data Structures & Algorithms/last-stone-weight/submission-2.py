class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=stones[:]
        heapq.heapify_max(heap)
        while(len(heap)>1):
            a,b=heapq.heappop_max(heap),heapq.heappop_max(heap)
            a = a-b
            if a :
                heapq.heappush_max(heap, a)
        if not heap:
            return 0
        return heap[0]