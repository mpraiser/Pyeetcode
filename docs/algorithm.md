## 算法复杂度分析
### 大$O$符号

算法的原子操作数量随着数据规模$n$增长，定义函数$f(n)$为原子操作数量与数据规模$n$的关系，用大$O$符号表示$f(n)$符合某一族函数的特征：

$$f(n) \ \ \text{is} \ \ O(g(n))$$

等价于：

$$\lim_{n \rightarrow \alpha} \frac{f(n)}{g(n)} = C$$

其中$C$为常数，$\alpha$可以为$\infty。$

## 排序算法

### 稳定性

- 定义：能保证两个相等的数，经过排序之后，其在序列的前后位置顺序不变。
- 意义：对数据的某个特性进行排序后可以方便继续按另一个特性进行二次排序

### 归并排序


## 算法框架

### DFS

- 图的DFS，递归形式

```py
visited = set()

def dfs(node): 
    nonlocal visited
    for (u, v) in node.edges:
        if v not in visited:
            visited.add(v)
            dfs(v)
```

> 递归形式的DFS实际上隐含了一个栈。

- 图的DFS，迭代形式

```py
from collections import deque

def dfs(node):
    # initialization
    visited = set()
    stack = deque()
    stack.append(node)
    # start dfs
    while len(stack) > 0:
        node = stack.pop()
        for (u, v) in node.edges:
            if v not in visited:
                visited.add(v)
                stack.append(v)
```

### BFS

- 图的BFS，迭代形式

```py
from collections import deque

def bfs(node):
    # initialization
    visited = set()
    queue = deque()
    queue.append(node)
    # start bfs
    while len(queue) > 0:
        node = queue.popleft()
        for (u, v) in node.edges:
            if v not in visited:
                visited.add(v)
                queue.append(v)
```