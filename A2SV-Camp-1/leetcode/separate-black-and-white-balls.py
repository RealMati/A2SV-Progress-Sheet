class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros=swaps=0

        for idx in range(len(s)):
            if s[idx]=='0':
                swaps+=(idx-zeros)
                zeros+=1

        return swaps
