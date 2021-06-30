from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        ans = None

        while left <= right:
            mid = (left + right) // 2
            # mid is peak or on downside
            diff = arr[mid + 1] - arr[mid]
            if diff < 0:
                ans = mid
                right = mid - 1
            # mid is on upside
            elif diff > 0:
                left = mid + 1
            # else:
            #     raise Exception
            
        return ans


x = Solution()
ans = x.peakIndexInMountainArray( [24,69,100,99,79,78,67,36,26,19])
print(ans)