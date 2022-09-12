class MagicDictionary:

    def __init__(self):
        self.lookup = collections.defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.lookup[len(word)].append(word)
        

    def search(self, searchWord: str) -> bool:
        if len(searchWord) in self.lookup.keys():
            for word in self.lookup[len(searchWord)]:
                if sum(a != b for a, b in zip(word, searchWord)) == 1:
                    return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
