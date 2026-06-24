class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # This solution hinges on how for any `i`,
        # max(arr[(i + 1):]) == max([arr[i + 1]] + arr[(i + 2):])
        #
        # Best seen with an example. For `arr = [2,4,5,3,1,2]` and `i = 2`,
        # max([5, 3, 1, 2]) == max([5] + [3, 1, 2])
        #
        # The key here is that if we simply traverse `arr` backwards,
        # we will be able to keep a running max of the progressively-
        # smaller right side of that list concatenation (`[3, 1, 2]`).

        running_max = -1

        for i in range(len(arr)):
            reverse_i = -(i + 1)
            old = arr[reverse_i]
            arr[reverse_i] = running_max
            running_max = max(old, running_max)

        return arr