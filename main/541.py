class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        for i in range(0, len(s), 2 * k):
            if len(s) <= i + k:
                result += s[i:len(s)][::-1]
            else:
                result += s[i:i + k][::-1]
                if len(s) <= i + 2 * k:
                    result += s[i + k:len(s)]
                else:
                    result += s[i + k:i + 2 * k]
        return result


cases = [
    ("abcdefg", 2)
]

for case in cases:
    ans = Solution().reverseStr(*case)
    print(ans)