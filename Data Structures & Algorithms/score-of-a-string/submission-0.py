class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_vals = [ord(char) for char in s]
        score = 0

        for i in range(len(ascii_vals)):
            try:
                score += abs(ascii_vals[i + 1] - ascii_vals[i])
            except IndexError:  # Handle `i + 1` OOB on last iteration
                break
        
        return score