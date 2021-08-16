class Solution:
    def countArrangement(self, n: int) -> int:
        candidates = [i + 1 for i in range(n)]
        count = 0

        def f(lo):
            nonlocal count
            if lo == n:
                count += 1
                # print(candidates)
                return

            i = lo + 1
            for ptr in range(lo, n):
                if candidates[ptr] % i == 0 or i % candidates[ptr] == 0:
                    candidates[lo], candidates[ptr] = candidates[ptr], candidates[lo]
                    f(lo + 1)
                    candidates[lo], candidates[ptr] = candidates[ptr], candidates[lo]

        f(0)
        return count


ans = Solution().countArrangement(3)
print(ans)