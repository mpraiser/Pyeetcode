from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 0是xor的幺元
        x_xor_y = 0
        x = 0
        y = 0

        for n in nums:
            x_xor_y ^= n

        m = 1  # mask
        while x_xor_y & m == 0:
            m = m << 1
        
        for n in nums:
            if m & n == 0:
                x ^= n
            else:
                y ^= n
        
        return [x, y]


ans = Solution().singleNumbers([1, 2, 5, 2])
print(ans)
