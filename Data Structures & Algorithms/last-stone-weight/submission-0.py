class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
      
        heapq.heapify_max(stones) 
        print(stones)

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones) if stones else 0
            print(stones)

            if x > y:
                x =x -y
                heapq.heappush_max(stones,x)

          
        return 0 if len(stones) == 0 else stones[0]