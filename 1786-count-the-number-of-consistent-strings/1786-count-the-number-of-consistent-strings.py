class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        lst = list()
        lst.extend(allowed)
        for i in words:
            aylan = 0
            for j in i:
                if j in lst:
                    aylan += 1
                else:
                    break
            if aylan == len(i):
                count += 1
        return count
