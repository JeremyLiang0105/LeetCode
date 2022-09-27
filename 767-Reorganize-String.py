class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)
        maxHeap = [[-value, key] for key, value in count.items()]
        heapq.heapify(maxHeap) # O(n)
        
        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            count, char = heapq.heappop(maxHeap)
            res += char
            count += 1
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if count != 0:
                prev = [count, char]
        return res
    # time complexity: O(nlogn)
    # space complexity: O(n)
