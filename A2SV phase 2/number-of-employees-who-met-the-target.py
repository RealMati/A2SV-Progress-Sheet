class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        ct=0
        for hour in hours:
            if hour>=target:
                ct+=1
            
        return ct