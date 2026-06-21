class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = math.sqrt(self.x**2 + self.y **2)

    def __lt__(self, other):
        return self.dist < other.dist


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ps = []
        
        for point in points:
            heapq.heappush(ps,Point(point[0],point[1]))

        ans = []
        i = 0
        
        while k > 0:
            k-=1
            p = heapq.heappop(ps)
            ans.append([p.x,p.y])
        
        return ans