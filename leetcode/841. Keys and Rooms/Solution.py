class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        availableRooms = set()
        availableRooms.add(0)
        
        quene = [0]
        while quene:
            currentRoom = quene[0]
            availableRooms.add(currentRoom)
            for room in rooms[currentRoom]:
                if room in availableRooms:
                    continue
                else:
                    availableRooms.add(room)
                    quene.append(room)
            quene = quene[1:]

        return len(rooms) == len(availableRooms)
