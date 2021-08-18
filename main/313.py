import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        if n == 1:
            return 1

        pq = [1]
        visited = {1}

        def f():
            count = 1
            while True:
                x = heapq.heappop(pq)
                if count == n:
                    return x
                for p in primes:
                    tmp = x * p
                    if tmp not in visited:
                        heapq.heappush(pq, tmp)
                        visited.add(tmp)
                count += 1

        return f()


cases = [
    (12, [2, 7, 13, 19])
]
for case in cases:
    ans = Solution().nthSuperUglyNumber(*case)
    print(ans)
