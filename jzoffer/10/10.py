import functools

@functools.cache
def f(n: int) -> int:
    if n <= 1:
        return n
    else:
        return (f(n-1) + f(n-2)) % 1000000007

class Solution:
    def fib(self, n: int) -> int:
        return f(n)


print(f(2))
print(f(5))
print(f(45))