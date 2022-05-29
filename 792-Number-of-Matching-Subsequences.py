class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        '''
        res = 0
        for word in words:
            if len(word) > len(s):
                continue
            if self.helper(s, word):
                res += 1
        return res

    def helper(self, s, word):
        i, j = 0, 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
        return True if j == len(word) else False
        '''
        lookup = defaultdict(list)
        for word in words:
            lookup[word[0]].append(word)
        
        ans = 0
        for c in s:
            strs = lookup[c]
            lookup[c] = []
            for part in strs:
                if len(part) == 1:
                    ans += 1
                else:
                    lookup[part[1]].append(part[1:])
        
        return ans
