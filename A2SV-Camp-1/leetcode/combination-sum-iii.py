class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        arr = []
        summ = 0

        def c(idx):
            nonlocal summ
            if summ == n and len(arr)==k:
                res.append(arr[:])
                return
            if summ > n or len(arr)>k:
                return

            for i in range(idx, 10):
                if summ + i > n:
                    break
                arr.append(i)
                summ += i
                c(i + 1)
                arr.pop()
                summ -= i

        c(1)
        return res
