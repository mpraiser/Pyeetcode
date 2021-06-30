from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> str:
        counter = OrderedDict()
        for c in s:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1
        
        for c in counter:
            if counter[c] == 1:
                return c
                
        return " "