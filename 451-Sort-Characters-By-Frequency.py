class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        lookup = {}
        res = ""
        for c in s:
            lookup[c] = 1 + lookup.get(c, 0)
        
        for key, val in sorted(lookup.items(), key = lambda x:x[1], reverse = True):
            res += key * val
        return res
        '''
        lookup = {}
        maxHeap = []
        res = ""
        
        for c in s:
            lookup[c] = 1 + lookup.get(c, 0)
        
        for key in lookup:
            maxHeap.append((-lookup[key], key))
        heapq.heapify(maxHeap)
        
        while maxHeap:
            value, key = heapq.heappop(maxHeap)
            res += -1 * value * key
        return res
    
    # heap
    # top() -> O(1)
    # insert() -> O(logn)
    # remove() -> O(logn)
    # heapify() -> O(n)
