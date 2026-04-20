class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # Right half is sorted
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # target in sorted right
                else:
                    r = mid - 1  # target in left
            # Left half is sorted
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # target in sorted left
                else:
                    l = mid + 1  # target in right
        
        return -1