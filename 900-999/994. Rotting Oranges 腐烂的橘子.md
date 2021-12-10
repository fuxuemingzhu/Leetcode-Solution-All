
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/rotting-oranges/


## 题目描述

n a given grid, each cell can have one of three values:

- the value 0 representing an empty cell;
- the value 1 representing a fresh orange;
- the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return ``-1`` instead.

Example 1:

![此处输入图片的描述][1]

    Input: [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

Example 2:

    Input: [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

    Input: [[0,2]]
    Output: 0
    Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
     

Note:

1. ``1 <= grid.length <= 10``
1. ``1 <= grid[0].length <= 10``
1. ``grid[i][j]`` is only 0, 1, or 2.

## 题目大意

在给定的二维格子里，每个格子有三个状态：0代表空，1代表新鲜的橘子，2代表腐败的橘子。

每一分钟，如果一个新鲜的橘子的四联通格子里有腐败的格子，那么这个格子的新鲜橘子就会变成腐败的。

问所有的橘子都腐败的时候，需要多久？

当不可能都腐败的时候，返回-1.

## 解题方法

### BFS

其实这个题很简单的，就是类似的四联通地走迷宫。因为每一步都是四联通的向前走，所以我们使用BFS来解决。

首先统计新鲜橘子的个数，把腐败橘子的位置保存到队列中。

然后遍历队列，每一步中，把队列中已经有的所有腐败橘子都弹出来，判断它的四周有没有新鲜橘子，然后把新鲜橘子变成腐败的，并把该位置放到队列中，同时还要把新鲜橘子的个数-1.

当我们走到某一个时间之后，发现队列中没有腐败的橘子了。这个时候意味着在上一步中，没有新鲜橘子被传染成腐败的，即无路可走了。这个时候，我们停止。

停止之后，需要根据新鲜橘子的个数是不是已经全部被染成了腐败的来判断是不是返回-1.如果全部被染了，需要返回的是step - 1，为什么不是step呢？因为我们在对队列的第一次循环过程中，遍历了题目给出的腐败橘子，这个也统计到了step中，所以比要经历的时间多了1次，因此减去。

python代码如下：

```python
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        fresh = 0
        q = collections.deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        if fresh == 0:
            return 0
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        step = 0
        while q:
            size = len(q)
            for i in range(size):
                x, y = q.popleft()
                for d in dirs:
                    nx, ny = x + d[0], y + d[1]
                    if nx < 0 or nx >= M or ny < 0 or ny >= N or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    q.append((nx, ny))
                    fresh -= 1
            step += 1
        if fresh != 0:
            return -1
        return step - 1
```

## 日期

2019 年 2 月 21 日 —— 一放假就再难抓紧了


  [1]: https://assets.leetcode.com/uploads/2019/02/16/oranges.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/87829987
