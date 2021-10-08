from collections import Counter


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        return [
            key for key, value in Counter(s[i:i+10] for i in range(0, len(s) - 10 + 1)).items() if value > 1
        ]


ans = Solution().findRepeatedDnaSequences("AAAAAAAAAAA")
print(ans)


