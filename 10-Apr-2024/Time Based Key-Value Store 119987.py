# Problem: Time Based Key-Value Store - https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.dic=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # if key not self.dic: return ""
        l=0
        r=len(self.dic[key])-1

        def check(mid):
            if self.dic[key][mid][0]<=timestamp:
                return True
            else:
                return False

        last=""
        while l<=r:
            mid=(l+r)//2
            # print(mid)
            if check(mid):
                last=self.dic[key][mid][1]
                l=mid+1
            else:
                r=mid-1

        # print(self.dic[key],l,last,"t=",timestamp)
        return last 

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)