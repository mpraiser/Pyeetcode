from collections import defaultdict
from typing import Optional


class WordDictionary:
    def __init__(self):
        self.children: dict[Optional[str]] = defaultdict(lambda: None)
        self.is_end = False

    def addWord(self, word: str) -> None:
        node: WordDictionary = self
        for c in word:
            if node.children[c] is None:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self.__search(word, 0)

    def __search(self, word: str, i: int) -> bool:
        node = self
        if i >= len(word):
            return self.is_end
        c = word[i]
        # dealing with special case
        if c == ".":
            return any(
                nxt.__search(word, i + 1) for nxt in node.children.values() if nxt
            )
        else:
            return node.children[c] is not None and node.children[c].__search(word, i + 1)


# root = WordDictionary()
# root.addWord("bad")
# root.addWord("dad")
# root.addWord("mad")
# print(root.search("pad"))
# print(root.search("bad"))
# print(root.search(".ad"))
# print(root.search("b.."))


if __name__ == "__main__":
    from itertools import zip_longest
    from operator import methodcaller

    cases = [
        (
            ["WordDictionary", "addWord", "addWord", "addWord", "addWord", "search", "search", "addWord", "search",
             "search", "search", "search", "search", "search"],
            [[], ["at"], ["and"], ["an"], ["add"], ["a"], [".at"], ["bat"], [".at"], ["an."], ["a.d."], ["b."], ["a.d"],
             ["."]]
        ),
        (
            ["WordDictionary", "addWord", "addWord", "search", "search", "search", "search", "search", "search",
             "search", "search"],
            [[], ["a"], ["ab"], ["a"], ["a."], ["ab"], [".a"], [".b"], ["ab."], ["."], [".."]]
        )
    ]

    def executor(case):
        root = None
        for method, parameter in zip_longest(case[0], case[1]):
            if method == "WordDictionary":
                root = WordDictionary()
                ans = None
            else:
                f = methodcaller(method, parameter[0])
                ans = f(root)
            print(method, parameter, ans)

    for c in cases:
        print(c)
        executor(c)
    # executor(cases[1])

