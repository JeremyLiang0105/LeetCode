class Solution:
    def countPoints(self, rings: str) -> int:
        lookup = collections.defaultdict(set)
        res = 0
        visited = set()
        for i in range(0, len(rings), 2):
            lookup[rings[i + 1]].add(rings[i])
            if len(lookup[rings[i + 1]]) == 3 and rings[i + 1] not in visited:
                res += 1
                visited.add(rings[i + 1])
        return res
    
    '''
        ans = 0
        for i in range(10):
            i = str(i)
            if 'R' + i in rings and 'G' + i in rings and 'B' + i in rings:
                ans += 1
        return ans
    ''' 
