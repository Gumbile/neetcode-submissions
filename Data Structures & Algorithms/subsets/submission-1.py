import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        def rec(numToAdd,arr:list[int]):

            for i,num in enumerate(numToAdd):
                arr.append(num)
                res.append(arr[:])
                rec(numToAdd[i+1:],arr)
                arr.pop()

        rec(nums,[])

        return res