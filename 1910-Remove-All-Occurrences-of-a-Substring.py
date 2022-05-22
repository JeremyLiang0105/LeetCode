class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        temp = ""
        
        for i in range(len(s)):
            temp += s[i]
            if len(temp) >= len(part):
                if temp[(len(temp) - len(part)):] == part:
                    temp = temp[:len(temp) - len(part)]
        return temp
    
    # time complexity: O(n)
    # space complexity: O(n)
