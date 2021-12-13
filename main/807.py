class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        m = len(grid)
        assert 0 < m <= 50
        n = len(grid[0])
        assert 0 < n <= 50

        max_row = [grid[i][0] for i in range(m)]
        max_col = [grid[0][j] for j in range(n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] > max_row[i]:
                    max_row[i] = grid[i][j]
                if grid[i][j] > max_col[j]:
                    max_col[j] = grid[i][j]

        ret = 0
        for i in range(m):
            for j in range(n):
                ret += min(max_row[i], max_col[j]) - grid[i][j]
        return ret


cases = [
    [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
]
for case in cases:
    ans = Solution().maxIncreaseKeepingSkyline(case)
    print(ans)
