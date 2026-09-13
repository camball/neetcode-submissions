class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        for i in range(len(s)):
            try:
                score += abs(ord(s[i + 1]) - ord(s[i]))
            except IndexError:  # Handle `i + 1` OOB on last iteration
                break
        
        return score