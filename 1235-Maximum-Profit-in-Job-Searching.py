class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        lookup = []
        for i in range(len(profit)):
            lookup.append([startTime[i], endTime[i], profit[i]])
        lookup.sort()
        dp = {}
        
        def dfs(i):
            if i == len(startTime):
                return 0
            if (i) in dp:
                return dp[(i)]
            j = i + 1
            while j < len(startTime) and lookup[i][1] > lookup[j][0]:
                j += 1
            one = lookup[i][2] + dfs(j)
            two = dfs(i + 1)
            dp[(i)] = max(one, two)
            return dp[(i)]
        
        return dfs(0)
