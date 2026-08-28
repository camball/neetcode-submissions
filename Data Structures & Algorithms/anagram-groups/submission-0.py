class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # "act" -> ["act", "cat"]
        sorted_strs: dict[str, list[str]] = dict()

        for string in strs:
            key = "".join(sorted(string))
            if key not in sorted_strs:
                sorted_strs[key] = [string]
            else:
                sorted_strs[key].append(string)

        return list(sorted_strs.values())