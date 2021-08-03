from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_n = float("-inf")
        right = -1
        min_n = float("inf")
        left = -1

        for i in range(len(nums)):
            # 记录左区间的最大值
            if nums[i] >= max_n:
                max_n = nums[i]
            # 如果不是最大值，则为乱序区间的右端点
            else:
                right = i
            
            if nums[n-1-i] <= min_n:
                min_n = nums[n-1-i]
            else:
                left = n - i - 1

        # 特殊情况是原数组全序，有left == -1且right == -1
        # 如果有乱序区间，一定有左右端点
        if right != -1 and left != -1 and left <= right:
            return right - left + 1
        else:
            return 0


        
cases = [
    [2,6,4,8,10,9,15],
    [1,2,3,4],
    [1]
]

for case in cases:
    ans = Solution().findUnsortedSubarray([1,2,3,1,2,3])
    print(ans)