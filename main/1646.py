class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        arr = [0] * (n + 1)
        arr[1] = 1
        max_arr = 1
        for i in range(n + 1):
            if 2 <= 2 * i <= n:
                arr[2 * i] = arr[i]
            if 2 <= 2 * i + 1 <= n:
                tmp = arr[i] + arr[i + 1]
                arr[2 * i + 1] = tmp
                if tmp > max_arr:
                    max_arr = tmp
        return max_arr



