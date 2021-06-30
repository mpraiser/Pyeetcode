from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        mids = []
        n = len(nums1) + len(nums2)
        n_mids = 1 if n % 2 == 1 else 2
        start = n // 2 if n % 2 == 1 else n // 2 - 1

        while len(mids) < n_mids:
            if j >= len(nums2) or (i < len(nums1) and nums1[i] < nums2[j]):
                if i + j >= start:
                    mids.append(nums1[i])
                i += 1
            else:
                if i + j >= start:
                    mids.append(nums2[j])
                j += 1
        
        return sum(mids) / len(mids)
        

cases = [
    ([1, 3], [2]),
    ([1, 2], [3, 4]),
    ([0,0], [0,0])
]
for case in cases:
    ans = Solution().findMedianSortedArrays(*case)
    print(ans)

# ans = Solution().findMedianSortedArrays(*cases[2])
# print(ans)