class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def area(x1, y1, x2, y2):
            return abs(x2 - x1) * abs(y2 - y1)

        ret = area(ax1, ay1, ax2, ay2) + area(bx1, by1, bx2, by2)
        # step 1: judge whether intersection exists.
        if not (by1 > ay2 or by2 < ay1 or bx1 > ax2 or bx2 < ax1):
            # step 2: calculate intersection area.
            condition_x1 = ax1 <= bx1 <= ax2
            condition_y1 = ay1 <= by1 <= ay2
            condition_x2 = ax1 <= bx2 <= ax2
            condition_y2 = ay1 <= by2 <= ay2
            cx1 = ax1 if not condition_x1 else bx1
            cx2 = ax2 if not condition_x2 else bx2
            cy1 = ay1 if not condition_y1 else by1
            cy2 = ay2 if not condition_y2 else by2
            ret -= area(cx1, cy1, cx2, cy2)
        return ret


cases = [
    ((-2, -2, 2, 2, -2, -2, 2, 2), 16),
    ((-2, -2, 2, 2, -3, -3, 3, -1), 24),
    ((-3, 0, 3, 4, 0, -1, 9, 2), 45),
    ((-1, -1, 1, 1, -2, -2, 2, 2), 16),
    ((-2, -2, 2, 2, 3, 3, 4, 4), 17),
    ((-2, -2, 2, 2, -1, 4, 1, 6), 20)
]

for data, correct in cases:
    ans = Solution().computeArea(*data)
    print(correct, ans)

# data, correct = cases[2]
# ans = Solution().computeArea(*data)
# print(correct, ans)
