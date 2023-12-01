class Solution(object):
    def romanToInt(self, s):
        dic={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result=0
        for i in range(len(s)):
            if (i+1)==len(s) or dic[s[i]]>=dic[s[i+1]]:
                result+=dic[s[i]]
            else:
                result-=dic[s[i]]
        return result

            
