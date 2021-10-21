class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        base = 10
        ci = 1
        for i in reversed(range(len(digits))):
            ci, digits[i] = divmod(digits[i] + ci, base)
        if ci != 0:
            digits.insert(0, ci)
        return digits


cases = [
    [1, 2, 3],
    [9, 9]
]
for case in cases:
    ans = Solution().plusOne(case)
    print(case, ans)
