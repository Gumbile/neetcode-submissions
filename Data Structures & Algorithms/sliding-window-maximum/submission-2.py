class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        dq = deque()
        sol = []

        for i , val in enumerate(nums):
            if dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] < val:
                dq.pop()
            
            dq.append(i)

            if i >= k - 1:
                sol.append(nums[dq[0]])

        return sol
        