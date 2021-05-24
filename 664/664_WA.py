import functools


class Solution:
    def strangePrinter(self, s: str) -> int:
        @functools.lru_cache(maxsize=None)
        def f(a, b):
            """
            min times in [a, b)
            """
            if b == a+1:
                return 1
            elif b <= a:
                return 0
            else:
                # at least 2 elements in [a, b)
                if s[a] == s[b-1]:
                    base = s[a]
                    i = a
                    j = b-1
                    while i < len(s) and s[i] == base:
                        i += 1
                    while j > 0 and s[j] == base:
                        j -= 1
                    return f(i, j+1) + 1
                else:
                    # base as the left one or the right one
                    base = s[a]
                    i = a
                    while i < len(s) and s[i] == base:
                        i += 1

                    base = s[b-1]
                    n = b-1
                    while n > 0 and s[n] == base:
                        n -= 1

                    return min([f(i, b)+1, f(a, n+1)+1])

        return f(0, len(s))

inputs = ["aaa", "aaabbb", "aba"]
x = Solution()
for i in inputs:
    ans = x.strangePrinter(i)
    print(ans)

# x = Solution()
# ans = x.strangePrinter("baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa")
# print(ans)
