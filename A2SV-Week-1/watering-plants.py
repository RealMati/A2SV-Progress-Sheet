class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps=0
        cur_capacity=capacity
        cur_index=-1
        for ind,water_need in enumerate(plants):
            if water_need<=cur_capacity:
                steps+=ind-cur_index
                cur_capacity-=water_need
                cur_index=ind
            else:
                steps+=cur_index+1
                cur_capacity=capacity
                steps+=ind+1
                cur_capacity-=water_need
                cur_index=ind
        return steps
