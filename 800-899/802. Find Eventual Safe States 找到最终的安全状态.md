# 【LeetCode】802. Find Eventual Safe States 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/find-eventual-safe-states/description/

## 题目描述：

In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:

    Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    Output: [2,4,5,6]
    Here is a diagram of the above graph.
    
![此处输入图片的描述][1]

Note:

1. graph will have length at most 10000.
1. The number of edges in the graph will not exceed 32000.
1. Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].

## 题目大意

题目有点难，需要我们抽象出来数学模型。题目的意思是，如果一个节点走过很多步之后无路可走了，认为这个节点是个安全节点。如果根本停不下来，那就是个不安全的节点。返回排序好了的所有安全节点的索引值。

题目给出的graph意思是每个节点的指向的下一个节点的索引。


## 解题方法

题目很容易抽象成一个查找一个节点是否在环中，或者经过一段路径之后在一个环中。所以使用的方法是DFS。

用0代表没有访问过，用1代表安全，用2代表不安全。其实就是把visited数组给拓展成了染色数组。

dfs函数的含义就是返回start节点是否是安全，如果是，返回True。

值得注意的是，默认是不安全还是安全。我刚开始考虑的是默认不安全，如果找到一个安全的路径就是安全的。这个是不对的，因为虽然这个节点通过一段路径之后能到达一个终点，但是经过另一个路径它就会进入环中。题目问的就是无论如何走都必须到达终点，即无论如何走都不会到达环中，这样的才是安全的。所以默认应该是不安全的。

代码如下：

```python
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        #color[i], 0 means not visited. 1 means safe. 2 means unsafe.
        color = [0] * len(graph)
        res = []
        for start in range(len(graph)):
            if self.dfs(graph, start, color):
                res.append(start)
        res.sort()
        return res
        
    def dfs(self, graph, start, color):
        # 返回start节点是否是安全，如果是，返回True
        if color[start] != 0:
            return color[start] == 1
        color[start] = 2
        for e in graph[start]:
            if not self.dfs(graph, e, color):
                return False
        color[start] = 1
        return True
```

参考资料：

https://leetcode.com/problems/find-eventual-safe-states/discuss/119871/Straightforward-Java-solution-easy-to-understand!

## 日期

2018 年 9 月 17 日 —— 早上很凉，夜里更凉


  [1]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/17/picture1.png
