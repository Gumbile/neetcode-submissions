class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap:
            self.maxHeap.append(-num)
            return
        
        if num > -self.maxHeap[0]:
            heapq.heappush(self.minHeap,num)
        else:
            heapq.heappush(self.maxHeap,-num)

        self.fixHeaps()

        
    def fixHeaps(self):
        if len(self.minHeap) > len(self.maxHeap):
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, - num)
        
        elif len(self.maxHeap) == len(self.minHeap) + 2:
            num = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, num)

    def findMedian(self) -> float:
        print(f"max heap : {self.maxHeap}")
        print(f"min heap : {self.minHeap}")
        print("______________________________")
        choice = len(self.maxHeap) + len(self.minHeap) 

        if choice == 1 :
            return float(-self.maxHeap[0])

        if choice % 2 == 1:
            return float(-self.maxHeap[0])

        else:
            return (-1 *self.maxHeap[0] + self.minHeap[0] ) /2
        