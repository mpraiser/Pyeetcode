from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows <= 0:
            return False
        cols = len(matrix[0])
        if cols <= 0:
            return False

        for i in range(rows):
            if matrix[i][0] > target or matrix[i][-1] < target:
                continue
            left = 0
            right = cols - 1
            while left <= right:
                # search in [left, right)
                mid = (left + right) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    left = mid + 1
                elif matrix[i][mid] > target:
                    right = mid - 1
        return False



x = Solution()
ans = x.findNumberIn2DArray([[5],[6]], 6)
print(ans)