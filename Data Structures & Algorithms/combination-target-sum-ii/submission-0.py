class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(last_sum, nums, prev: list[int]):
            if last_sum <= target:
                if last_sum == target:
                    ans.append(prev[:])
            else:
                return
            
            i = 0
            
            while i < len(nums):
                
                num = nums[i]
                last_sum += num
                prev.append(num)
                
                dfs(last_sum, nums[i + 1 :], prev)
                
                prev.pop()
                last_sum -= num
                
                i+=1
                while i < len(nums) and num == nums[i]:
                    i+=1


        dfs(0,candidates,[])
        return ans
