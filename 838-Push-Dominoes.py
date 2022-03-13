class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        q = deque()
        
        for i, v in enumerate(dom):
            if v != ".":
                q.append((i, v))
        
        while q:
            i, d = q.popleft()
            if d == "L":
                if i - 1 >= 0 and dom[i - 1] == ".":
                    q.append((i - 1, "L"))
                    dom[i - 1] = "L"
            elif d == "R":
                if i + 1 < len(dom) and dom[i + 1] == ".":
                    if i + 2 < len(dom) and dom[i + 2] == "L":
                        q.popleft()
                    else:
                        q.append((i + 1, "R"))
                        dom[i + 1] = "R"
        return "".join(dom)
    
    # time complexity: O(n) because the worst case is that every single dominoe could be added to the queue
    # space complexity: O(n)
