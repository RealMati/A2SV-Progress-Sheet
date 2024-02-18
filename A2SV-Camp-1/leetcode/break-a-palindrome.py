class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        res = []
        res.extend(palindrome)

        if n==1:
            return ""
        if n%2:
            odd=n//2
        else: odd=None

        for i in range(n):
            if i==odd: continue

            if palindrome[i]!='a':
                res[i]='a'
                #print('in')
                return "".join(res)
      #print(res)
        res[-1]='b'
        return "".join(res)

            
