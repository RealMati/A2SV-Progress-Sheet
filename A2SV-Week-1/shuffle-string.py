class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr=[0]*len(s)
        for i,ind in enumerate(indices):
            arr[ind]=s[i]
        return "".join(arr)
