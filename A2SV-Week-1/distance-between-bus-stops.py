class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        total_distance = sum(distance)

        #swapping if the start is greater than the destination
        if start > destination:
            start, destination = destination, start

        direct_path = sum(distance[start:destination])
        indirect_path = total_distance - direct_path

        return min(indirect_path, direct_path)
        