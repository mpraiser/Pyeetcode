from typing import List
from functools import cache


def nth_digit(n: int, i: int) -> int:
    return int(str(n)[i])


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        """
            len(nums) >= 1
        """
        def dfs(choices: tuple, last: str) -> str:
            # find min first-digit
            if len(choices) > 1:
                solutions = []
                indices = {}
                for i, choice in enumerate(choices):
                    if choice not in indices:
                        indices[choice] = i
                weight = 0 #
                # min_width = min((len(str(x)) for x in choices))
                while True:
                    ds = [nth_digit(choice, weight) for choice in indices]
                    min_d = min(ds)
                    filtered_indices = {}

                    for seq, choice in enumerate(indices):
                        if ds[seq] == min_d:
                            width = len(str(choice))
                            if width == weight + 1:
                                solutions.append(
                                        dfs(choices[:indices[choice]] + choices[indices[choice]+1:], 
                                            last + str(choice))
                                    )
                            elif width > weight + 1:
                                filtered_indices[choice] = indices[choice]
                    if not filtered_indices:
                        break
                    else:
                        indices = filtered_indices
                        weight += 1
                return min(solutions, key=lambda x: int(x))
            else:
                return last + str(choices[0])

        return dfs(tuple(nums), "")


a = [3,30,34,5,9]
b = [123, 321]
c = [41,23,87,55,50,53,18,9,39,63,35,33,54,25,26,49,74,61,32,81,97,99,38,96,22,95,35,57,80,80,16,22,17,13,89,11,75,98,57,81,69,8,10,85,13,49,66,94,80,25,13,85,55,12,87,50,28,96,80,43,10,24,88,52,16,92,61,28,26,78,28,28,16,1,56,31,47,85,27,30,85,2,30,51,84,50,3,14,97,9,91,90,63,90,92,89,76,76,67,55]
d = [1,2,4,8,16,32,64,128,256,512]

# ans = Solution().minNumber(c)
# print(ans)


import time
for i in reversed(range(len(c)-1)):
    t = time.time()
    ans = Solution().minNumber(c[:len(c)-i])
    print(len(c)-i, f"{time.time()-t:.2f}")

            