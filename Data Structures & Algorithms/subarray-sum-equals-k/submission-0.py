class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        O(n) time using prefix sums + a frequency map, where the frequency
        map has keys of each `i`'s running sum (a prefix sum) and values of
        the number of left-hand-side subarrays that we can "chop off" such
        that `running_sum - chopped_off_subarray == k`.

        At each index, let `running_sum` be the sum of nums[0..i] (a
        prefix sum). We want to know the count of how many earlier prefixes
        we can "chop off" so that the remaining subarray sums to `k`.

        If       running_sum - previous_prefix_sum == k,
        then     previous_prefix_sum == running_sum - k

        So we keep a frequency map of prefix sums we've already seen.

        E.g., for an input of    [  2, -1,  1,  2],  and k = 2
        our prefix sum array is  [  2,  1,  2,  4]

        At the final index, `running_sum = 4`, so we need a previous prefix
        sum of 2, because 4 (running_sum) - 2 (previous_prefix_sum) = 2 (k)

        We've previously seen prefix sum `2` twice (the part we want to
        "chop off"), shown below with the squiggly lines (the subarrays
        that sum to `k` shown via the straight lines):

                    sum = 2
              |~| |--------|
            [  2, -1,  1,  2]

                        sum = 2
              |~~~~~~~~~| |-|
            [  2, -1,  1,  2]

        So there are two different prefixes we can chop off for a given
        nums[i], meaning two valid subarrays ending at this index. This
        is why we need a frequency map rather than just a set.

        We initialise the map with `{0: 1}` to represent the one empty
        prefix before nums[0], whose sum is 0. This is what allows an
        input like `[2], k = 2` to work.
        """
        count = 0
        running_sum = 0

        freqs: dict[int, int] = {0: 1}

        for num in nums:
            running_sum += num

            count += freqs.get(running_sum - k, 0)

            freqs[running_sum] = freqs.get(running_sum, 0) + 1

        return count
