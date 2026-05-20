class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
    
        max_heap = []
        sol = []
        for index,value in enumerate(nums):
            heapq.heappush(max_heap,Item((value,index)))
            if index >= k - 1:
                while max_heap and max_heap[0].index() <= index - k:
                    heapq.heappop(max_heap)
                maxItem:Item = max_heap[0]
                sol.append(maxItem.numbr())
        
        return sol
        



class Item:
    def __init__(self, item):
        self.item = item

    def __lt__(self, other):
        if self.item[0] == other.item[0]:
            return self.item[1] < other.item[1]
        return self.item[0] > other.item[0]

    def __eq__(self, other):
        return self.item[0] == other.item[0] and self.item[1] == other.item[1]
    def index(self):
        return self.item[1]
    
    def numbr(self):
        return self.item[0]
    def __repr__(self):
        return f"({self.item[0]},{self.item[1]})"  