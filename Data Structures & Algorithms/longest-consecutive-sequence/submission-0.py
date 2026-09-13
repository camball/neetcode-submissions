class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Only look for sequences if we encounter the start
        of a sequence. We know we have encountered the start
        of a sequence if the number immediately to the left
        of a given number (i.e., `num - 1`) isn't in `nums`,
        and we can know that in O(1) time by first initialising
        a set with the values of `nums`.

        When we do encounter the start of a sequence, let's check
        how long of a sequence it is! We can just keep a running
        `longest` count, and if the length of the sequence we just
        found is longer than the current longest, we'll just update
        the `longest` count. By the end, `longest` will represent
        the length of the longest consecutive sequence, so we can
        simply return that.
        """
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longest = length if length > longest else longest
        return longest