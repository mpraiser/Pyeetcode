from typing import Optional


class Trie:
    @staticmethod
    def to_key(char: str):
        return ord(char) - ord('a')

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children: list[Optional] = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for c in word:
            c = self.to_key(c)
            if node.children[c] is None:
                node.children[c] = Trie()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for c in word:
            c = self.to_key(c)
            if node.children[c] is None:
                return False
            node = node.children[c]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for c in prefix:
            c = self.to_key(c)
            if node.children[c] is None:
                return False
            node = node.children[c]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
