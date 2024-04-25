# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        person = {}
        parent = {}

        def find(x):
            cur = x
            while cur != parent[cur]:
                cur = parent[cur]

            return cur

        def union(p, a, b):
            if a not in parent:
                parent[a] = a
            if b not in parent:
                parent[b] = b

            parentA = find(a)
            parentB = find(b)

            parent[parentB] = parentA

        for i in range(len(accounts)):
            p = accounts[i][0]
            m1 = accounts[i][1]
            #### check if d/t person same name
            person[m1] = p
            if m1 not in parent:
                parent[m1] = m1

            for j in range(2, len(accounts[i])):
                m2 = accounts[i][j]
                union(p, m1, m2)
                m1 = m2

        print(parent)
        print(person)
        res = {}
        for key in person:
            res[find(key)] = [person[key],[]]

        print("RES", res)
        for key in parent:
            print(key)
            p = find(key)
            print(p)
            res[p][1].append(key)
        
        ress=[]
        for key in res:
            ress.append([res[key][0]])
            ress[-1].extend(sorted(res[key][1]))

        # print(ress)
        return ress
