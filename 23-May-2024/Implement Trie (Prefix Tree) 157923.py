# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.end=False
        self.children=[None for i in range(26)]
class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            idx=ord(c)-ord("a")
            if not cur.children[idx]:
                cur.children[idx]=TrieNode()
            cur=cur.children[idx]
        cur.end=True
        

    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            idx=ord(c)-ord("a")
            if not cur.children[idx]:
                return False
            cur=cur.children[idx]
        return True==cur.end

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            idx=ord(c)-ord("a")
            if not cur.children[idx]:
                return False
            cur=cur.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)