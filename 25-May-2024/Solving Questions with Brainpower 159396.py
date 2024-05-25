# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo={}

        def dp(idx):
            state=(idx)

            if state in memo:
                return memo[state]
            
            if idx>=len(questions):
                return 0

            pick=questions[idx][0]+dp(idx+questions[idx][1]+1)
            notpick=dp(idx+1)
                  
            memo[state]=max(pick,notpick)
            return memo[state]

        return dp(0)