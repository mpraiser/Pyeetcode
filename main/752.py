from typing import List
from queue import Queue


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        len(target) == 4
        len(item) == 4 for item in deadends
        """
        pass


ans = Solution().openLock(["0201","0101","0102","1212","2002"], "0202")
print(ans)