from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        ret: List[List[int]] = []

        for k in range(len(nums)-2):
            if nums[k] > 0:
                # beacause nums[k] <= nums[i] <= nums[j]
                # sum of them could not be 0
                break
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = len(nums) - 1
            while i < j:
                s = nums[i] + nums[j]
                t = -nums[k]
                if s == t:
                    ret.append([nums[k], nums[i], nums[j]])
                    # increase i until nums[i] becomes bigger
                    while i < j and nums[i+1] == nums[i]:
                        i += 1
                    i += 1
                    # decrease j until nums[j] becomes smaller
                    while i < j and nums[j-1] == nums[j]:
                        j -= 1
                    j -= 1
                elif s < t:
                    i += 1
                elif s > t:
                    j -= 1
        return ret


cases = [
    [-1,0,1,2,-1,-4],
    [0,0,0,0],
    [-2,0,1,1,2],
    [-1,0,1,2,-1,-4]
]
ans = Solution().threeSum(cases[3])
print(ans)