class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,permutation = [],[]

        choosen = [False]* len(nums)

        def dfs():
            if len(permutation) == len(nums):
                res.append(permutation[:])
                return

            for j in range(len(nums)):
                if not choosen[j]:
                    choosen[j] = True
                    permutation.append(nums[j])
                    dfs()
                    permutation.pop()
                    choosen[j] = False

        dfs()
        return res