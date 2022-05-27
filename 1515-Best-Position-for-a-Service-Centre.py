class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def helper(a, b):
            res = 0
            for x, y in positions:
                res += math.sqrt((x - a)**2 + (y - b)**2)
            return res
        
        
        startX = 0
        startY = 0
        
        for x, y in positions:
            startX += x
            startY += y
        startX /= len(positions)
        startY /= len(positions)
        curDist = helper(startX, startY)
        
        step = 1
        while step > 0.000001:
            flag = True
            for dx, dy in [(0, step), (0, -step), (step, 0), (-step, 0)]:
                newX = startX + dx
                newY = startY + dy
                temp = helper(newX, newY)
                if temp < curDist:
                    curDist = temp
                    startX, startY = newX, newY
                    flag = False
            if flag:
                step /= 10
        return curDist
