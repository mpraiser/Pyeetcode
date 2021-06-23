from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        List of width-bit int
        where target occur 1 time, other int occurs M times
        """
        WIDTH = 32
        M = 3
        counter = [0] * WIDTH
        for n in nums:
            for bit in range(WIDTH):
                counter[bit] += n & 1
                n >>= 1
        res = 0
        for bit in range(WIDTH):
            res |= (counter[bit] % M) << bit
        return res


ans = Solution().singleNumber([3,4,3,3])
print(ans)
        