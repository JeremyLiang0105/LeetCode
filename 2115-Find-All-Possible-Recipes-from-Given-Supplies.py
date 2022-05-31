class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        q = deque()
        
        for supply in supplies:
            indegree[supply] = 0
            q.append(supply)
            
        for i, r in enumerate(recipes):
            for ing in ingredients[i]:
                graph[ing].append(r)
                indegree[r] += 1
        
        res = []
        while q:
            node = q.popleft()
            if node in recipes:
                res.append(node)
            for n in graph[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
                    
        return res
                            '''
                            drawing explaination
                            
                              yeast (indegree: 0)
                               /
                              /
                            bread (indegree: 2)
                           /   \
                          /     \
                         /    flour (indegree: 0)
                        / 
                    sandwich (indegree: 2)
                        \
                         \
                         meat (indegree: 0)
                        '''
