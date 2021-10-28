class Solution:
    @staticmethod
    def split(number: int) -> tuple:
        # split into digits and sort
        digits = []
        while number:
            number, digit = divmod(number, 10)
            digits.append(digit)
        digits.sort()
        return tuple(digits)

    def reorderedPowerOf2(self, n: int) -> bool:
        power_of_two = set()
        power = 1
        while power < 10 ** 9:
            digits = self.split(power)
            power_of_two.add(digits)
            power <<= 1

        digits = self.split(n)
        return digits in power_of_two


cases = [
    1, 10, 16, 24, 46
]
for case in cases:
    ans = Solution().reorderedPowerOf2(case)
    print(case, ans)

# case = 56635
# ans = Solution().reorderedPowerOf2(case)
# print(case, ans)
