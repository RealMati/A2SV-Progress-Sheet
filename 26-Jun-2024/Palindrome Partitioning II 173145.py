# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        memo={}
        @cache
        def isPalindrome(i, j):
            if i>j:
                return True
            if s[i] == s[j]:
                return isPalindrome(i+1, j-1)
            else:
                return False

        def dp(idx):
            state=(idx)

            if state in memo:
                return memo[state]
            
            if idx==len(s):
                return 0

            # print(s)
            ans=float('inf')
            for i in range(idx+1, len(s)+1):
                # segment=st[idx:i]

                if isPalindrome(idx, i-1):
                    ans=min(ans, 1+dp(i))

            memo[state]=ans
            return memo[state]

        res=dp(0)-1
        # print(memo)
        return res