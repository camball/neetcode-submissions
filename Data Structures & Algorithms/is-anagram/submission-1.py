class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_in_s = dict()
        letters_in_t = dict()

        for letter in s:
            letters_in_s[letter] = letters_in_s.get(letter, 0) + 1

        for letter in t:
            letters_in_t[letter] = letters_in_t.get(letter, 0) + 1
        
        return letters_in_s == letters_in_t