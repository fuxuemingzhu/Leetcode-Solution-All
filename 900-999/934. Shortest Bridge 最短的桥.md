作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/shortest-bridge/description/


## 题目描述

In a given 2D binary array ``A``, there are two islands.  (An island is a 4-directionally connected group of ``1``s not connected to any other ``1``s.)

Now, we may change ``0``s to ``1``s so as to connect the two islands together to form ``1`` island.

Return the smallest number of ``0``s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

    Input: [[0,1],[1,0]]
    Output: 1

Example 2:

    Input: [[0,1,0],[0,0,0],[0,0,1]]
    Output: 2

Example 3:

    Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    Output: 1
 

Note:

1. ``1 <= A.length = A[0].length <= 100``
1. ``A[i][j] == 0 or A[i][j] == 1``


## 题目大意

题目给出一个二维矩阵，其中的0表示水，1表示陆地，四联通的陆地会连成一片岛。题目保证给出了两个岛，求两个岛之间的最短路径。

## 解题方法

### DFS + BFS

本周周赛第三题，比赛的时候没时间写了，但是赛后感觉这个题很简单。

首先用DFS来确定其中一个岛，把这个岛所有的1变成了2，这么做的目的是和另一个岛作为区分。需要注意的是把找到的这个岛的每个位置都添加到队列里面，我们会用这个队列去做BFS.

找出了岛之后，使用BFS，来找出这个岛离1最近的距离是多少。每次循环是相当于走了一步，把所有走了一步仍然是水路的位置设置成2，并放到队列里；如果找到了1，就可以直接结束了，因为我们的BFS没走一步会向前走一些，第一次寻找到的就是最近的距离；如果找到的是2，那说明这个位置已经遍历过了，直接不要管了。

最坏时间复杂度是O(MN)，最坏空间复杂度O(MN). 时间是240 ms。

```python
class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        M, N = len(A), len(A[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[0] * N for _ in range(M)]
        hasfind = False
        que = collections.deque()
        for i in range(M):
            if hasfind: break
            for j in range(N):
                if A[i][j] == 1:
                    self.dfs(A, i, j, visited, que)
                    hasfind = True
                    break
        step = 0
        while que:
            size = len(que)
            for _ in range(size):
                i, j = que.popleft()
                for d in dirs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < M and 0 <= y < N:
                        visited[x][y] = 1
                        if A[x][y] == 1:
                            return step
                        elif A[x][y] == 0:
                            A[x][y] = 2
                            que.append((x, y))
                        else:
                            continue
            step += 1
        return -1

    def dfs(self, A, i, j, visited, que):
        if visited[i][j]: return
        visited[i][j] = 1
        M, N = len(A), len(A[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if A[i][j] == 1:
            que.append((i, j))
            A[i][j] = 2
            for d in dirs:
                x, y = i + d[0], j + d[1]
                if 0 <= x < M and 0 <= y < N:
                    self.dfs(A, x, y, visited, que)
```


## 相似题目


## 参考资料


## 日期

2018 年 11 月 4 日 —— 下雨的周日


  [1]: https://assets.leetcode.com/uploads/2018/10/12/knight.png
  [2]: https://assets.leetcode.com/uploads/2018/10/30/keypad.png
  [3]: https://assets.leetcode.com/uploads/2018/10/30/keypad.png
  [4]: https://assets.leetcode.com/uploads/2018/10/30/keypad.png
  [5]: https://assets.leetcode.com/uploads/2018/10/12/knight.png
  [6]: https://assets.leetcode.com/uploads/2018/10/12/knight.png
  [7]: https://assets.leetcode.com/uploads/2018/10/12/knight.png
  [8]: https://assets.leetcode.com/uploads/2018/10/30/keypad.png
  [9]: https://assets.leetcode.com/uploads/2018/10/30/keypad.png
  [10]: https://assets.leetcode.com/uploads/2018/10/12/knight.png
  [11]: https://assets.leetcode.com/uploads/2018/10/12/knight.png
  [12]: https://blog.csdn.net/fuxuemingzhu/article/details/82747623
