from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        state = 'up'
        last = arr[0]
        peak = None
        for i in range(1, len(arr)):
            if state == 'up':
                if arr[i] < last:
                    state = 'down'
                    peak = i-1
                if state == 'down':
                    if arr[i] > last:
                        state = 'up'
            last = arr[i]
        return peak

x = Solution()
ans = x.peakIndexInMountainArray( [24,69,100,99,79,78,67,36,26,19])
print(ans)