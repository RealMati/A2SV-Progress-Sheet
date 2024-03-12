class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res=0
        before=0

        for upper,percent in brackets:
            res+= (min(upper,income)-before)*percent
            if upper>=income:
                break
            before=upper
        return res/100