class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if m < n:
            nums1, nums2 = nums2, nums1
            n, m = m, n
        half = (n + m + 1) // 2
        left, right = 0, n

        while left <= right:
            i = left + (right - left) // 2
            j = half - i

            nums1_left = nums1[i - 1] if i >= 1 else float('-inf')
            nums1_right = nums1[i] if i < n else float('inf')

            nums2_left = nums2[j - 1] if j >= 1 else float('-inf')
            nums2_right = nums2[j] if j < m else float('inf')

            if nums1_left <= nums2_right and nums1_right >= nums2_left:
                if (m + n) % 2 == 1:
                    return max(nums1_left,nums2_left)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_right < nums2_left:
                left = i + 1
            else:
                right = i - 1



