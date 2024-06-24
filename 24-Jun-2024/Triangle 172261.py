# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res=0

        for i in range(len(triangle)-2, -1, -1):
            for t in range(len(triangle[i])):
                triangle[i][t]+=min(triangle[i+1][t], triangle[i+1][t+1])
            
        return triangle[0][0]