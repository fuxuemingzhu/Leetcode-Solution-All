# 【LeetCode】785. Is Graph Bipartite? 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/is-graph-bipartite/description/

## 题目描述：

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:

    Input: [[1,3], [0,2], [1,3], [0,2]]
    Output: true
    Explanation: 
    The graph looks like this:
    0----1
    |    |
    |    |
    3----2
    We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:

    Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
    Output: false
    Explanation: 
    The graph looks like this:
    0----1
    | \  |
    |  \ |
    3----2
    We cannot find a way to divide the set of nodes into two independent subsets.
 

Note:

1. graph will have length in range [1, 100].
1. graph[i] will contain integers in range [0, graph.length - 1].
1. graph[i] will not contain i or duplicate values.
1. The graph is undirected: if any element j is in graph[i], then i will be in graph[j].

## 题目大意

判断一个无向图是不是二分图。二分图的定义是，可以把一个图划分成两部分，使得图中的每个边的两个定点分别来自这两部分。

## 解题方法

这个题很容易理解了，做法也很简单，使用众所周知的染色法。可以通过BFS或者DFS来解决。我使用的是BFS.

使用一个visited数组来保存每个节点被染的颜色。0代表没染色，1代表染成蓝色，2代表染成红色。对图的每个顶点进行一个遍历，把和这个顶点相邻的顶点全部染成相反的颜色。如果相邻顶点已经染色，而且染色和当前顶点染色相同，则返回False。全部成功染色后返回True。

这个题没有说明是连通图，这个就很坑爹了，不能通过一次的BFS就把所有的顶点染色成功。所以需要的是一个外层的对顶点进行遍历，一个内层的对每个顶点相邻的顶点遍历，这样两重遍历才能保证每个顶点、这个顶点相邻的顶点都被强行的染色。

时间复杂度是O(E+V)，空间复杂度是O(E).

代码如下：

```python
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        visited = [0] * len(graph)# 0-not visited; 1-blue; 2-red;
        for i in range(len(graph)):
            if graph[i] and visited[i] == 0:
                visited[i] = 1
                q = collections.deque()
                q.append(i)
                while q:
                    v = q.popleft()#every point
                    for e in graph[v]:#every edge
                        if visited[e] != 0:
                            if visited[e] == visited[v]:
                                return False
                        else:
                            visited[e] = 3 - visited[v]
                            q.append(e)
        return True
```

参考资料：

https://leetcode.com/problems/is-graph-bipartite/discuss/115503/java-BFS

## 日期

2018 年 9 月 20 日 —— 趁年轻多读书
