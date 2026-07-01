from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Key insight: Since we can simply rotate students, student
        # order doesn't matter, but sandwich order *does*, since
        # we can only pop a sandwich from the top of the stack.

        students_freq = Counter(students)

        for sandwich in sandwiches:
            if students_freq[sandwich] == 0:
                break

            students_freq[sandwich] -= 1

        return students_freq.total()