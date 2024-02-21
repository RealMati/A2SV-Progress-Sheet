class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0: return [1]

        def pascal(arr,rowIndex):
            if rowIndex==0: return arr
            
            res=[1]
            for i in range(len(arr)-1):
                res.append(arr[i]+arr[i+1])
            res.append(1)
            
            return pascal(res,rowIndex-1)
        return pascal([1],rowIndex)

            