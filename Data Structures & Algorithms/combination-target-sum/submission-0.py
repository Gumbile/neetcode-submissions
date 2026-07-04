class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(arr,count,numss):
            if count >= target:
                if count == target:
                    res.append(arr[:])
                return
            
            for i,num in enumerate(numss):
                arr.append(num)
                count = sum(arr)
                # print(arr,count)
                # print("_________________")
                dfs(arr,count,numss[i:])
                arr.pop()

        dfs([],0,nums)
        return res