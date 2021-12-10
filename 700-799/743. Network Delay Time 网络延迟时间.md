# 【LeetCode】743. Network Delay Time 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/network-delay-time/description/

## 题目描述：

There are ``N`` network nodes, labelled ``1`` to ``N``.

Given times, a list of travel times as directed edges ``times[i] = (u, v, w)``, where ``u`` is the source node, ``v`` is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node ``K``. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Note:

1. ``N`` will be in the range ``[1, 100]``.
1. K will be in the range ``[1, N]``.
1. The length of times will be in the range ``[1, 6000]``.
1. All edges ``times[i] = (u, v, w)`` will have ``1 <= u, v <= N`` and ``1 <= w <= 100``.


## 题目大意

求单源有向图的最长路径。如果有节点不可抵达，返回-1.

## 解题方法

Dijkstra算法，纯模板题。

时间复杂度是O(N ^ 2 + E)，空间复杂度是O(N+E).

代码如下：

```python
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        K -= 1
        nodes = collections.defaultdict(list)
        for u, v, w in times:
            nodes[u - 1].append((v - 1, w))
        dist = [float('inf')] * N
        dist[K] = 0
        done = set()
        for _ in range(N):
            smallest = min((d, i) for (i, d) in enumerate(dist) if i not in done)[1]
            for v, w in nodes[smallest]:
                if v not in done and dist[smallest] + w < dist[v]:
                    dist[v] = dist[smallest] + w
            done.add(smallest)
        return -1 if float('inf') in dist else max(dist)
```

Floyd-Warshall算法。这个算法TLE.

时间复杂度O(n^3)， 空间复杂度O(n^2)。

```python
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        d = [[float('inf')] * N for _ in range(N)]
        for time in times:
            u, v, w = time[0] - 1, time[1] - 1, time[2]
            d[u][v] = w
        for i in range(N):
            d[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return -1 if float('inf') in d[K - 1] else max(d[K - 1])
```

Bellman-Ford算法，这个算法TLE。

时间复杂度O(ne)， 空间复杂度O(n)。


```python
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        dist = [float('inf')] * N
        dist[K - 1] = 0
        for i in range(N):
            for time in times:
                u = time[0] - 1
                v = time[1] - 1
                w = time[2]
                dist[v] = min(dist[v], dist[u] + w)
        return -1 if float('inf') in dist else max(dist)
```

参考资料：

https://zxi.mytechroad.com/blog/graph/leetcode-743-network-delay-time/
https://leetcode.com/problems/network-delay-time/discuss/172857/Python-Dijkstra-Solution-that-beats-86

## 日期

2018 年 9 月 27 日 ———— 今天起得格外早
