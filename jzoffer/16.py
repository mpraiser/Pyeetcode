class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fpow(x, n):
            """
            Returns: x ** n
            """
            if n < 0:
                return 1 / fpow(x, -n)
            elif n == 0:
                return 1
            elif n == 1:
                return x
            else:
                half_n = n // 2
                half_pow = fpow(x, half_n) 
                result = half_pow * half_pow
                if n % 2 == 1:
                    result *= x
                return result
        return fpow(x, n)        

x = Solution()
ans = x.myPow(2, -2)
print(ans)