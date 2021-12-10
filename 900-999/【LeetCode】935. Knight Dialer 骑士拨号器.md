作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/knight-dialer/description/


## 题目描述

A chess knight can move as indicated in the chess diagram below:

![此处输入图片的描述][1]       .          ![此处输入图片的描述][2]

This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes ``N-1`` hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing ``N`` digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer **modulo 10^9 + 7**.

 

Example 1:

    Input: 1
    Output: 10

Example 2:

    Input: 2
    Output: 20

Example 3:

    Input: 3
    Output: 46
 

Note:

1. 1 <= N <= 5000

## 题目大意

马的初始位置可以在拨号按键的任意位置，现在要让它走N - 1步，问这个马能产生出多少种不同的拨号号码？


## 解题方法

### 动态规划TLE

本周周赛第二题，卡了我好久啊！好气！

这个题本身肯定是动态规划题目，设置dp数组为当前步以每个按键结尾的状态数。所以我使用了一个4×3的二维数组，需要注意的是左下角和右下角的位置不可能到达，设置它的数值为0.状态转移方程很好求得，那就是把上一步可能存在的位置状态累加在一起就成了当前位置的状态数。

问题是会超时啊！甚至可能会超过内存限制！

先上一份很容易想到的，但是会超时TLE的代码：

时间复杂度是O(N)，空间复杂度O(N).

```python
class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.ans = dict()
        self.ans[0] = 10
        board = [[1] * 3 for _ in range(4)]
        board[3][0] = board[3][3] = 0
        pre_dict = {(i, j) : self.prevMove(i, j) for i in range(4) for j in range(3)}
        for n in range(1, N):
            new_board = copy.deepcopy(board)
            for i in range(4):
                for j in range(3):
                    cur_move = 0
                    for x, y in pre_dict[(i, j)]:
                        cur_move = (cur_move + board[x][y]) % (10 ** 9 + 7)
                    new_board[i][j] = cur_move
            board = new_board
        return sum([board[i][j] for i in range(4) for j in range(3)]) % (10 ** 9 + 7)
        
    def prevMove(self, i, j):
        if (i, j) == (3, 0) or (i, j) == (3, 2):
            return []
        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        res = []
        for d in directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < 4 and 0 <= y < 3 and (x, y) != (3, 0) and (x, y) != (3, 2):
                res.append((x, y))
        return res
```

在比赛的时候剩下的一个小时都在优化这个题，个人感觉这个题卡时间卡的有点太严了，上面这个做法应该是标准做法吧，通过不了，需要一些奇技淫巧才能通过。

### 空间换时间，利用对称性

这是我在比赛最后的时间通过的代码，把所有状态给初始化了，这样好处是可以不用在循环中不停地copy原来的棋盘状态了，同时利用了对称性，只需要求出4个位置（1,2,4,0）的状态，其余状态可以直接利用对称性得到。

还有一个优化的地方在于在每次的过程中进行取模！虽然取模运算是耗时的运算，但是数字很大的时候，大整数既占空间又占时间，所以取模！

经过上面的优化勉强通过了，真是不容易，我觉得这个题非常不友好，因为同样的Java代码可以不做任何优化就通过了。这个题在N很大的时候还会告诉我内存超了……简直了。。

时间复杂度是O(N)，空间复杂度O(N).总时间1500ms。


```python
class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.ans = dict()
        self.ans[0] = 10
        board = [[[1] * 3 for _ in range(4)] for _ in range(N)]
        board[0][3][0] = board[0][3][2] = 0
        pre_dict = {(i, j) : self.prevMove(i, j) for i in range(4) for j in range(3)}
        for n in range(1, N):
            for i in range(2):
                cur_move = 0
                for x, y in pre_dict[(i, 0)]:
                    cur_move += board[n - 1][x][y]
                board[n][i][0] = cur_move % (10 ** 9 + 7)
            cur_move = 0
            for x, y in pre_dict[(0, 1)]:
                cur_move += board[n - 1][x][y]
            board[n][0][1] = cur_move % (10 ** 9 + 7)
            cur_move = 0
            for x, y in pre_dict[(3, 1)]:
                cur_move += board[n - 1][x][y]
            board[n][3][1] = cur_move % (10 ** 9 + 7)
            board[n][4][0] = board[n][0][0]
            board[n][0][2] = board[n][0][0]
            board[n][5][1] = 0
            board[n][6][2] = board[n][7][0]
            board[n][8][1] = board[n][0][1]
            board[n][9][2] = board[n][0][2]
            board[n][3][0] = board[n][3][2] = 0
        return (board[N - 1][0][0] * 4 + board[N - 1][0][1] * 2 + board[N - 1][10][0] * 2 + board[N - 1][3][1] + board[N - 1][11][1]) % (10 ** 9 + 7)
        
    def prevMove(self, i, j):
        if (i, j) == (3, 0) or (i, j) == (3, 2):
            return []
        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        res = []
        for d in directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < 4 and 0 <= y < 3 and (x, y) != (3, 0) and (x, y) != (3, 2):
                res.append((x, y))
        return res
```


### 优化空间复杂度

上面的做法我一直在想着优化时间复杂度，事实上，每个状态只和之前的状态有关，所以很容易想到优化空间复杂度。

使用10个变量，分别保存每个位置能取到的状态数，然后人为的把每个状态能通过其他的状态得到的代码给写出来就行了。

代码如下，真的很简洁，为什么我没有想到优化空间！！优化之后时间降到了264 ms，这个告诉我们，优化空间同样可以大规模地降低时间，如果DP问题超时的话，优先考虑空间！

时间复杂度是O(N)，空间复杂度O(1).时间264 ms.

```python
class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1: return 10
        x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1
        MOD = 10 ** 9 + 7
        for i in range(N - 1):
            x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = (x6 + x8) % MOD,\
                (x7 + x9) % MOD, (x4 + x8) % MOD, (x3 + x9 + x0) % MOD, 0, (x1 + x7 + x0) % MOD,\
                (x2 + x6) % MOD, (x1 + x3) % MOD, (x2 + x4) % MOD, (x4 + x6) % MOD
        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % MOD
```

如果在上面的解法上再利用好对称性的话，可以把时间再次降低到160 ms。

时间复杂度是O(N)，空间复杂度O(1).时间160 ms。

```python
class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1: return 10
        x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1
        MOD = 10 ** 9 + 7
        for i in range(N - 1):
            x1, x2, x4, x0 = (x6 + x8) % MOD, (x7 + x9) % MOD, (x3 + x9 + x0) % MOD, (x4 + x6) % MOD
            x3, x5, x6, x7, x8, x9 = x1, 0, x4, x1, x2, x1
        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % MOD
```


## 相似题目

[688. Knight Probability in Chessboard][12]

## 参考资料

https://leetcode.com/problems/knight-dialer/discuss/189252/O(logN)

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
