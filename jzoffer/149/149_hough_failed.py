from typing import List
from math import sqrt, cos, sin


def plot(figure: List[List[int]]):
    from matplotlib import pyplot as plt
    import numpy as np

    plt.imshow(np.array(figure),cmap='gray')
    plt.show()


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        r_max = int(max(
            (sqrt(p[0] ** 2 + p[1] ** 2) for p in points)
            )) + 1
        theta_max = 180 + 1
        vote = [[0] * r_max for _ in range(theta_max)]
        for p in points:
            for theta in range(theta_max):
                r = int(p[0] * cos(theta) + p[1] * sin(theta))
                vote[theta][r] += 1

        vote_max = vote[0][0]
        for theta in range(theta_max):
            for r in range(r_max):
                if vote[theta][r] > vote_max:
                    vote_max = vote[theta][r]

        return vote_max


a = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
b = [[1,1],[2,2],[3,3]]
c = [[-9,-651],[-4,-4],[-8,-582],[9,591],[-3,3]]
ans = Solution().maxPoints(c)
print(ans)
