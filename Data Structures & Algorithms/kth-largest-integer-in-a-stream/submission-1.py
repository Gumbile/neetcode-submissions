import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.size = 0
        self.heap = self.initHeap(nums)
        

    def add(self, val: int) -> int:
        if self.size > self.k:
            heapq.heappop(self.heap)
            self.size-=1
        heapq.heappush(self.heap, val)
        return heapq.nlargest(self.k, self.heap)[-1]

    def initHeap(self,nums):
        h = []
        for num in nums:
            if self.size > self.k:
                heapq.heappop(h)
                self.size-=1

            heapq.heappush(h,num)
            self.size+=1
        return h
            
        