class Solution:
    """
    Using a run-length encoding (RLE) approach.

    Length of each string is between 0 and 199 characters.

    We will store the length of each string in exactly three characters,
    which will cover our constraints. E.g., "g" is of length "001" whereas
    "asdfghjkl;" is of length "010".

    To encode a string, we append the length (per the above format) of the
    current string to a list, then append each character.

    To decode the encoded string, we read the next three characters to know
    how far to read for the next string, appending that string's contents
    to the output list.
    """

    LENGTH_CHARS = 3

    def encode(self, strs: List[str]) -> str:
        parts = []

        for string in strs:
            int_length = len(string)
            if int_length < 10:
                parts.append(f"00{int_length}")
            elif int_length < 100:
                parts.append(f"0{int_length}")
            else:
                parts.append(str(int_length))
            
            parts.append(string)

        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        original = []
        cursor = 0

        while cursor < len(s):
            length = int(s[cursor:cursor + self.LENGTH_CHARS])
            cursor += 3
            original.append(s[cursor:cursor + length])
            cursor += length

        return original


