# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Trie:
    def __init__(self,val):
        self.children = {}
        self.val=val
        self.end = False


class Solution:
    def __init__(self):
        self.root = Trie("")

    def longestWord(self, words: List[str]) -> str:
        
        for word in words:
            cur = self.root
            for c in word:
                idx = ord(c) - ord("a")

                if idx not in cur.children:
                    cur.children[idx] = Trie(c)

                cur = cur.children[idx]
            cur.end = True

        maxx=""
        def dfs(cur, ans, count):
            nonlocal maxx
            ans+=cur.val
            if cur.end and count==len(ans)-1:
                if len(ans)>len(maxx):
                    maxx=ans
                elif len(ans)==len(maxx):
                    maxx=min(maxx, ans)

            if cur.end:
                count+=1

            for child in cur.children:
                dfs(cur.children[child], ans, count)
        
        dfs(self.root, "", 0)
        return maxx
           
           
