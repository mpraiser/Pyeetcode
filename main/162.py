class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)
        nums.append(float('-inf'))
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:  # 哪边高，哪边至少存在一个峰
                left = mid + 1
            else:  # 由于已经判断不是峰，一边低，另一边一定高
                right = mid
        return -1


cases = [
    [1, 2, 1, 3, 5, 6, 4],
    [2, 1],
    [3, 1, 2],
    [1]
]
for case in cases:
    ans = Solution().findPeakElement(case)
    print(ans)

# ans = Solution().findPeakElement(cases[2])
# print(ans)
