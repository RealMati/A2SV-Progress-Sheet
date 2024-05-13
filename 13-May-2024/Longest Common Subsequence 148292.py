# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res=0
        memo={}

        def dp(i,j):
            state=(i,j)

            if state in memo:
                return memo[state]

            if i==len(text1) or j==len(text2):
                return 0

            if text1[i]==text2[j]: 
                memo[state]=1+dp(i+1, j+1)
            else:
                memo[state]=max(dp(i+1, j), dp(i, j+1))
            return memo[state]

        return dp(0,0)
