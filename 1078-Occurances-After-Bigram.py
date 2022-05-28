class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        stack = []
        
        text = text.split(" ")
        
        for c in text:
            if len(stack) > 1 and stack[-2] == first and stack[-1] == second:
                res.append(c)
            stack.append(c)
        return res
   
 # time complexity: O(n)
 # space complexity: O(n)
