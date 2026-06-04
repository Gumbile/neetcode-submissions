class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        points = []
        for i,pos in enumerate(position):
            points.append([pos,speed[i]])



        points.sort(reverse=True,key= lambda x:x[0])

        # print(points)

        prevArival  = (target - points[0][0]) / points[0][1]
        numOfFleets = 1

        for point in points:
            arrival = (target - point[0]) / point[1]

            if arrival > prevArival:
                numOfFleets+=1 
                prevArival = arrival


        return numOfFleets 