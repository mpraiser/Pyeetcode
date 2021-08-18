class Solution:
    def checkRecord(self, n: int) -> int:
        m = 10 ** 9 + 7
        # f[n][a][l]
        f = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        f[1][0][1] = 1
        f[1][0][0] = 1
        f[1][1][0] = 1
        for i in range(1, n):
            # end with 'A'
            for L in range(3):
                f[i + 1][1][0] += f[i][0][L] % m
            # end with 'L'
            for L in range(3 - 1):
                for A in range(2):
                    f[i + 1][A][L+1] += f[i][A][L] % m
            # end with 'P'
            for L in range(3):
                for A in range(2):
                    f[i + 1][A][0] += f[i][A][L] % m

        result = 0
        for A in range(2):
            for L in range(3):
                result += f[n][A][L] % m
        return result % m


ans = Solution().checkRecord(10101)
print(ans)
