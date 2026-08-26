class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum_matrix = [[0] * len(row) for row in matrix]

        for row_idx, row in enumerate(matrix):
            count = 0
            for col_idx, num in enumerate(row):
                count += num
                self.prefix_sum_matrix[row_idx][col_idx] = count


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region_sum = 0
        for row in self.prefix_sum_matrix[row1:row2 + 1]:
            l_sum = 0 if col1 == 0 else row[col1 - 1]
            r_sum = row[col2]

            region_sum += r_sum - l_sum

        return region_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
