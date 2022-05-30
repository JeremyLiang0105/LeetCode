class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        N = len(words)
        l = 0
        
        while l < N:
            total = len(words[l])
            r = l + 1
            while r < N:
                if total + len(words[r]) + 1 > maxWidth:
                    break
                total += (len(words[r]) + 1)
                r += 1
            gaps = r - l - 1
            temp = ""
            
            if (r == N or gaps == 0):
                for i in range(l, r):
                    temp += words[i]
                    if i != r - 1:
                        temp += " "
                while len(temp) < maxWidth:
                    temp += " "
            else:
                # totalChars = word1 + space + word2 + space + word3
                # spaces = (maxWidth - total) // gaps
                # rest = (maxWidth - total) % gaps
                spaces = (maxWidth - total) // gaps
                rest = (maxWidth - total) % gaps
                for i in range(l, r - 1):
                    temp += words[i]
                    temp += " "
                    if i - l < rest:
                        c = spaces + 1
                    else:
                        c = spaces
                    for j in range(c):
                        temp += " "
                temp += words[r - 1]
            res.append(temp)
            l = r
        return res
