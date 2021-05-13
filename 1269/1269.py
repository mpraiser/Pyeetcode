import functools

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @functools.lru_cache(maxsize=None)
        def f(p, s) -> int:
            """
            Args:
                p: present location
                s: steps left

            Returns:
                number of solutions
            """
            if s > 0:
                # Optimization: too far from 0
                if p > s:
                    return 0
                
                ans = f(p, s-1)
                if 0 <= p+1 < arrLen:
                    ans += f(p+1, s-1)
                if 0 <= p-1 < arrLen:
                    ans += f(p-1, s-1)
                return ans % (10**9+7)
            else:
                return 1 if p == 0 else 0
            
        return f(0, steps)


x = Solution()
ans = x.numWays(27, 7)
print(ans)