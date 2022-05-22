class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # store a pair [char, count]
        
        for i in range(len(s)):
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += 1
            else:
                stack.append([s[i], 1])
            
            if stack and stack[-1][1] == k:
                stack.pop()
        
        return "".join(cnt * char for char, cnt in stack)
    
    # time complexity: O(n)
    # space complexity: O(n)
