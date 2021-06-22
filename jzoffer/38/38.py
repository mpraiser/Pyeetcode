from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        result = []

        def helper(s, r):
            """
            Args:
                x: string to be chosen
                r: choosed string
            """
            if s == "":
                result.append(r)
            visted = set()
            for i, c in enumerate(s):
                if c not in visted:
                    visted.add(c)
                    helper(s[:i] + s[i+1:], r + c)

        helper(s, "")
        return result


ans = Solution().permutation("aab")
print(ans)