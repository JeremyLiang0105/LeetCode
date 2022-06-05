class Solution:
    
    def minimum_cost(self, sticks: List[int]) -> int:
        # write your code here
        minHeap = [stick for stick in sticks]
        heapq.heapify(minHeap)
        res = 0

        while len(minHeap) > 1:
            one = heapq.heappop(minHeap)
            two = heapq.heappop(minHeap)
            new = one + two
            res += new
            heapq.heappush(minHeap, new)
        return res
    # time complexity: O(nlogn)
