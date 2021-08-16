class Solution:
    def countArrangement(self, n: int) -> int:
        # f: state -> int, 选取[1, n]中数的时候，总方案数
        f = [0] * (1 << n)
        f[0] = 1

        def count_one(m: int) -> int:
            count = 0
            while m:
                m &= m - 1
                count += 1
            return count

        for mask in range(0, 1 << n):
            this = count_one(mask)  # 当前是第几个选取的数
            for index in range(n):
                i = index + 1
                # 如果该数被选取，是第this个数
                if (mask >> index) & 1:
                    # 如果符合要求
                    if i % this == 0 or this % i == 0:
                        f[mask] += f[mask ^ (1 << index)]  # 加上被选取的位为0的方案数

        return f[(1 << n) - 1]


ans = Solution().countArrangement(2)
print(ans)
