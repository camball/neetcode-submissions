class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = [-1] * len(nums1)

        # Mapping nums1's values -> indexes for quick lookup as we iterate thru nums2
        idx_mapping = {value: idx for idx, value in enumerate(nums1)}

        # Invariant: top of stack == smallest element, monotonically increasing from there
        stack = []

        for i in range(len(nums2)):
            # If we ever see a greater value than `stack[-1]`, repeatedly pop
            # the stack to check if there are greater elements that the
            # current element is greater than as well. We look up the index
            # of where to write to in `output`, corresponding to where the
            # number is in `nums1`.

            while stack and nums2[i] > stack[-1]:
                top_of_stack = stack.pop()
                output[idx_mapping[top_of_stack]] = nums2[i]
            
            if nums2[i] in idx_mapping:
                stack.append(nums2[i])

        return output