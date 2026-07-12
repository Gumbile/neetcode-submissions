class MedianFinder:

    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        if len(self.lo) == len(self.hi):
            heapq.heappush(self.hi,-heapq.heappushpop(self.lo,-num))
        else:
            heapq.heappush(self.lo,-heapq.heappushpop(self.hi,num))


    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return float(self.hi[0] - self.lo[0]) / 2.0
        else:
            return float(self.hi[0])
        