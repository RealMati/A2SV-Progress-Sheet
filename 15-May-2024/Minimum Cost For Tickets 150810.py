# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}

        def dp(idx, until):
            state = (idx, until)

            if state in memo:
                return memo[state]

            if idx == len(days):
                return 0

            if days[idx] < until:
                memo[state] = dp(idx + 1, until)

            else:
                memo[state] = min(
                    costs[0] + dp(idx + 1, days[idx] + 1),
                    costs[1] + dp(idx + 1, days[idx] + 7),
                    costs[2] + dp(idx + 1, days[idx] + 30),
                )

            return memo[state]
        return dp(0, days[0])
