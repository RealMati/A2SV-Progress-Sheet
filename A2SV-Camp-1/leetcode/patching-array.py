class Solution:
	def minPatches(self, nums: List[int], n: int) -> int:
		ans, summ = 0, 0
		idx = 0

		while summ < n:
			if idx < len(nums):
				if summ < nums[idx] - 1:
					summ = summ * 2 + 1
					ans += 1
				else:
					summ += nums[idx]
					idx += 1
			else:
				summ = summ * 2 + 1
				ans += 1
                
		return ans