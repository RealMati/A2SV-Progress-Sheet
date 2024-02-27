class Solution:
    def letterCombinations(self, dig: str) -> List[str]:
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = ""
        res = []
        if not dig:
            return []

        def c(idx):
            nonlocal ans
            if idx >= len(dig):
                res.append(ans)
                return

            for i in range(len(dic[dig[idx]])):
                ans+=dic[dig[idx]][i]
                c(idx + 1)
                ans=ans[:-1]

        c(0)
        return res
