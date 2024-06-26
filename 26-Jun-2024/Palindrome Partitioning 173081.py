# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo={}

        def isPalindrome(st):
            return st==st[::-1]

        def dp(s):
            state=(s)

            if state in memo:
                return memo[state]
            
            if not s:
                return [[]]

            # print(s)
            ans=[]
            for i in range(1, len(s)+1):
                segment=s[:i]

                if isPalindrome(segment):
                    for pals in dp(s[i:]):
                        ans.append([segment]+pals)

            memo[s]=ans
            # print(memo)
            return memo[s]

 
        return dp(s)