import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        arr = [0]  * 26
        for c in tasks:
            arr[ord(c) - ord('A')]+=1
        
        heap = [-count for count in arr if count > 0]
        heapq.heapify(heap)

        
        time = 0
        while heap:
            
            cycles = n + 1
            cooldown = []
           
            for _ in range(cycles):

                if heap:
                    task = heapq.heappop(heap)
                    task += 1

                    if task != 0:
                        cooldown.append(task)

                time += 1

                if not heap and not cooldown:
                    break

            for task in cooldown:
                heapq.heappush(heap,task)


        return time