class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # prefix=[[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
        ct=0


        for row in range(len(matrix)):
            for col in range(1,len(matrix[0])):
                # prefix[row][col] = matrix[row-1][col-1] + prefix[row-1][col] + prefix[row][col-1] - prefix[row-1][col-1]
                matrix[row][col]+=matrix[row][col-1]
                
                # dic[prefix[row][col]].append([row,])
        for start in range(len(matrix[0])):
            for end in range(start, len(matrix[0])):
                dic={0:1}
                summ=0

                for row in range(len(matrix)):
                    summ+=matrix[row][end] - (matrix[row][start-1] if start-1>=0 else 0)

                    if summ-target in dic:
                        ct+=dic[summ-target]
                    if summ not in dic:
                        dic[summ]=1
                    else:
                        dic[summ]+=1
        return ct

            
                    
