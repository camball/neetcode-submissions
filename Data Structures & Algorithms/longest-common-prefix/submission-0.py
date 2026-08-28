from collections import Counter

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        for letters_at_index in zip(*strs):
            if all(letter == letters_at_index[0] for letter in letters_at_index):
                common_prefix += letters_at_index[0]
            else:
                break

        return common_prefix