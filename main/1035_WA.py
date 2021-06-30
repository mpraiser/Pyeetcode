from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # find all possible pair
        pairs = []
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                if  x == y:
                    pairs.append((i, j))
        
        if len(pairs) <= 1:
            return len(pairs)

        def cross(pair1, pair2) -> bool:
            return not (((pair1[0] > pair2[0]) and (pair1[1] > pair2[1])) or ((pair1[0] < pair2[0]) and (pair1[1] < pair2[1])))

        # delete conflict
        while True:
            # calculate how many cross
            cross_cnt = {}
            for p in pairs:
                cross_cnt[p] = 0

            for i in range(len(pairs)-1):
                for j in range(i+1, len(pairs)):
                    if cross(pairs[i], pairs[j]):
                        cross_cnt[pairs[i]] += 1
                        cross_cnt[pairs[j]] += 1
            
            max_item = max(cross_cnt.items(), key=lambda x: x[1])

            if max_item[1] > 0:
                pairs.remove(max_item[0])
            else:
                break

        return len(pairs)


x = Solution()
# ans = x.maxUncrossedLines([1,4,2], [1,2,4])
# print(ans)
# ans = x.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2])
# print(ans)
# ans = x.maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1])
# print(ans)
# ans = x.maxUncrossedLines([1], [3])
# print(ans)
# ans = x.maxUncrossedLines([2,1], [1,2,1,3,3,2])
# print(ans)
ans = x.maxUncrossedLines([1,1,3,5,3,3,5,5,1,1], [2,3,2,1,3,5,3,2,2,1])
print(ans)