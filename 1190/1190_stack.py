from typing import Tuple


class Solution:
    def reverseParentheses(self, s: str) -> str:
        

        def reverseOne(s: str):
            stack = []
            result = ''
            for p in range(len(s)):
                # print(s[p])
                if s[p] == '(':
                    stack.append(result)
                    result = ''
                elif s[p] == ')':
                    result = stack.pop() + result[::-1]
                else:
                    result += s[p]
            return result
        return reverseOne(s)


x = Solution()
ans = x.reverseParentheses("(u(love)i)")
print(ans)