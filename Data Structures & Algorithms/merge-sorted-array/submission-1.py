class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """
        Notice that there are `n` sentinel zeroes at the end of `nums1`.
        
        The initial way of thinking about merging two lists is to start from
        the beginning of each, merging as we go, but that would lead us to an
        O(n^2) solution, from needing to shift the rest of `nums1` as we
        insert values. If we instead iterate back-to-front in both nums1 and
        nums2, we can simply overwrite the next free writable position, and
        we'll do this O(m + n) times. 

        To facilitate the above, we'll keep track of:
        - The index of the next largest element in nums1 (initialised to index
          m - 1)
        - The index of the next largest element in nums2 (initialised to index
          len(nums2) - 1)
        - The next index in `nums1` to overwrite (initialised to len(nums1) - 1)

        A better test case than the provided ones:

        nums1=[0,20,20,40,0,0,0], m=4
        nums2=[-2,-1,35], n=3
        """

        nums1_idx = m - 1
        nums2_idx = len(nums2) - 1
        next_writable_idx = len(nums1) - 1

        while nums2_idx >= 0:
            if nums1_idx >= 0 and nums1[nums1_idx] > nums2[nums2_idx]:
                nums1[next_writable_idx] = nums1[nums1_idx]
                nums1_idx -= 1
            else:  # nums2[nums2_idx] >= nums1[nums1_idx]
                nums1[next_writable_idx] = nums2[nums2_idx]
                nums2_idx -= 1

            next_writable_idx -= 1