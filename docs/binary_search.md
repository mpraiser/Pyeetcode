# 二分搜索

## 数组中（大于/小于/大于等于/小于等于）目标值的最小/大下标

目标是否在数组中是一个问题，因为如果不在数组中，大于/小于目标值可能是无解的，这个时候需要额外处理这种情况。

左闭右开区间：
```py
def min_i_gt_t(n: List[int], t: target):
    left = 0
    right = len(n)
    while left < right:
        mid = (left + right) // 2
        if n[mid] > t:
            left = mid + 1
        else:
            right = mid
    return left
```
