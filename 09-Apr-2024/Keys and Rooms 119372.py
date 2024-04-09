# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph={}

        for idx,room in enumerate(rooms):
            graph[idx]=room
        visited=set([0])
        q=deque([0])
        
        while q:
            cur=q.popleft()

            for nbs in graph[cur]:
                if nbs not in visited:
                    q.append(nbs)
                    visited.add(nbs)

        return len(visited)==len(rooms)
                
        
                