# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """

        direction=[(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1),(0,0)]
        res=[[0]*len(img[0]) for _ in range(len(img))]
        for row in range(len(img)):
            for column in range(len(img[0])):
                sum=ct=0

                for x,y in direction:
                    if 0<=row+x<len((img)) and 0<=column+y<len((img[0])):
                        sum+=img[row+x][column+y]
                        ct+=1
                #         print(img[row+x][column+y])
                # print("_")
                res[row][column]=sum//(ct)
        return res


        