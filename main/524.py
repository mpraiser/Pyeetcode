class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        dictionary.sort()
        dictionary.sort(key=lambda _: len(_), reverse=True)
        # index of first j in [i, len(s))
        automaton = [[0] * 26 for _ in range(len(s))]
        automaton.append([len(s)] * 26)  # boundary condition, index >= len(s) means invalid

        for i in reversed(range(len(s))):
            for j in range(26):
                if ord(s[i]) - ord('a') == j:
                    automaton[i][j] = i
                else:
                    automaton[i][j] = automaton[i + 1][j]

        for item in dictionary:
            i = 0
            match = True
            for x in item:
                i = automaton[i][ord(x) - ord('a')]
                if i >= len(s):
                    match = False
                    break
                i += 1
            if match:
                return item
        return ""


cases = [
    ("abpcplea", ["ale", "apple", "monkey", "plea"])
]
for case in cases:
    ans = Solution().findLongestWord(*case)
    print(ans)
