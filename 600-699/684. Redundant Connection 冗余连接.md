
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/redundant-connection/description/

## 题目描述

In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of ``edges``. Each element of ``edges`` is a pair ``[u, v]`` with u < v, that represents an undirected ``edge`` connecting nodes u and v.

Return an ``edge`` that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge ``[u, v]`` should be in the same format, with u < v.

    Example 1:
    
    Input: [[1,2], [1,3], [2,3]]
    Output: [2,3]
    Explanation: The given undirected graph will be like this:
      1
     / \
    2 - 3
    
    Example 2:
    
    Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
    Output: [1,4]
    Explanation: The given undirected graph will be like this:
    5 - 1 - 2
        |   |
        4 - 3

Note:

1. The size of the input 2D-array will be between 3 and 1000.
1. Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.


## 题目大意

给出了一个有环无向图的各个边，找出能去除的边，使得这个图不含环（即为树）。

注意，这个图中的各个节点是1～N,总共有N条边，即只多了一条边。

## 解题方法

### 并查集

上一次看这个题的时候，我知道使用``并查集``去做，但是并没有做出来。这次再次心平气和的看的时候，已经能一遍写出来了。

关于并查集，这个知识点有点大。简而言之，告诉你一条边，去集合里查找这条边的两个节点分别属于哪个树。根据是否属于同一个树，做后续的判断。我之前的一篇文章讲述了并查集的一种应用：[【九度OJ】题目1012：畅通工程 解题报告][1]。更多的资料，可以看《计算机考研——机试指南》。

下面的代码实现了并查集查找根节点的代码，并且做了路径压缩，防止树太高导致查找根节点缓慢。

具体到这个题，虽然说是返回最后一个边，但我们知道只需要去除一条边就够了，之前的边不会构成环，直至多余的那条边出现。

另外要注意，当一条边的左右节点的根节点不同时，要把他们设置相同，这样等下次判断某条边的左右节点相同的情况时，说明是多余的那条边了。

python代码如下：

```python
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        tree = [-1] * (len(edges) + 1)
        for edge in edges:
            a = self.findRoot(edge[0], tree)
            b = self.findRoot(edge[1], tree)
            if a != b:
                tree[a] = b
            else:
                return edge
        
        
    def findRoot(self, x, tree):
        if tree[x] == -1: return x
        else:
            root = self.findRoot(tree[x], tree)
            tree[x] = root
            return root
```

C++代码如下：

```cpp
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        const int N = 1001;
        m_ = vector<int>(N, 0);
        for (int i = 0; i < N; ++i) {
            m_[i] = i;
        }
        for (auto edge : edges) {
            if (!u(edge[0], edge[1]))
                return edge;
        }
        return {0, 0};
    }
private:
    vector<int> m_;
    int f(int a) {
        if (m_[a] != a) 
            m_[a] = f(m_[a]);        
        return m_[a];
    }
    bool u(int a, int b) {
        int fa = f(a);
        int fb = f(b);
        if (fa == fb)
            return false;
        m_[fa] = b;
        return true;
    }
};
```

## 日期

2018 年 5 月 28 日 —— 太阳真的像日光灯～
2019 年 1 月 25 日 —— 这学期最后一个工作日

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/60962744
