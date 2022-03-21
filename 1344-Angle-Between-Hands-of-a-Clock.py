class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_degree = (minutes / 60.0) * 360
        hour_degree = (((hour + minutes / 60.0) / 12.0) * 360) % 360
        return min(abs(min_degree - hour_degree), 360 - abs(min_degree - hour_degree))
