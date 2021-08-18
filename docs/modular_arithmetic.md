# 模运算

$$(a + b) \bmod p = (a \bmod p + b \bmod p) \bmod p$$

$$(a - b) \bmod p = (a \bmod p - b \mod p + p) \bmod p$$

$$(ab) \bmod p = ((a \bmod p) (b \bmod p)) \bmod p$$

## 将答案对$m$取模

如果最终解$r$具有以下计算形式

$$r = \sum_{x} f(x)$$

且函数$f$具有以下计算形式

$$f(j) = \sum_{x} f(i)$$

现在要求对答案取$m$的模，即要求

$$
r \mod m = [\sum_{x} f(x)] \mod m \\
= [\sum_{x} (f(x) \mod m)] \mod m 
$$

定义辅助函数

$$g(x) = f(x) \mod m$$

那么有

$$
r \mod m = [\sum_{x} g(x)] \mod m 
$$

其中对于$g$有：

$$g(j) = f(j) \mod m \\
= [\sum_i f(i)] \mod m \\
= [\sum_i (f(i) \mod m)] \mod m \\
= [\sum g(i)] \mod m
$$

一般来讲，当$i = 0$时，有$f(i) < m$，因此$f(0) = g(0)$

想要修改$f$的代码为$g$：

```py
f[j] = reduce(lambda a, b: a + b, ..., 0)
```

代码改为

```py
f[j] = reduce(lambda a, b: (a + b) % m, ..., 0) 
```

即可满足要求，此时`f`含义为上式中的$g$。

对于$r$，对应的修改为

```py
r = reduce(lambda a, b: a + b, ..., 0) % m
```

> 对于两种形式：
> 
> ```py
> f1 = lambda array: reduce(lambda a, b: a + b, array, 0) % m
> f2 = lambda array: reduce(lambda a, b: (a + b) % m, array, 0)
> ```
> 
> 其实`f1`与`f2`是完全等价的。

> 证明？