class Solution:
    def findNumberIn2DArray(self, matrix: list[list[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        def quad_search(
                row_lo: int, row_hi: int, column_lo: int, column_hi: int, target: int
        ):
            if row_lo < row_hi and column_lo < column_hi:
                row_mid = (row_lo + row_hi) // 2
                column_mid = (column_lo + column_hi) // 2
                if matrix[row_mid][column_mid] == target:
                    return True
                elif matrix[row_mid][column_mid] > target:
                    return quad_search(row_lo, row_mid, column_lo, column_mid, target) or \
                           quad_search(row_lo, row_mid, column_mid, column_hi, target) or \
                           quad_search(row_mid, row_hi, column_lo, column_mid, target)
                else:
                    return quad_search(row_mid + 1, row_hi, column_mid + 1, column_hi, target) or \
                           quad_search(row_lo, row_mid + 1, column_mid + 1, column_hi, target) or \
                           quad_search(row_mid + 1, row_hi, column_lo, column_mid + 1, target)
            else:
                return False

        return quad_search(0, len(matrix), 0, len(matrix[0]), target)


cases = [
    ([[1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10],
      [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20],
      [21, 22, 23, 24, 25]], 5),
    ([[1, 4, 7, 11, 15],
      [2, 5, 8, 12, 19],
      [3, 6, 9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]], 5)
]
for case in cases:
    ans = Solution().findNumberIn2DArray(*case)
    print(ans)

# ans = Solution().findNumberIn2DArray([[-1, 3]], -1)
# print(ans)
