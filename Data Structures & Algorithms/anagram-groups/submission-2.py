class Solution:
    def create_freq_map(self, word: str) -> tuple:
        frequencies = [0] * 26  # 26 lowercase English letters

        for letter in word:
            # 97 is the ASCII value of the first lowercase letter, 'a'
            frequencies[ord(letter) - 97] += 1

        return tuple(frequencies)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Key must be immutable, and must be a mapping of characters
        in the character set to their frequencies.

        What the character set is can depend, but we have the constraint
        here that "strs[i] is made up of lowercase English letters".

        Needing a immutable key lends itself to only a handful of types
        in Python. We can bypass storing a `Counter`/`dict`-esque type
        by storing frequency counts at the integer offset of each
        dictionary letter in a k-tuple, where there are k letters in our
        potential character set. E.g.,

        (1,0,2,0,0,0,4,...) means "one 'a', two 'c's, four 'g's"
        """
        # tuple(1,0,1,...,1,0,0,0,0,0,0) -> ["cat", "act"]
        anagrams: dict[tuple, list[str]] = dict()

        for word in strs:
            frequency_map = self.create_freq_map(word)
            if frequency_map in anagrams:
                anagrams[frequency_map].append(word)
            else:
                anagrams[frequency_map] = [word]

        return list(anagrams.values())
