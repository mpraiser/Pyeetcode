DP?

已知$f(\mathbf{x}_0),\ \mathbf{x}_0 \in \Psi$与$f$的递推表达式：

$$f(\mathbf{x}) = \left\{
    \begin{aligned}
        & f(\mathbf{x}_0)   & \mathbf{x}_0 \in \Psi \\
        & g(\mathbf{x}, f)  & \text{otherwise}   
    \end{aligned}
    \right.$$

如果$g$比较简单，且从$f(\mathbf{x}_0),\ \mathbf{x}_0 \in \Psi$出发，可以遍历所有$f$的定义域（目标的解空间），使用**动态规划**？