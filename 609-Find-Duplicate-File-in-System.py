class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        lookup = collections.defaultdict(list)
        
        for path in paths:
            path = path.split(" ")
            folder = path[0]
            for s in path[1:]:
                s = s.split(".txt")
                name = s[0]
                content = s[1]
                lookup[content].append((folder, name))
        
        res = []
        
        for key, value in lookup.items():
            if len(value) > 1:
                temp = []
                for path, name in value:
                    temp.append(path + "/" + name + ".txt")
                res.append(temp)
        return res
