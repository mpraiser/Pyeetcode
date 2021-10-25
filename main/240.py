class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix)
        assert n >= 1
        m = len(matrix[0])
        assert m >= 1

        i = 0
        j = m - 1
        while i < n and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
        return False


cases = [
    (
        [[1, 4, 7, 11, 15],
         [2, 5, 8, 12, 19],
         [3, 6, 9, 16, 22],
         [10, 13, 14, 17, 24],
         [18, 21, 23, 26, 30]],
        5
    ),
]
for case in cases:
    ans = Solution().searchMatrix(*case)
    print(case, ans)
