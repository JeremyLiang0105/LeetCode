class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        lst = list(s)
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            if s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    lst[i] = ""
    
        for index in stack:
            lst[index] = ""
        return "".join(lst)
      
      # time complexity: O(n)
      # space complexity: O(n)
