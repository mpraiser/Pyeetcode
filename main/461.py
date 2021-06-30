class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        result = 0
        for i in range(31):
            result += (z & (1 << i)) >> i
        return result


x = Solution()
ans = x.hammingDistance(680142203, 1111953568)
print(ans)