class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        dic=defaultdict(int)
        count=0

        for answer in answers:
            if not dic[answer]:
                count+=answer+1
            if dic[answer]<answer+1:
                dic[answer]+=1
            else:
                dic[answer]=1
                count+=answer+1

        return count