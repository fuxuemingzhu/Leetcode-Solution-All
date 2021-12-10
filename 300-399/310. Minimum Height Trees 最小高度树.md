作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/minimum-height-trees/description/


## 题目描述

For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains ``n`` nodes which are labeled from ``0`` to ``n - 1``. You will be given the number ``n`` and a list of undirected ``edges`` (each edge is a pair of labels).

You can assume that no duplicate edges will appear in ``edges``. Since all edges are undirected, ``[0, 1]`` is the same as ``[1, 0]`` and thus will not appear together in ``edges``.

Example 1 :

    Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
    
            0
            |
            1
           / \
          2   3 
    
    Output: [1]

Example 2 :

    Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    
         0  1  2
          \ | /
            3
            |
            4
            |
            5 
    
    Output: [3, 4]

Note:

1. According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
1. The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

## 题目大意

找出以哪些节点为根节点的时候，构建出来的整棵树的高度是最低的。


## 解题方法

### BFS

这个题很优秀啊，是个好题。这个题给定的是个图，但是让我们构建成树，也就是说构建出来的并不是二叉树。题目其实想考我们的是，整个图最靠近中间的节点是什么。我们使用类似与拓扑排序的BFS进行解决。

拓扑排序我们都知道，每次选择入度为0的节点进行删除。在这个题中，因为我们要找到无向图最靠近中间的节点，所以，我们先使用一个字典保存每个节点的所有相邻节点set。每次把所有只有一个邻接的节点（叶子节点，类似于入度为0，但是这是个无向图，入度等于出度）都放入队列，然后遍历队列中的节点u，把和每个节点u相邻的节点v的set删去u，所以这一步操作得到的是去除了叶子节点的新一轮的图。所以我们需要再次进行选择只有一个邻接节点的叶子节点，然后放入队列中，再次操作。最后结束的标准是，整个图只留下了1个或者两个元素。为什么不能是3个呢？因为题目第一句话说了给出的图是具有树的特性的，所以一定没有环存在。

这个题整体的思路就是把所有的叶子节点放入队列中，然后同时向中间遍历，这样最后剩下来的就是整棵树中间的元素。

时间复杂度是O(V)，空间复杂度是O(E + V).

```python
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        leaves = collections.defaultdict(set)
        for u, v in edges:
            leaves[u].add(v)
            leaves[v].add(u)
        que = collections.deque()
        for u, vs in leaves.items():
            if len(vs) == 1:
                que.append(u)
        while n > 2:
            _len = len(que)
            n -= _len
            for _ in range(_len):
                u = que.popleft()
                for v in leaves[u]:
                    leaves[v].remove(u)
                    if len(leaves[v]) == 1:
                        que.append(v)
        return list(que)
```


## 相似题目

[207. Course Schedule][1]
[210. Course Schedule II][2]

## 参考资料

http://www.cnblogs.com/grandyang/p/5000291.html

## 日期

2018 年 10 月 30 日 —— 啊，十月过完了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82951771
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/83302328
