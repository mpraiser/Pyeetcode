from typing import Tuple


class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        p = 0
        def reverseOne(s: str) -> Tuple[int, str]:
            nonlocal p
            result = ''
            while p < len(s):
                # print(s[p])
                if s[p] == '(':
                    p += 1 # skip this char
                    result += reverseOne(s)[::-1]
                elif s[p] == ')':
                    return result
                else:
                    result += s[p]
                p += 1
            return result
        return reverseOne(s)


x = Solution()
ans = x.reverseParentheses("(u(love)i)")
print(ans)