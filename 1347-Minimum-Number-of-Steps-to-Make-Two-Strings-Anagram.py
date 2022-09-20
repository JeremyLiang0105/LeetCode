from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = Counter(s)
        c2 = Counter(t)
        for k, v in c1.items():
            if k in c2:
                v2 = c2[k]
                if v2 > v:
                    c2[k] -= v
                else:
                    del c2[k]
        return sum(c2.values())
