class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res , combination = [],[]
        candidates.sort()

        def dfs(i):
            
            if sum(combination) == target:
                res.append(combination[:])
                return
            
            if i >=len(candidates) or sum(combination) > target:
                return

            combination.append(candidates[i])
            
            i+= 1
            dfs(i)
            combination.pop()
            
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i+=1

            dfs(i)

        dfs(0)

        return res