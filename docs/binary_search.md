# 二分搜索

[TOC]

## 基本思想

对于给定数组$n[]$，考虑待搜索区间为左闭右开

$$[\text{left}, \text{right})$$

要能够进行搜索，区间必须为非空，因此必须满足（循环进行的条件）

$$\text{left} < \text{right}$$

取区间中点

$$\text{mid} = (\text{left} + \text{right}) // 2$$

有关于索引的单调（递增，一般而言）函数$f(i)$，通过判断$f(\text{mid})$与$0$的大小关系，可以决定下一轮的搜索区间是什么。

搜索区间可以视作无遗漏地划分为三个区间：

$$
[\text{left} , \text{mid}),
[\text{mid} , \text{mid} + 1),
[\text{mid} + 1, \text{right})
$$

现在的问题是：下一轮的目标解落在哪个区间？

## 使用中点$\text{mid}$作返回值

二分的简单应用是直接判断$\text{mid}$上是否成立并且直接返回，应用问题场景如：

### 搜索特定值

考虑需要在数组中搜索一个特定值$t$的下标$i$。

特别地，$[\text{mid} , \text{mid} + 1)$即为仅包含中点的单元素集合$\{ \text{mid} \}$，如果我们计算得到

$$x[\text{mid}] == t$$

那么我们得到$t$的下标就是$\text{mid}$，因为：

$$ i \in \{\text{mid}\}  \rightarrow i == \text{mid} $$

如果$x[\text{mid}] > t$，说明$t$一定落在左区间，因此下一个搜索区间有

$$\text{right} = \text{mid}$$

反之，如果$x[\text{mid}] < t$

## 使用区间端点$\text{left}$作返回值

二分还可以进行更加复杂一点的设计，不是返回中点$\text{mid}$，而是将迭代到达边界时的搜索区间端点作为对目标的标记进行返回：

### 小于目标值的最大下标

类似这种问题


### 数组中（大于/小于/大于等于/小于等于）目标值的最小/大下标

目标是否在数组中是一个问题，因为如果不在数组中，大于/小于目标值可能是无解的，这个时候需要额外处理这种情况。

左闭右开区间：
```py
def min_i_gt_t(n: list[int], t: int):
    left = 0
    right = len(n)
    while left < right:
        mid = (left + right) // 2
        if n[mid] <= t:
            left = mid + 1
        else:
            right = mid
    return left
```

```py
def max_i_lt_t(n: list[int], t: int):
    left = 0
    right = len(n)
    while left < right:
        mid = (left + right) // 2
        if n[mid] < t:
            left = mid + 1
        else:
            right = mid
    return left - 1
```

## 总结