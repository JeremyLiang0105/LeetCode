class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        '''
        # brute force
        taken = []
        res = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                taken.append(i)
        
        for i in range(len(seats)):
            if seats[i] == 0:
                tmp = float("inf")
                for pos in taken:
                    tmp = min(tmp, abs(pos - i))
                res = max(res, tmp)
        return res
        '''
        
        
        prevSeat = -1
        dist = float("-inf")
        
        for i in range(len(seats)):
            if seats[i] == 1:
                if prevSeat == -1:
                    dist = i
                else:
                    dist = max(dist, (i - prevSeat) // 2)
                prevSeat = i
        dist = max(dist, len(seats) - 1 - prevSeat)
        return dist
