from functools import lru_cache

class Solution:

    @lru_cache
    def climbStairs(self, n: int) -> int:
        """
        Recursive solution.

        The recursive solution here runs in 2^n time,
        where the 2 comes from two-branch recursion.
        
        In order for this to run within the time
        limit, memoizing with `lru_cache`.
        """
        if n <= 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)