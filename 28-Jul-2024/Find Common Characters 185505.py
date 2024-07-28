# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        for i in words[0]:
            if i not in res:
                minn=words[0].count(i)
                for word in words[1:]:
                    minn=min(word.count(i),minn)
                res+=[i]*minn
        return res