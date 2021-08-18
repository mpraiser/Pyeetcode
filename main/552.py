class Solution:
    def checkRecord(self, n: int) -> int:
        m = 10 ** 9 + 7
        # f[n][a][l]
        f = [[0] * 3 for _ in range(2)]
        f_next = [[0] * 3 for _ in range(2)]
        f[0][1] = 1
        f[0][0] = 1
        f[1][0] = 1
        for i in range(1, n):
            # end with 'A'
            for L in range(3):
                f_next[1][0] += f[0][L]
            # end with 'L'
            for L in range(3 - 1):
                for A in range(2):
                    f_next[A][L+1] += f[A][L]
            # end with 'P'
            for L in range(3):
                for A in range(2):
                    f_next[A][0] += f[A][L]
            # modular
            for L in range(3):
                for A in range(2):
                    f_next[A][L] %= m
            # next iter
            f, f_next = f_next, f
            for L in range(3):
                for A in range(2):
                    f_next[A][L] = 0

        result = 0
        for A in range(2):
            for L in range(3):
                result += f[A][L]
        return result % m


ans = Solution().checkRecord(10101)
print(ans)
