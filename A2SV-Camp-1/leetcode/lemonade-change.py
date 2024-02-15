class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic=defaultdict(int)

        for bill in bills:
            if bill==5:
                dic[5]+=1
            elif bill==10:
                if dic[5]:
                    dic[5]-=1
                    dic[10]+=1
                else:
                    return False
            else:
                if dic[10] and dic[5]:
                    dic[10]-=1
                    dic[5]-=1
                    dic[20]+=1
                elif dic[5]>=3:
                    dic[5]-=3
                    dic[20]+=1
                else:
                    return False
        return True
            

