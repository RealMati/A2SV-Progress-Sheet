# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph=defaultdict(list)
        indegree=defaultdict(int)
        supplies=set(supplies)
        
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])
                indegree[recipes[i]]+=1

        # print(graph)
        # print(indegree)

        q=deque()
        res=[]
        visited=set()
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                if indegree[ing]==0:
                    if ing in supplies and ing not in visited:
                        q.append(ing)
                        visited.add(ing)
                        if ing in recipes:
                            res.append(ing)
        
        while q:
            for _ in range(len(q)):
                ing=q.popleft()

                for rec in graph[ing]:
                    if ing not in graph[rec]:
                        indegree[rec]-=1
                        # print(ing, graph[ing])
                        if indegree[rec]==0:
                            
                            q.append(rec)
                            res.append(rec)
            
        return res

        
