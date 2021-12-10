# 【LeetCode】764. Largest Plus Sign 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/largest-plus-sign/description/

## 题目描述：

In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

    Order 1:
    000
    010
    000
    
    Order 2:
    00000
    00100
    01110
    00100
    00000
    
    Order 3:
    0000000
    0001000
    0001000
    0111110
    0001000
    0001000
    0000000

Example 1:

    Input: N = 5, mines = [[4, 2]]
    Output: 2
    Explanation:
    11111
    11111
    11111
    11111
    11011
    In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.

Example 2:

    Input: N = 2, mines = []
    Output: 1
    Explanation:
    There is no plus sign of order 2, but there is of order 1.

Example 3:

    Input: N = 1, mines = [[0, 0]]
    Output: 0
    Explanation:
    There is no plus sign, so return 0.

Note:

1. N will be an integer in the range [1, 500].
1. mines will have length at most 5000.
1. mines[i] will be length 2 and consist of integers in the range [0, N-1].
1. (Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)

## 题目大意

题目要求我们找出在一个边长为N的正方形中能画出的最大的正“+”加号的边长，加号的边长就是除了从中间点到一条边的尽头的1的个数。为了加大难度，题目给出了一些值为0的坐标点，这些点上是不允许放正方形的边的。

## 解题方法

如果是暴力解法的话，我们很容易就写出O(n^3)的解法，就是对于每个位置，都向上下左右四个方向去寻找能拓展多远。（注意，因为方向是定死的，且四个方向长度是一致的，所以不是O(n^4)）。这样肯定会超时的。

一个比较容易理解的方法就是，我们先确定一个dp数组，这个数组dp[i][j]保存的是到从i,j位置向上下左右四个方向能拓展的长度。最后每个位置能拓展多远就是上下左右四个方向能拓展长度的最小值。我选择遍历的方向是左右上下，那么到下的遍历的时候，dp数组保存的就就是最小的边长了。

这个题四个方向是对称的，因此只需要知道一个方向怎么写，那么直接改循环方向就行，根本不用思考我查找的方向到底是四个方向中的哪一个。同时使用了set把二维坐标改成了一维，可以加快查找。

时间复杂度是O(n^2)，空间复杂度是O(n^2).

代码如下：

```python3
class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        res = 0
        dp = [[0 for i in range(N)] for j in range(N)]
        s = set()
        for mine in mines:
            s.add(N * mine[0] + mine[1])
        for i in range(N):
            cnt = 0
            for j in range(N):#left
                cnt = 0 if N * i + j in s else cnt + 1
                dp[i][j] = cnt
            cnt = 0
            for j in range(N - 1, -1, -1):#right
                cnt = 0 if N * i + j in s else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
        for j in range(N):
            cnt = 0
            for i in range(N):#up
                cnt = 0 if N * i + j in s else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
            cnt = 0
            for i in range(N - 1, -1, -1):#down
                cnt = 0 if N * i + j in s else cnt + 1
                dp[i][j] = min(dp[i][j], cnt)
                res = max(dp[i][j], res)
        return res
```

如果用四个变量代表上下左右方向的话可以缩短一下代码：

```python3
class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        res = 0
        dp = [[N for i in range(N)] for j in range(N)]
        s = set()
        for mine in mines:
            dp[mine[0]][mine[1]] = 0
        for i in range(N):
            l, r, u, d = 0, 0, 0, 0
            for j in range(N):
                l = l + 1 if dp[i][j] else 0
                r = r + 1 if dp[j][i] else 0
                u = u + 1 if dp[i][N - 1 -j] else 0
                d = d + 1 if dp[N - 1 - j][i] else 0
                dp[i][j] = min(dp[i][j], l)
                dp[j][i] = min(dp[j][i], r)
                dp[i][N - 1 - j] = min(dp[i][N -  1 - j], u)
                dp[N - 1 - j][i] = min(dp[N - 1 - j][i], d)
        for i in range(N):
            for j in range(N):
                res = max(res, dp[i][j])
        return res
```

参考资料：

http://www.cnblogs.com/grandyang/p/8679286.html

## 日期

2018 年 9 月 16 日 ———— 天朗气清，惠风和畅