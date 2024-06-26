# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo={}

        for i in range(len(arr)-1, -1, -1):
            if arr[i]+difference in memo:
                memo[arr[i]]=memo[arr[i]+difference]+1
            else:
                memo[arr[i]]=1

        return max(memo.values())