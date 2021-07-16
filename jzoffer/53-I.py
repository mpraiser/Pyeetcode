from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0

        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                count += 1
                i = mid - 1
                while i >= 0 and nums[i] == target:
                    count += 1
                    i -= 1
                j = mid + 1
                while j < len(nums) and nums[j] == target:
                    count += 1
                    j += 1
                return count
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        
        return 0


cases = [
    ([5,7,7,8,8,10], 8),
    ([5,7,7,8,8,10], 6)
]


for case in cases:
    ans = Solution().search(*case)
    print(ans)