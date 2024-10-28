class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        n = len(edges)
        freq = [0] * (n + 2)
        for a,b in edges:
            freq[a] += 1
            freq[b] += 1
        for i in range(1, n + 2):
            if freq[i] == n:
                return i

        return 0    
