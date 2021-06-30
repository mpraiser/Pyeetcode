from typing import List
from functools import lru_cache


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        @lru_cache
        def jumper(index :int, step: int):
            if index == len(stones) - 1:
                return True

            for j in range(index+1, len(stones)):
                if stones[index] + step + 1 == stones[j]:
                    if jumper(j, step+1):
                        return True
            
                if stones[index] + step == stones[j]:
                    if jumper(j, step):
                        return True

                if step > 1 and stones[index] + step - 1 == stones[j]:
                    if jumper(j, step-1):
                        return True
            
            return False

        return jumper(1, 1)


s = Solution()
result = s.canCross([0,1,3,5,6,8,12,17])
print(result)