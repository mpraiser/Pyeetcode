class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return 0
        result = 0
        t = 0
        d = nums[1] - nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i+1] - nums[i] == d:
                t += 1
            else:
                d = nums[i+1] - nums[i]
                t = 0
            result += t
        return result


cases = [
    [1, 2, 3, 4],
]
for case in cases:
    ans = Solution().numberOfArithmeticSlices(case)
    print(ans)
