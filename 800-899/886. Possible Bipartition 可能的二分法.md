# 【LeetCode】886. Possible Bipartition 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/possible-bipartition/description/

## 题目描述：

Given a set of ``N`` people (numbered ``1, 2, ..., N``), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if ``dislikes[i] = [a, b]``, it means it is not allowed to put the people numbered ``a`` and ``b`` into the same group.

Return ``true`` if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

    Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
    Output: true
    Explanation: group1 [1,4], group2 [2,3]

Example 2:

    Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
    Output: false

Example 3:

    Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    Output: false
 

Note:

1. 1 <= N <= 2000
1. 0 <= dislikes.length <= 10000
1. 1 <= dislikes[i][j] <= N
1. dislikes[i][0] < dislikes[i][1]
1. There does not exist i != j for which dislikes[i] == dislikes[j].

## 题目大意

一群人中有些人不喜欢对方因此不能放到同一个组里，问所有的人能否划分成两个组。

## 解题方法

这个题还是要抽象出来，抽象出一个二分图的模型。即不喜欢对方的两个人属于二分图中不同的部分。所以，这个题和[785. Is Graph Bipartite?][1]一模一样的。

同样使用dfs去做，需要把每个节点都当做起始节点去染色，这样判断是否有冲突。染色的方式是0-未染色，1-染了红色，-1代表染了蓝色。

时间复杂度是O(V + E)，空间复杂度是O(V + E).

代码如下：

```python
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for dislike in dislikes:
            graph[dislike[0] - 1].append(dislike[1] - 1)
            graph[dislike[1] - 1].append(dislike[0] - 1)
        color = [0] * N
        for i in range(N):
            if color[i] != 0: continue
            bfs = collections.deque()
            bfs.append(i)
            color[i] = 1
            while bfs:
                cur = bfs.popleft()
                for e in graph[cur]:
                    if color[e] != 0:
                        if color[cur] == color[e]:
                            return False
                    else:
                        color[e] = -color[cur]
                        bfs.append(e)
        return True
```

参考资料：

https://www.youtube.com/watch?v=VlZiMD7Iby4

## 日期

2018 年 9 月 24 日 —— 祝大家中秋节快乐


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82788401
