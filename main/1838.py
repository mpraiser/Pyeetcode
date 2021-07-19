from typing import List
from itertools import accumulate


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        psum = list(accumulate(nums))
        max_frequncy = 1
        for j in range(len(nums)):
            # find where max f <= k
            left = j
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if j > 0:
                    f = (mid - j + 1 ) * nums[j] - (psum[mid] - psum[j-1])
                else:
                    f = (mid - j + 1) * nums[j] - psum[mid]
                if f <= k:
                    left = mid + 1
                else:
                    right = mid
            frequncy = left - j
            if frequncy > max_frequncy:
                max_frequncy = frequncy
            if max_frequncy > len(nums) - j:
                break

        return max_frequncy


cases = [
    ([1,2,4], 5),
    ([1,4,8,13], 5),
    ([3,9,6], 2),
    ([9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966], 3056)
]
for case in cases:
    ans = Solution().maxFrequency(*case)
    print(ans)

# ans = Solution().maxFrequency(*cases[3])
# print(ans)