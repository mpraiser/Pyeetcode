from typing import List

def is_connected(p1, p2):
    # 2-norm, d4 connect
    if p1 and p2:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) == 1
    else:
        return True

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board:
            m = len(board)
        else:
            return False
        if board[0]:
            n = len(board[0])
        else:
            return False


        def helper(p, i):
            """
            Args:
                p: point of last char
                i: index of char to find in word
            """
            # end of search
            if i >= len(word):
                return True

            for a in range(m):
                for b in range(n):
                    if board[a][b] == word[i] and is_connected(p, (a, b)):
                        board[a][b] = ''
                        if helper((a,b), i+1):
                            return True
                        board[a][b] = word[i]
            return False
        
        return helper(None, 0)


x = Solution()
ans = x.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
print(ans)