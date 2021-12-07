from collections import deque


class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        m = len(grid)
        assert m > 0
        n = len(grid[0])
        assert n > 0

        def neighbour4(xx: int, yy: int):
            yield xx + 1, yy
            yield xx - 1, yy
            yield xx, yy + 1
            yield xx, yy - 1

        connected = set()
        not_connected = set()
        connected.add((row, col))

        queue = deque()
        queue.append((row, col))
        while queue:
            x, y = queue.popleft()
            for (i, j) in neighbour4(x, y):
                if 0 <= i < m and 0 <= j < n:
                    if (i, j) not in connected and (i, j) not in not_connected:
                        if grid[i][j] == grid[x][y]:
                            connected.add((i, j))
                            queue.append((i, j))
                        else:
                            not_connected.add((i, j))

        for (x, y) in connected:
            if not all(
                    0 <= i < m and 0 <= j < n and (i, j) in connected for i, j in neighbour4(x, y)
            ):
                grid[x][y] = color
        return grid


cases = [
    ([[1, 2, 2], [2, 3, 2]], 0, 1, 3),
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2)
]
for case in cases:
    ans = Solution().colorBorder(*case)
    print(ans)
