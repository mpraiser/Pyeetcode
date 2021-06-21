from typing import List, Tuple


class Solution:
    def permutation(self, s: str) -> List[str]:
        
        def helper(depth) -> List[Tuple[str, List]]:
            if depth == 1:
                return [(c, [i]) for i, c in enumerate(s)]

            result = []
            for i, c in enumerate(s):
                result += [(c + y[0], [i] + y[1]) for y in helper(depth - 1) if i not in y[1]]
            return result

        result = set()
        for item in helper(len(s)):
            result.add(item[0])
        return list(result)


ans = Solution().permutation("aab")
print(ans)