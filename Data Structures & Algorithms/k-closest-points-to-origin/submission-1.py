class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        X = math.sqrt(self.x**2 + self.y **2)
        Y = math.sqrt(other.x**2 + other.y **2)
        print(X,Y)
        return X < Y
    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return f"({self.x},{self.y})"


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