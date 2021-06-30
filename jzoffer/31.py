from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push_ptr = 0
        stack = []
        for x in popped:
            # if i is stack top
            if stack and stack[-1] == x:
                stack.pop()
            # if i in pushed
            else:
                flag = False
                for j in range(push_ptr, len(pushed)):
                    if x == pushed[j]:
                        for m in range(push_ptr, j):
                            stack.append(pushed[m])
                        push_ptr = j + 1
                        flag = True
                        break
                if not flag:
                    return False
        return stack == []
            
            

# ans = Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1])
ans = Solution().validateStackSequences([1,2,3,4,5], [4,3,5,1,2])
print(ans)