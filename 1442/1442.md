## 前缀和

给定一个序列$[x_i]$，和二元运算$\times$，$\times$符合交换律，结合律，$\ast$的**幺元**为$\theta$，满足：

$$\theta \times x = x$$

对于其中每一个元素依次计算，累计结果为$[S_i]$，称作**前缀和**。有递归定义：

$$S_i = 
\left\{\begin{aligned}
    \theta                   &, i =  0\\
    S_{i-1} \times x_{i-1} &, i \geq 1
\end{aligned}\right.$$

$S_i$具有以下计算形式：

$$S_i = \theta \times x_0 \times x_1 \times x_2 \times \cdots \times x_{i-1}$$

对应代码可能如：

```py
s_i = reduce(f, x[:i], initializer=theta)
```

定义在左闭右开区间$[a, b)$上的使用运算$\times$的**积分**运算$\int$，有：

$$\int_a^b x_i = 
\left\{\begin{aligned}
    x_a \times x_{a+1} \times \cdots \times x_{b-1} &, b > a+1 \\
    x_a &, b = a+1 \\
    \theta &, b = a
\end{aligned}\right.$$

则**前缀和**可以表示为：

$$S_n = \int_0^n x_i$$

该积分具有以下性质：

$$\int_0^b x_i = \int_0^a x_i \times \int_{a}^b x_i$$

如果$\times$存在逆运算$\otimes$，则有：

$$
\begin{aligned}
    \int_0^a x_i \otimes \int_0^b x_i &= \int_0^a x_i \otimes \int_0^a x_i \times \int_{a}^b x_i \\
    \int_0^a x_i \otimes \int_0^b x_i &= \theta \times \int_{a}^b x_i
\end{aligned}$$

即：

$$\int_{a}^b x_i = \int_0^a x_i \otimes \int_0^b x_i = S_b \otimes S_a $$