class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)- 1
        res = 0
        while l < r :
            mid = (l + r ) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
            # if nums[mid] > nums[l]:
            #     if nums[mid] > nums[r]:
            #         l = mid + 1
            #     else:
            #         r = mid - 1
            #         res = min(nums[res],nums[mid])
            # else:
            #     r = mid - 1
            #     res = min(nums[res],nums[mid])
        return nums[r]