class Solution:
    def findComplement(self, num: int) -> int:
        ret = 0
        mask = 0x1
        while num:
            digit = num & 0x1
            if not digit:
                ret |= mask
            num >>= 1
            mask <<= 1
        return ret


cases = [
    5, 1
]
for case in cases:
    ans = Solution().findComplement(case)
    print(case, ans)