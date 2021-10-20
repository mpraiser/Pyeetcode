class Solution:
    def minMoves(self, nums: list[int]) -> int:
        s = 0
        m = nums[0]
        for n in nums:
            s += n
            if n < m:
                m = n
        return s - m * len(nums)


cases = [
    [1, 2, 3],
    [1, 1, 1],
    [1, 1000],
    [1, 1, 1000],
    [5, 6, 8, 8, 5]
]

for case in cases:
    ans = Solution().minMoves(case)
    print(case, ans)
