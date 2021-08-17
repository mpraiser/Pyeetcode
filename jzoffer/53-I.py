class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # find max n <= target
        # if target > nums[-1], returns len(nums)
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        lower = left
        # find min n >= target
        # if target < nums[0], returns -1
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        upper = left - 1
        # target in [lower, upper]
        count = upper - lower + 1 if 0 <= lower <= upper < len(nums) else 0
        return count


cases = [
    ([5, 7, 7, 8, 8, 10], 8),
    ([5, 7, 7, 8, 8, 10], 6),
    ([1], 1)
]

for case in cases:
    ans = Solution().search(*case)
    print(ans)
