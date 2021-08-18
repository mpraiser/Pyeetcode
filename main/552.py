class Solution:
    def checkRecord(self, n: int) -> int:
        m = 10 ** 9 + 7
        # f[n][a][l]
        f = [[0] * 3 for _ in range(2)]
        f[0][1] = 1
        f[0][0] = 1
        f[1][0] = 1
        for i in range(1, n):
            f_next = [[0] * 3 for _ in range(2)]
            # end with 'A'
            for L in range(3):
                f_next[1][0] += f[0][L] % m
            # end with 'L'
            for L in range(3 - 1):
                for A in range(2):
                    f_next[A][L+1] += f[A][L] % m
            # end with 'P'
            for L in range(3):
                for A in range(2):
                    f_next[A][0] += f[A][L] % m
            f = f_next

        result = 0
        for A in range(2):
            for L in range(3):
                result += f[A][L]
        return result % m


ans = Solution().checkRecord(10101)
print(ans)
