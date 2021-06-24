from typing import List
from math import inf


def eq_appr(x, y):
    PRECISION = 1e-4
    return x - PRECISION <= y <= x + PRECISION


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        hough = {}
        

        if len(points) == 1:
            return 1
        
        for i in range(len(points) - 1):
            for j in range(i+1, len(points)):
                # 两点互不相同
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]

                if x1 == x2:
                    k = inf
                else:
                    k = (y1 - y2) / (x1 - x2)

                b_this = y1 - x1  * k 

                if k not in hough:
                    hough[k] = {}
                if k == inf:
                    hough[k][x1] = 0
                else:
                    exist = False
                    for b in hough[k]:
                        if eq_appr(b, b_this):
                            exist = True
                            break
                    if not exist:
                        hough[k][b_this] = 0
        
        for (x, y) in points:
            for k in hough:
                if k == inf:
                    for x0 in hough[k]:
                        if x0 == x:
                            hough[k][x0] += 1
                else:
                    b_this = y - x * k
                    for b in hough[k]:
                        if eq_appr(b, b_this):
                            hough[k][b] += 1

        hough_max = 0
        for k in hough:
            for b in hough[k]:
                if hough[k][b] > hough_max:
                    hough_max = hough[k][b]
        return hough_max
        
        
a = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
b = [[1,1],[2,2],[3,3]]
c = [[-9,-651],[-4,-4],[-8,-582],[9,591],[-3,3]]
d = [[-9,-651],[-8,-582],[9,591]]
e = [[-6,-1],[3,1],[12,3]]
z = [[0,0], [1,1], [2,2], [3,3]]
ans = Solution().maxPoints(e)
print(ans)
