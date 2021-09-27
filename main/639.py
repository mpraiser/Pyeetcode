class Solution:
    def numDecodings(self, s: str) -> int:
        boundary = 10 ** 9 + 7
        dp = [0] * (len(s) + 1)  # number of solutions in s[:i]
        dp[0] = 1

        for i in range(1, len(s) + 1):
            if i - 1 >= 0:
                if s[i - 1] == "*":
                    alpha = 9
                elif s[i - 1] == "0":
                    alpha = 0
                else:
                    alpha = 1

                dp[i] += (alpha * dp[i - 1]) % boundary

            if i - 2 >= 0:
                if s[i - 1] == "*" and s[i - 2] == "*":
                    beta = 15
                elif s[i - 1] == "*" and s[i - 2] != "*":
                    if s[i - 2] == "1":
                        beta = 9
                    elif s[i - 2] == "2":
                        beta = 6
                    else:
                        beta = 0
                elif s[i - 1] != "*" and s[i - 2] == "*":
                    if ord(s[i - 1]) <= ord("6"):
                        beta = 2
                    else:
                        beta = 1
                else:
                    if s[i - 2] != "0" and 1 <= int(s[i - 2] + s[i - 1]) <= 26:
                        beta = 1
                    else:
                        beta = 0
                dp[i] += (beta * dp[i - 2]) % boundary
                dp[i] %= boundary

        return dp[len(s)]


cases = [
    "*",
    "*1",
    "*0",
    "*7",
    "1*",
    "2*",
    "**",
    "*1*",
    "*1*1*0"
]
for case in cases:
    ans = Solution().numDecodings(case)
    print(ans)

# ans = Solution().numDecodings("*1*")
# print(ans)
