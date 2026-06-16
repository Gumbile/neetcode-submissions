import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.size = 0
        self.heap = self.initHeap(nums)
        

    def add(self, val: int) -> int:
        # print(self.heap)

        heapq.heappush(self.heap, val)
        return heapq.nlargest(self.k, self.heap)[-1]

    def initHeap(self,nums):
        heapq.heapify(nums)
        return nums
        