from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Algorithm
        major = -1
        count = 0
        for n in nums:
            if count == 0:
                major = n
            if n == major:
                count += 1
            else:
                count -= 1
        if count <= 0:
            return -1
        count = 0
        for n in nums:
            if n == major:
                count += 1
            if count > len(nums) / 2:
                return major
        return -1
        

        
ans = Solution().majorityElement([1,2,3])
print(ans)