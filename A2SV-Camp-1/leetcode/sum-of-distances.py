class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dic=defaultdict(list)
        res=[0]*len(nums)
        
        for idx,num in enumerate(nums):
            dic[num].append(idx)

        for key in dic:
            prefix=[dic[key][0]]

            for i in range(1,len(dic[key])):
                prefix.append(prefix[-1]+dic[key][i])

            for idx,num in enumerate(dic[key]):
                if idx-1>=0:
                    left=abs(prefix[idx-1]-(idx*num))
                else:
                    left=0

                right=abs((prefix[-1]-prefix[idx])-(len(dic[key])-idx-1)*num)

                if len(dic[key])==1: res[num]=0
                else: res[num]=left+right
                
        return res