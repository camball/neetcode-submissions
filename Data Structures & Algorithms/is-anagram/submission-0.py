from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_in_s = Counter(s)
        letters_in_t = Counter(t)

        return letters_in_s == letters_in_t