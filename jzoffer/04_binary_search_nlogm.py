class Solution:
    def findNumberIn2DArray(self, matrix: list[list[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        for row in matrix:
            if row[0] <= target <= row[-1]:
                left = 0
                right = len(row)
                while left < right:
                    mid = (left + right) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        right = mid
                    else:
                        left = mid + 1
        return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

targets = [
    1, 31, 30
]
for t in targets:
    ans = Solution().findNumberIn2DArray(matrix, t)
    print(ans)
