class Solution:
    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
        res = []
        cand.sort()
        arr = []
        summ = 0

        def c(idx):
            nonlocal summ
            if summ == target:
                res.append(arr[:])
                return
            if summ > target:
                return

            for i in range(idx, len(cand)):
                if i != idx and cand[i] == cand[i - 1]:
                    continue
                if summ + cand[i] > target:
                    break
                arr.append(cand[i])
                summ += cand[i]
                c(i + 1)
                arr.pop()
                summ -= cand[i]

        c(0)
        return res
