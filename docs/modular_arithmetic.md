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

$$g(j) = f(j) \mod m \\
= [\sum_i f(i)] \mod m \\
= [\sum_i (f(i) \mod m)] \mod m \\
= [\sum g(i)] \mod m
$$

对应到代码中，代码中$f$和$r$有计算形式

```py
f[j] = reduce(lambda a, b: a + b, ..., initializer=0)
r = reduce(lambda a, b: a + b, ..., initializer=0)
```

代码改为

```py
f[j] = reduce(lambda a, b: (a + b) % m, ..., initializer=0) 
r = reduce(lambda a, b: a + b, ..., initializer=0) % m
```

是满足要求的，此时`f`含义为上式中的$g$。



