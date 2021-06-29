from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dq = deque()
        max_len = 0
        for x in s:
            if len(dq) > 0 and x in dq:
                while True:
                    y = dq.popleft()
                    if y == x:
                        break
            dq.append(x)
            if len(dq) > max_len:
                max_len = len(dq)
        return max_len


cases = ["abcabcbb", "bbbbb", "pwwkew"]
for case in cases:
    ans = Solution().lengthOfLongestSubstring(case)
    print(ans)