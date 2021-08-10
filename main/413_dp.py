from functools import lru_cache


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return 0

        @lru_cache(maxsize=1)
        def f(i: int) -> int:
            """number of solutions, end with i"""
            if i == 1:
                return 0
            else:
                return f(i-1) + 1 if nums[i] - nums[i-1] == nums[i-1] - nums[i-2] else 0

        return sum(f(i) for i in range(2, len(nums)))


cases = [
    [1, 2, 3, 4],
]
for case in cases:
    ans = Solution().numberOfArithmeticSlices(case)
    print(ans)
