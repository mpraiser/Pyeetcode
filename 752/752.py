from typing import List, Tuple
from functools import cache


def n_diff(a: str, b: str):
    """number of differences in a and b"""
    assert len(a) == len(b)
    n = len(a)
    counter = 0
    for i in range(n):
        if a[i] != b[i]:
            counter += 1
    return counter


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        len(target) == 4
        len(item) == 4 for item in deadends
        """
        n = len(target)
        deadends = set(deadends)
        basic_choices = set((str(i) for i in range(10)))

        cache = {}
        cache["0000"] = 0
        for dead in deadends:
            cache[dead] = -1

        def f(current: str) -> int:
            """Returns n-times to reach target"""
            if current in cache and cache[current] is not None:
                return cache[current]
            
            solutions = []
            for i in range(n):
                # fix 1 bit, change other bits
                if current[i] == "0":
                    for j in (m for m in range(n) if m != i):
                        choices = [str((int(current[j]) - 1) % 10), str((int(current[j]) + 1) % 10)]
                        for choice in choices:
                            latter = "".join(
                                (item if index != j else choice for index, item in enumerate(current))
                                )
                            if latter not in cache:
                                cache[latter] = None
                                solution = f(latter) + 1
                                cache[latter] = solution
                                if solution != -1:
                                    solutions.append(solution) 
                            elif cache[latter] is not None:
                                if cache[latter] != -1:
                                    solutions.append(cache[latter] + 1) 
            
            if solutions:
                result = min(solutions)
                cache[current] = result
                return result
            else:
                cache[current] = -1
                return -1

        return f(target)

ans = Solution().openLock(["0201","0101","0102","1212","2002"], "0202")
print(ans)