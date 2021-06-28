from typing import List
from queue import Queue


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        len(target) == 4
        len(item) == 4 for item in deadends
        """
        n = len(target)
        deadends = set(deadends)

        cache = dict()
        cache["0000"] = 0
        for dead in deadends:
            cache[dead] = -1

        for index in range(n):
            for i in range(1, 10):
                cache[f"{i * 10 ** index:04d}"] = i

        def f(current: str, visited: set) -> int:
            """Returns n-times to reach target"""
            if current in cache and cache[current] is not None:
                return cache[current]
            
            queue = Queue()
            for i in range(n):
                # fix 1 bit, change other bits
                choices = [str((int(current[i]) - 1) % 10), str((int(current[i]) + 1) % 10)]
                for choice in choices:
                    latter = "".join(
                        (item if index != i else choice for index, item in enumerate(current))
                        )
                    if latter not in cache and latter not in visited:
                        queue.put(latter)

            while
                        cache[latter] = None
                        visited = visited.copy()
                        visited.add(latter)
                        solution = f(latter, visited) + 1
                        cache[latter] = solution
                        if solution != -1:
                            solutions.append(solution)
                    elif cache[latter] is not None:
                        if cache[latter] != -1:
                            solutions.append(cache[latter] + 1)
            solutions = []
            if solutions:
                result = min(solutions)
                cache[current] = result
                return result
            else:
                cache[current] = -1
                return -1

        return f(target, set())


ans = Solution().openLock(["0201","0101","0102","1212","2002"], "0202")
print(ans)