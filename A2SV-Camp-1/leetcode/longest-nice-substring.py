class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def c(string):
            freq = set(string)
            for idx, ch in enumerate(string):
                if ch.swapcase() not in freq:
                    right = c(string[idx + 1 :])
                    left = c(string[:idx])
                    # print(right, left)
                    if len(left) >= len(right):
                        return left
                    else:
                        return right
            return string
        return c(s)
