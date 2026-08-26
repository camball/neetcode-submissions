class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        # Initialise a matrix of all zeroes.
        #
        # We make our matrix (n + 1) x (m + 1) to leave room for
        # a "spacer" top and left border of all zeroes, which
        # eliminates some out-of-bounds edge cases (since adding
        # zero to any number is the additive identity).
        self.sum_matrix = [[0] * (COLS + 1) for row in range(ROWS + 1)]

        for row in range(ROWS):
            count = 0
            for col in range(COLS):
                # Increment count only by current row's prefix sum
                count += matrix[row][col]
                # Save current row's prefix sum + row above's mat's total sum
                self.sum_matrix[row + 1][col + 1] += count + self.sum_matrix[row][col + 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Add the full prefix matrix sum, and subtract the regions above
        # and to the left of it. The above and left matrices will overlap
        # on the diagonal from the top-left corner, counting that region
        # twice. We fix this by subtracting one copy of the sum of that
        # overlapping region.
        return self.sum_matrix[row2 + 1][col2 + 1] - self.sum_matrix[row2 + 1][col1] - self.sum_matrix[row1][col2 + 1] + self.sum_matrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
