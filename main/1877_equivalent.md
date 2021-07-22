给定一向量$\mathbf{x}$，长度为$2k, k \in N^+$（即为偶数）

$$\mathbf{x} = [x_0, x_1, \cdots, x_{2k-1}]^T$$

$\mathbf{x}^{(i)}$是$\mathbf{x}$的一个排列。如对于$\mathbf{x} = [1, 2, 3, 4]^T$，$\mathbf{x}^{(0)} = [4, 2, 3, 1]^T$是$\mathbf{x}$的一个排列。

所有可能形成的排列的集合为：

$$P(\mathbf{x}) = \{\mathbf{x}^{(i)}\}$$

函数$f(\mathbf{x})$为求$\mathbf{x}$中元素“首尾相加”的最大值

$$
\begin{aligned}
    f(\mathbf{x}) &= \max \left(
        \begin{bmatrix}
            1 &   &   & \cdots & \cdots &   &   & 1 \\
            & 1 &   & \cdots & \cdots &   & 1 &   \\
            &   & 1 & \cdots & \cdots & 1 &   &   \\
            &   &   & \cdots & \cdots &   &   &   \\
            &   &   & 1 & 1 &   &   &
        \end{bmatrix}
        \begin{bmatrix}
            x_0 \\ x_1 \\ x_2 \\ \cdots \\ x_{2k-1}
        \end{bmatrix}
    \right) \\
    &= \max\left(
            \begin{matrix}
                x_0+x_{2k-1} \\ x_1+x_{2k-2} \\ x_2+x_{2k-3} \\ \cdots \\ x_k + x_{k+1}
            \end{matrix}
        \right)
\end{aligned}    
$$

求证当所有排列$P(\mathbf{x})$中的排列$\mathbf{x}^{(i)}$使得$f(\mathbf{x}^{(i)})$最小时

$$\mathbf{x}^{(\text{opt})} = \arg\min_{\mathbf{x}^{(i)}}
    \{f(\mathbf{x}^{(i)}) \big| \mathbf{x}^{(i)} \in P(\mathbf{x})\}
$$

对于$\mathbf{x}^{(\text{opt})}$满足：

$$x_0^{(\text{opt})} \leq x_1^{(\text{opt})} \leq x_2^{(\text{opt})} \leq \cdots \leq x_{2k-1}^{(\text{opt})} $$