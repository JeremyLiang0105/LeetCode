class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        res = []
        lookup = {}
        
        for n in nums:
            lookup[n] = 1 + lookup.get(n, 0)
            
        for key in lookup:
            heapq.heappush(maxHeap, (-lookup[key], key))
            
        for i in range(k):
            count, num = heapq.heappop(maxHeap)
            res.append(num)
        return res
    # time complexity: O(nlogn)
    # space complexity: O(n)
