class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Djikstra algorigthm - shortest path graph
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((w, v))
        
        minHeap = [(0, k)]
        visited = set()
        res = 0
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            res = max(res, w1)
            for w2, n2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return res if len(visited) == n else -1
    
    # time complexity: O(E*logV)
