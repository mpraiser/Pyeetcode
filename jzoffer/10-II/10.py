import functools

@functools.cache
def f(n: int) -> int:
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (f(n-1) + f(n-2)) % 1000000007

class Solution:
    def numWays(self, n: int) -> int:
        return f(n)


print(f(2))
print(f(7))
print(f(0))