from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # simple version of itertools.product
        def product(*args: str) -> List[str]:
            result = ['']
            for pool in args:
                result = [x+y for x in result for y in pool]
            return result

        d2c = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        if digits == "":
            return []
        pools = (d2c[d] for d in digits)
        return product(*pools)


ans = Solution().letterCombinations("23")
print(ans)


# def d2c(digit: str):
#     left = (ord(digit) - ord("2")) * 3
#     return tuple(chr(ord("a") + i) for i in range(left, left+3))

# d = {}
# for i in range(2, 7):
#     d[str(i)] = d2c(str(i))