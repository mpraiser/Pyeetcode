class Solution:
    def getSum(self, a: int, b: int) -> int:
        BITWIDTH = 32

        def atom_add(x: int, y: int, ci: int) -> tuple[int, int]:
            """x + y + ci -> (sum, co)"""
            s = x ^ y ^ ci
            co = (x and y) or (ci and (x or y))
            return s, co

        def unsigned_add(x: tuple[int], y: tuple[int], *, bitwidth) -> tuple[int]:
            result: list[int] = []
            ci = 0
            for i in reversed(range(bitwidth)):
                s, co = atom_add(x[i], y[i], ci)
                result.insert(0, s)
                ci = co
            return tuple(result)

        def reverse(x: tuple[int]) -> tuple[int]:
            return tuple(1 if d == 0 else 0 for d in x)

        def reverse_add_one(x: tuple[int], *, bitwidth) -> tuple[int]:
            one = tuple([0] * (bitwidth - 1) + [1])
            return unsigned_add(
                reverse(tuple(x)),
                one,
                bitwidth=bitwidth
            )

        def int2complement(x: int) -> tuple[int]:
            if x >= 0:
                sign = 0
            else:
                sign = 1
                x = -x
            value: list[int] = []
            for _ in range(BITWIDTH - 1):
                x, digit = divmod(x, 2)
                value.insert(0, digit)
            if sign == 1:
                value = list(
                    reverse_add_one(tuple(value), bitwidth=BITWIDTH - 1)
                )
            complement = tuple([sign] + value)
            return complement

        def complement2int(x: tuple[int]) -> int:
            # note: - 2 ** BITWIDTH has not true form!
            sign = x[0]
            value = x[1:]
            if sign == 1:
                if all(digit == 0 for digit in value):
                    return - 2 ** (BITWIDTH - 1)
                value = reverse_add_one(value, bitwidth=BITWIDTH - 1)
            weight = 1
            result = 0
            for digit in reversed(value):
                result += weight * digit
                weight *= 2
            if sign == 1:
                result *= -1
            return result

        ca = int2complement(a)
        cb = int2complement(b)
        cs = unsigned_add(ca, cb, bitwidth=BITWIDTH)
        return complement2int(cs)


sol = Solution()
for a in range(-1000, 1000 + 1):
    for b in range(-1000, 1000 + 1):
        s = sol.getSum(a, b)
        st = a + b
        print(a, b, st, s)
        assert s == st
