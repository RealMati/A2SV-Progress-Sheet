class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lRow=lCol=0
        rRow=len(matrix)-1
        rCol=len(matrix[0])-1
        
        while lRow<=rRow:
            midRow=(lRow+rRow)//2

            if matrix[midRow][0]<=target<=matrix[midRow][-1]:
                last=midRow
                break
            elif matrix[midRow][-1]>target:
                rRow=midRow-1
            elif matrix[midRow][0]<target:
                lRow=midRow+1
            last=midRow
        # print("last",last)

        while lCol<=rCol:
            midCol=(lCol+rCol)//2

            if matrix[last][midCol] == target:
                return True
            elif matrix[last][midCol] < target:
                lCol=midCol + 1
            else:
                rCol=midCol - 1   
            # print(matrix[last][midCol])
            
        return False

