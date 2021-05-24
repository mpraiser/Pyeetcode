import functools

class Solution:
    def strangePrinter(self, s: str) -> int:
        def preprocess(s):
            p = ''
            last = ''
            for x in s:
                if x != last:
                    p += x
                    last = x
            return p

        s = preprocess(s)

        @functools.lru_cache(maxsize=None)
        def f(a, b):
            """
            min times in [a, b)
            """
            
            if b <= a:
                return 0
            elif b == a+1:
                return 1
            elif b == a+2:
                return 2 if s[a] != s[a+1] else 1
            else:
                # at least 2 elements in [a, b)
                if s[a] == s[b-1]:
                    # base on both sides
                    # return f(a+1, b-1) + 1
                    return min([f(a, b-1), f(a+1, b)])
                else:
                    # base as the left one or the right one
                    # base as left
                    return min([f(a, k)+f(k, b) for k in range(a+1, b)])

        return f(0, len(s))

# inputs = ["aaa", "aaabbb", "aba", "baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa"]
# x = Solution()
# for i in inputs:
#     ans = x.strangePrinter(i)
#     print(ans)

x = Solution()
ans = x.strangePrinter("abababac")
print(ans)
