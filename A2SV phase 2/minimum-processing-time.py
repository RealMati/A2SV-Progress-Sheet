class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        processorTime.sort()
        tasks.sort()
        maxTime=0
        procidx=0

        
        for idx in range(len(tasks)-1,-1,-4):
            maxTime=max(maxTime, tasks[idx]+processorTime[procidx])
            procidx+=1

        return maxTime



        