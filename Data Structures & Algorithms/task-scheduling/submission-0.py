import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        arr = [0]  * 26
        for c in tasks:
            arr[ord(c) - ord('A')]+=1
        
        heap = []

        for i,v in enumerate(arr):
            if v > 0:
                heapq.heappush(heap,[-v,i])
        print(heap) 
        
        cnt = 0
        while heap:
            
            k = n + 1
            cooldown = []
            while k > 0 :
                k-= 1
                cnt+=1
                
                if heap:
                    task = heapq.heappop(heap)
                    
                    task[0] = task[0] + 1
                    if task[0] != 0:
                        cooldown.append(task)
                
                if not heap and not cooldown:
                    break
            
            
            while cooldown:
                heapq.heappush(heap,cooldown.pop())


        return cnt