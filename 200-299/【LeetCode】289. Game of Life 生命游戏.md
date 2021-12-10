作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/game-of-life/description/

## 题目描述

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with `m` by `n` cells, each cell has an initial state `live` (1) or `dead` (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population..
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

    Input: 
    [
      [0,1,0],
      [0,0,1],
      [1,1,1],
      [0,0,0]
    ]
    Output: 
    [
      [0,0,0],
      [1,0,1],
      [0,1,1],
      [0,1,0]
    ]

Follow up:

1. Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
1. In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?


## 题目大意


玩一个生存游戏。这个游戏给了一个二维数组，每个数组上写的是这个地方是否有部落。看每个位置的 8 连通位置的部落数：

1. 如果一个活着的部落，其周围少于2个部落，这个部落会死；
2. 如果一个活着的部落，其周围部落数在2或者3，这个部落活到下一个迭代中；
3. 如果一个活着的部落，其周围多于3个部落，这个部落会死；
4. 如果一个死了的部落，其周围多于3个部落，这个部落会活。

**一次迭代是同时进行的**，求一轮之后，整个数组。

解释下 4 联通和 8 联通：

![image.png](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9waWMubGVldGNvZGUtY24uY29tL2Y1MzgwOWZjYjdjYWUzODFhZTlkYTJmYzhiNzk3YTM0MTVmMWM0NWMyN2I0ZjhkNTdiNjQwMzcwYjZlOWI5OGQtaW1hZ2UucG5n?x-oss-process=image/format,png)


## 解题方法


方法很简单暴力，直接统计每个位置的 8 连通分量并根据部落数进行题目所说的判断就好了。

由于一次迭代是同时进行的，所以不能一边统计一边修改数组，这样会影响后面的判断。我的做法是先把输入的面板复制了一份，这样使用原始的 `board` 去判断部落数，更新放在了新的 `board_next` 上不会影响之前的 `board`。最后再把数值复制过来。

题目给了 4 个存活和死亡的判断条件，直接按照这4个条件判断即可。我定义了一个函数`liveOrDead()`用来判断当前判断的部落应该活还是死，返回结果的解释：0-不变, 1-活下来,2-要死了。

时间复杂度是O(MN)，空间复杂度是O(MN).

Python代码如下：

```python
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board and board[0]:
            M, N = len(board), len(board[0])
            board_next = copy.deepcopy(board)
            for m in range(M):
                for n in range(N):
                    lod = self.liveOrDead(board, m, n)
                    if lod == 2:
                        board_next[m][n] = 0
                    elif lod == 1:
                        board_next[m][n] = 1
            for m in range(M):
                for n in range(N):
                    board[m][n] = board_next[m][n]
            
    def liveOrDead(self, board, i, j):# return 0-nothing,1-live,2-dead
        ds = [(1, 1), (1, -1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1)]
        live_count = 0
        M, N = len(board), len(board[0])
        for d in ds:
            r, c = i + d[0], j + d[1]
            if 0 <= r < M and 0 <= c < N:
                if board[r][c] == 1:
                    live_count += 1
        if live_count < 2 or live_count > 3:
            return 2
        elif board[i][j] == 1 or (live_count == 3 and board[i][j] ==0):
            return 1
        else:
            return 0
```

参考资料：

https://leetcode.com/problems/game-of-life/discuss/73223/Easiest-JAVA-solution-with-explanation/178496

## 日期

2018 年 9 月 22 日 —— 周末加班
