# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Trie:
    def __init__(self):
        self.children = {}
        self.end = False


class Solution:
    def __init__(self):
        self.root = Trie()

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()

        for word in dictionary:
            cur = self.root
            for c in word:
                idx = ord(c) - ord("a")

                if idx not in cur.children:
                    cur.children[idx] = Trie()

                cur = cur.children[idx]
            cur.end = True

        def dfs(cur, idx, word):
            if cur.end:
                return word[:idx]
            if idx == len(word):
                return word

            i = ord(word[idx]) - ord("a")

            if i not in cur.children:
                return word
            else:
                return dfs(cur.children[i], idx + 1, word)

        for i in range(len(words)):
            words[i] = dfs(self.root, 0, words[i])
        return " ".join(words)
