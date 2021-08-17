class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] != mid:
                right = mid
            else:
                left = mid + 1
        return left


cases = [
    [0, 1, 3],
    [0, 1, 2, 3, 4, 5, 6, 7, 9],
    [0]
]

for case in cases:
    ans = Solution().missingNumber(case)
    print(ans)
