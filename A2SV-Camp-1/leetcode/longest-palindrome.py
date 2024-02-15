class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=sorted((Counter(s)).values(), reverse=True)
        res=0
        longOdd=None

        for i in count:
            if i%2==0:
                res+=i
            elif not longOdd:
                res+=i
                longOdd=i
            else:
                res+=(i-1)            
        # print(count)
        return res