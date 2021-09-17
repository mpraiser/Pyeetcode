class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        category = (0, 1, 2)  # row, col, block
        state = [[0] * 9 for _ in category]  # row, col, block states

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                mask = 1 << (ord(board[row][col]) - ord("0"))
                block = (row // 3) * 3 + col // 3
                idx = (row, col, block)  # row, col, block index
                for c in category:
                    if state[c][idx[c]] & mask != 0:
                        return False
                    state[c][idx[c]] |= mask
        return True


case = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

ans = Solution().isValidSudoku(case)
print(ans)
