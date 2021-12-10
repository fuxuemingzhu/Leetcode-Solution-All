
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/out-of-boundary-paths/description/


## 题目描述

There is an ``m`` by ``n`` grid with a ball. Given the start coordinate ``(i,j)`` of the ball, you can move the ball to ``adjacent`` cell or cross the grid boundary in four directions (up, down, left, right). However, you can ``at most`` move ``N`` times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod ``10^9 + 7``.

 

Example 1:

    Input: m = 2, n = 2, N = 2, i = 0, j = 0
    Output: 6
    Explanation:

![此处输入图片的描述][1]

Example 2:

    Input: m = 1, n = 3, N = 3, i = 0, j = 1
    Output: 12
    Explanation:

 ![此处输入图片的描述][2]

Note:

1. Once you move the ball out of boundary, you cannot move it back.
1. The length and height of the grid is in range [1,50].
1. N is in range [0,50].



## 题目大意

每次可以把足球从一个格子移动到另一个格子，要求最多通过N步能使得球移动到外边的方案数？


## 解题方法

### 动态规划

这个题有个很明显的对于动态规划的提示，那就是要模10^9 + 7，也就是说结果会很大，普通的搜索可能hold不住。

使用三维数组dp[k][x][y]表示在不超过k步的情况下，从x,y点移动到外边需要的步数。那么，当前位置通过k步移动到外边的步数等于其周围4个位置走k - 1步移动到外边的步数和。

因为当x,y处于边界的时候，实际上只有两个或者三个相邻的位置，因为向边界方向走的话，只需要1步就可以移动到外部。所以，如果向当前位置的周围位置出界的话，那么从这个方向需要出去移动步数就是1.

最后求和取模。

时间复杂度是O(N*m*n)，空间复杂度是O(N*m*n).

```python
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[[0] * n for _ in range(m)] for _ in range(N + 1)]
        for s in range(1, N + 1):
            for x in range(m):
                for y in range(n):
                    v1 = 1 if x == 0 else dp[s - 1][x - 1][y]
                    v2 = 1 if x == m - 1 else dp[s - 1][x + 1][y]
                    v3 = 1 if y == 0 else dp[s - 1][x][y - 1]
                    v4 = 1 if y == n - 1 else dp[s - 1][x][y + 1]
                    dp[s][x][y] = (v1 + v2 + v3 + v4) % (10**9 + 7)
        return dp[N][i][j]
```

上面这个做法可以看出每个状态其实只和上一次的状态有关，因此可以做状态压缩节省空间。

只使用二维数组表示地图即可，需要注意的是每次循环的时候还是需要重新开一个全部为0的curStatus，为什么全部是0而不是dp的拷贝呢？因为我们每次对下一次的状态进行搜索之前，下个状态应该全部是未知的，我们下面的代码就是计算每个位置的值，因此不能初始化dp的拷贝，否则下面的代码不work。其实这个和上面的做法对比一下就知道了，因为上面的做法中，每一步开始的时候，里面的二维数组其实全部都是0.

每次搜索结束之后，需要更新dp，也就是我们把当前的状态作为下次搜索的初始状态。

时间复杂度是O(N*m*n)，空间复杂度是O(m*n).

```python
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[0] * n for _ in range(m)]
        for s in range(1, N + 1):
            curStatus = [[0] * n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    v1 = 1 if x == 0 else dp[x - 1][y]
                    v2 = 1 if x == m - 1 else dp[x + 1][y]
                    v3 = 1 if y == 0 else dp[x][y - 1]
                    v4 = 1 if y == n - 1 else dp[x][y + 1]
                    curStatus[x][y] = (v1 + v2 + v3 + v4) % (10**9 + 7)
            dp = curStatus
        return dp[i][j]
```


### 状态搜索

