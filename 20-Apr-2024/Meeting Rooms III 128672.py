# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms=[]
        freeRooms=[]
        counter=defaultdict(int)

        for i in range(n):
            freeRooms.append((0,i))

        heapq.heapify(rooms)
        heapq.heapify(freeRooms)
        meetings.sort()
        t=meetings[0][0]

        for start, end in meetings:
            if not freeRooms and rooms and start<rooms[0][0]:
                t=max(t,rooms[0][0])
            else:
                t=max(t,start)

            while rooms and rooms[0][0]<=t:
                finish, room = heappop(rooms)
                heappush(freeRooms, (0, room))


            if start<=t and freeRooms:
                finish, room = heappop(freeRooms)
                heappush(rooms, (end+t-start, room))
                counter[room]+=1
                # print(rooms, meetings, t)
            # print(rooms, t)
            
            
        
        # print(counter)
        maxx=max(counter.values())
        res=float('inf')

        for key in counter:
            if counter[key]==maxx:
                res=min(key, res)
        return res
        


