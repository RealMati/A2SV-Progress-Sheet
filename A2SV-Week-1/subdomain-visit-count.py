class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        

        from collections import defaultdict
        repetition=defaultdict(int)

        for repdomain in cpdomains:
            domain=repdomain.split()
            domain[0]=int(domain[0])
            web=domain[1].split(".")
            for cur in range(len(web)):
                repetition[".".join(web[cur:])]+=domain[0]
                cur+=1
        res=[]
        for key,value in repetition.items():
            res.append(str(value)+" "+str(key))

        return res