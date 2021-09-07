class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_l = 0
        count_r = 0
        ret = 0
        for x in s:
            if x == "L":
                count_l += 1
            elif x == "R":
                count_r += 1
            if count_r == count_l and count_r > 0:
                ret += 1
                count_r = 0
                count_l = 0
        return ret
