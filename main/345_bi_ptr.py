class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            while i < len(s) and s[i] not in vowels:
                i += 1
            while j >= 0 and s[j] not in vowels:
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)


cases = [
    "leetcode",
    "a."
]

for case in cases:
    ans = Solution().reverseVowels(case)
    print(ans)
#
# ans = Solution().reverseVowels()
# print(ans)