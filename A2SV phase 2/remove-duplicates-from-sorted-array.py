class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited=set()

        for idx,num in enumerate(nums):
            if num in visited:
                nums[idx]="_"
            else:
                visited.add(num)
        
        read=write=0
    
        while read<len(nums):
            if nums[read]!="_":
                nums[read],nums[write]=nums[write],nums[read]
                read+=1
                write+=1
            else:
                read+=1
        
        return len(visited)

        