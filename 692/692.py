import random
from collections import Counter
from typing import List
from operator import itemgetter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # get count
        counter = Counter(words)
        counted = list(counter.items())
        counted.sort(key=itemgetter(0))
        counted.sort(key=itemgetter(1), reverse=True)
        
        result = [counted[i][0] for i in range(k)]
        return result
    

x = Solution()
# ans = x.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
ans = x.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
print(ans)