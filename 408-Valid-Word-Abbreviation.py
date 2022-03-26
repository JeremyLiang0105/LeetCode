class Solution:
    def valid_word_abbreviation(self, word: str, abbr: str) -> bool:
        
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                if 48 < ord(abbr[j]) <= 57:
                    tmp = ord(abbr[j]) - 48
                    while j + 1 < len(abbr) and 48 <= ord(abbr[j + 1]) <= 57:
                        tmp = 10 * tmp + (ord(abbr[j + 1]) - 48)
                        j += 1
                    j += 1
                    i += tmp
                else:
                    return False
        return i == len(word) and j == len(abbr)
