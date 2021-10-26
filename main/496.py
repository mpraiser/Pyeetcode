class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []
        # monotone stack
        for x in reversed(nums2):
            while len(stack) > 0 and stack[-1] <= x:
                # stack top should strictly > x
                stack.pop()
            next_greater[x] = stack[-1] if len(stack) > 0 else -1
            stack.append(x)
        ret = [next_greater[x] for x in nums1]
        return ret


cases = [
    ([4, 1, 2], [1, 3, 4, 2]),
]
for case in cases:
    ans = Solution().nextGreaterElement(*case)
    print(case, ans)
