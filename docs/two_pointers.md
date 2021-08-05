# 双指针

## 同向双指针

在有序数组$n$内找到$i$，$j$使得$f(n_i, n_j) \oplus  0$成立，$\oplus$可以为$=$、$>$、$\geq$、$<$、$\leq$，其中$f$在两个维度上分别单调。

### a + b = c

```py
def f(n: List[int], c: int) -> Tuple[int, int]:
    ans = 0
    i = 0
    j = len(n) - 1
    while i < j:
        if n[i] + n[j] == c:
            return (i, j)
        elif n[i] + n[j] < c:
            i += 1
        elif n[i] + n[j] > c:
            j -= 1
```

### a + b < c

```py
def f(n: List[int], c: int) -> int:
    ans = 0
    i = 0
    j = len(n) - 1
    while i < j:
        if n[i] + n[j] >= c:
            j -= 1
        else:
            ans += j - i  # for fixed i, number of (i, j)
            i += 1
    return ans
```

### a + b > c

```py
def f(n: List[int], c: int) -> int:
    ans = 0
    i = 0
    j = len(n) - 1
    while i < j:
        if n[i] + n[j] <= c:
            i += 1
        else:
            ans += j - i  # for fixed j, number of (i, j)
            j -= 1
    return ans
```