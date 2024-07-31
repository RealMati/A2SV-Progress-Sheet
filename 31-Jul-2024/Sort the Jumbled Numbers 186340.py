# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        for idx,num in enumerate(nums):
            mapped=0
            for dig in str(num):
                mapped = (mapped * 10) + mapping[int(dig)]

            nums[idx]=[mapped, num]

        pos={num[1]:idx for idx,num in enumerate(nums)}
        nums.sort(key=lambda x: (x[0], pos[x[1]]) )

        for idx,num in enumerate(nums):
            nums[idx]=nums[idx][1]
    
        return nums