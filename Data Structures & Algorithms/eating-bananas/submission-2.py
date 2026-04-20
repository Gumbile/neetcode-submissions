import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        found = 0
        while l < r :
            mid = (r+l) //2
            # print(mid)
            if self.feisable(piles,mid,h):
                r = mid
                # found = mid
            else:
                l = mid + 1
        return l
        

    def feisable(self,piles: List[int], k : int, h: int) -> bool:
        totalHours = 0
        for p in piles:
            if p < k:
                totalHours+= 1
            else:
                totalHours+= math.ceil(p/k)
        # print(totalHours)
        if totalHours > h:
            return False
        else:
            return True