class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        nums=deque()
        deck.sort(reverse=True)

        for num in deck:
            if nums:
                a=nums.pop()
                nums.appendleft(a)
            nums.appendleft(num)
            # print(nums,num)
        return nums