这个dp其实属于对状态的搜索，如果看了《计算机考研机试指南》或者《挑战程序设计竞赛》的话，会很清楚的知道其实这是个搜索的题目。归根到底都是对状态的转移问题，所以这个方法的名称叫做动归还是搜索都可以。

这种的做法有点类似于BFS搜索的题目，我们在做BFS的时候也会记录当前处于哪一步，所以是非常类似的。我们定义了四个搜索的方向，从当前位置向周围4个方向进行搜索，如果搜索到了边界以外，和上面的做法类似的，我们把当前的步数+1；如果在边界以内，那么就把当前第s步的结果增加第s-1步的(nx, ny)位置能到达边界的解法步数。

时间复杂度是O(N*m*n)，空间复杂度是O(N*m*n).

```python
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[[0] * n for _ in range(m)] for _ in range(N + 1)]
        ds = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for s in range(1, N + 1):
            for x in range(m):
                for y in range(n):
                    for d in ds:
                        nx, ny = x + d[0], y + d[1]
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            dp[s][x][y] += 1
                        else:
                            dp[s][x][y] = (dp[s][x][y] + dp[s - 1][nx][ny]) % (10**9 + 7)
        return dp[N][i][j]
```

同样的可以优化空间。

时间复杂度是O(N*m*n)，空间复杂度是O(m*n).

```python
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[0] * n for _ in range(m)]
        ds = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for s in range(1, N + 1):
            curStatus = [[0] * n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    for d in ds:
                        nx, ny = x + d[0], y + d[1]
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            curStatus[x][y] += 1
                        else:
                            curStatus[x][y] = (curStatus[x][y] + dp[nx][ny]) % (10**9 + 7)
            dp = curStatus
        return dp[i][j]
```

### 记忆化搜索

其实，应该是先有了记忆化搜索的代码才能推出dp。这个题我用记忆化搜索重新实现了一下，但是发现果然过不了啊！但是记忆化搜索确实能加深我们对这个题目的理解。

把上面的状态搜索的dp改成记忆化搜索后的代码如下。如何加深理解呢？看看dfs的参数，变量其实只有x,y两个。dfs函数代表了我们从(x, y)位置出发，最多移动N次的情况下能到达边界的个数。所以，我们的(x, y)的初始化值是题目要求的(i, j).

最后TLE了，很无奈，因为C++版本的能够通过。

时间复杂度是O(N*m*n)，空间复杂度是O(N*m*n).

```python
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[[0] * n for _ in range(m)] for _ in range(N + 1)]
        return self.dfs(m, n, N, i, j, dp)
    
    def dfs(self, m, n, N, x, y, dp):
        if N == 0:
            return 0
        if x < 0 or x >= m or y < 0 or y >= n:
            return 1
        if dp[N][x][y]:
            return dp[N][x][y]
        ds = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for d in ds:
            nx, ny = x + d[0], y + d[1]
            dp[N][x][y] = (dp[N][x][y] + self.dfs(m, n, N - 1, nx, ny, dp)) % (10**9 + 7)
        return dp[N][x][y]
```


## 相似题目

[688. Knight Probability in Chessboard][3]
[62. Unique Paths][4]
[63. Unique Paths II][5]
[913. Cat and Mouse][6]

## 参考资料

http://www.cnblogs.com/grandyang/p/6927921.html
https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-576-out-of-boundary-paths/


## 日期

2018 年 10 月 27 日 —— 10月份最后一个周末


  [1]: https://assets.leetcode.com/uploads/2018/10/13/out_of_boundary_paths_1.png
  [2]: https://assets.leetcode.com/uploads/2018/10/12/out_of_boundary_paths_2.png
  [3]: https://blog.csdn.net/fuxuemingzhu/article/details/82747623
  [4]: https://blog.csdn.net/fuxuemingzhu/article/details/79337352
  [5]: https://blog.csdn.net/fuxuemingzhu/article/details/83154114
  [6]: https://blog.csdn.net/fuxuemingzhu/article/details/83350880
