from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        ret = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                t = target - nums[i] - nums[j]
                m = j + 1
                n = len(nums) - 1
                while m < n:
                    s = nums[m] + nums[n]
                    if s == t:
                        ret.append([nums[i], nums[j], nums[m], nums[n]])
                        while m < n and nums[m] == nums[m+1]:
                            m += 1
                        m += 1
                        while m < n and nums[n] == nums[n-1]:
                            n -= 1
                        n -= 1
                    elif s < t:
                        m += 1
                    elif s > t:
                        n -= 1
        return ret
                
       
ans = Solution().fourSum([1,0,-1,0,-2,2], 0)
print(ans)