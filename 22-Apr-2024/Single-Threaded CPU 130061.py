# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort()
        time=tasks[0][0]
        heap=[]
        res=[]
        print(tasks, time)
        i=0
        while i<len(tasks):
            if tasks[i][0]<=time:
                heappush(heap, (tasks[i][1], tasks[i][2]))
                i+=1
            else:
                dur, idx = heappop(heap)

                time+=dur
                if not heap:
                    time=max(time, tasks[i][0])
                    
                res.append(idx)

        while heap:
            dur, idx = heappop(heap)
            res.append(idx)
        

        return res
