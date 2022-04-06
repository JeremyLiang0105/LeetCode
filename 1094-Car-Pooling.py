class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x : x[1])
        minHeap = [] # (end, numOfPass)
        curPass = 0
        
        for trip in trips:
            numPass = trip[0]
            start = trip[1]
            end = trip[2]
            while minHeap and minHeap[0][0] <= start:
                curPass -= minHeap[0][1]
                heapq.heappop(minHeap)
            curPass += numPass
            if curPass > capacity:
                return False
            heapq.heappush(minHeap, (end, numPass))
        return True
    
    # time complexity: O(nlogn)
    # space complexity: O(n)
