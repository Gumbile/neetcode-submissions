class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        n_total = n1 + n2

        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        L = 0
        R = n1

        while L <= R:
            mid1 = (L + R) // 2
            mid2 = (n_total + 1) // 2 - mid1

            l1 = float("-inf") if (mid1 == 0) else nums1[mid1 - 1]
            r1 = float("inf") if (mid1 == n1) else nums1[mid1]
            l2 = float("-inf") if (mid2 == 0) else nums2[mid2 - 1]
            r2 = float("inf") if (mid2 == n2) else nums2[mid2]

            if l1 <= r2 and r1 >= l2:
                if n_total % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                R = mid1 - 1
            else:
                L = mid1 + 1

        return 0
