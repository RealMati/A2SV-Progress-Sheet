class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        repeated=set()

        for idx,chr in enumerate(s):
            if chr not in dic:
                dic[chr]=idx
            else:
                repeated.add(chr)
        
        minn = float('inf')
        
        for chr in dic:
            if chr not in repeated:
                minn=min(minn, dic[chr])
        
        if minn==float('inf'):
            return -1
        return minn
