from collections import defaultdict
from typing import Optional


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = defaultdict(Trie)
        self.word: Optional[str] = None

    @property
    def is_word(self):
        return self.word is not None

    def insert(self, word: str):
        """
        Inserts a word into the trie.
        """
        node = self
        for c in word:
            node = node.children[c]
        node.word = word


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m = len(board)  # m, n > 0
        n = len(board[0])

        def neighbours(p: tuple[int, int]) -> tuple[int, int]:
            x, y = p
            if x + 1 < m:
                yield x + 1, y
            if x - 1 >= 0:
                yield x - 1, y
            if y + 1 < n:
                yield x, y + 1
            if y - 1 >= 0:
                yield x, y - 1

        root = Trie()
        for word in words:
            root.insert(word)

        ret = set()

        def backtrack(node: Trie, p: tuple[int, int]):
            ch = board[p[0]][p[1]]
            if ch not in node.children:
                return
            if node.children[ch].is_word:
                ret.add(node.children[ch].word)
                # backtrack should not stop here

            board[p[0]][p[1]] = "*"
            for q in neighbours(p):
                backtrack(node.children[ch], q)
            board[p[0]][p[1]] = ch

        for i in range(m):
            for j in range(n):
                backtrack(root, (i, j))
        return list(ret)


cases = [
    ([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
     ["oath", "pea", "eat", "rain"]),
    ([["a", "a"]], ["aaa"]),
    ([["a"]], ["a"]),
    ([["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]], ["oa", "oaa"]),
    ([["a", "a"]], ["aa"])
]
# for case in cases:
#     ans = Solution().findWords(*case)
#     print(ans)
ans = Solution().findWords(*cases[4])
print(ans)
