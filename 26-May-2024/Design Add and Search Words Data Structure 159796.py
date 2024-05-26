# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.trie = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end=True

    def search(self, word: str) -> bool:
        def dfs(curr,i):
            if i==len(word):
                return curr.end
            
            if word[i]=='.':
                for child in curr.children.values():
                    if dfs(child,i+1):
                        return True
                return False

            if word[i] not in curr.children:
                return False
                
            return dfs(curr.children[word[i]],i+1)
  

        return dfs(self.trie,0)
                
            


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)