class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        lastPoint = m+n-1
        while lastPoint >= 0:
            if i < 0:
                nums1[lastPoint] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[lastPoint] = nums1[i]
                i -= 1
            else:
                if nums1[i] > nums2[j]:
                    nums1[lastPoint] = nums1[i]
                    i -= 1
                else:
                    nums1[lastPoint] = nums2[j]
                    j -= 1
            lastPoint -= 1
