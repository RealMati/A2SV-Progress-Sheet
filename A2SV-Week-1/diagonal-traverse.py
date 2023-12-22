class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
          
        res=[mat[0][0]]
        point=[0,0]
        up=True
        while point!=[len(mat)-1,len(mat[0])-1]:
            if up:
                if point[1]+1>=len(mat[0]):
                    point[0]+=1
                    up=False
                    res.append(mat[point[0]][point[1]])
                    continue
                
                elif point[0]-1<0:
                    point[1]+=1
                    up=False
                    res.append(mat[point[0]][point[1]])
                    continue
                else:
                    point=[point[0]-1,point[1]+1]
                    res.append(mat[point[0]][point[1]])
            else:
                if point[0]+1>=len(mat):
                    point[1]+=1
                    up=True
                    res.append(mat[point[0]][point[1]])
                    continue
                
                elif point[1]-1<0:
                    point[0]+=1
                    up=True
                    res.append(mat[point[0]][point[1]])
                    continue
                else:
                    point=[point[0]+1,point[1]-1]
                # print(point)
                    res.append(mat[point[0]][point[1]])

        # res.append(point[len(mat)-1][]
        return res





