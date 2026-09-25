class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        next_largest_in_nums1 = m - 1
        next_largest_in_nums2 = len(nums2) - 1
        next_writable_position = len(nums1) - 1

        while next_largest_in_nums2 >= 0:
            if next_largest_in_nums1 >= 0 and nums1[next_largest_in_nums1] > nums2[next_largest_in_nums2]:
                nums1[next_writable_position] = nums1[next_largest_in_nums1]
                next_largest_in_nums1 -= 1
            else: 
                nums1[next_writable_position] = nums2[next_largest_in_nums2]
                next_largest_in_nums2 -= 1

            next_writable_position -= 1