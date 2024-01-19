class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        value=skill[0]+skill[len(skill)-1]
        res=0

        for l in range(len(skill)//2):
            if skill[l]+skill[len(skill)-1-l]==value:
                res+=(skill[l]*skill[len(skill)-1-l])
            else:
                return -1
        
        return res
        