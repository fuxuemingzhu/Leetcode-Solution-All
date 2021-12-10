作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

## 题目描述：

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

    Input: nums = 
    [
      [9,9,4],
      [6,6,8],
      [2,1,1]
    ] 
    Output: 4 
    Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

    Input: nums = 
    [
      [3,4,5],
      [3,2,6],
      [2,2,1]
    ] 
    Output: 4 
    Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.


## 题目大意

求二维矩阵中最长的递增路径。

## 解题方法

和[417. Pacific Atlantic Water Flow][1]非常类似，直接DFS求解。一般来说DFS需要有固定的起点，但是对于这个题，二维矩阵中的每个位置都算作起点。

把每个位置都当做起点，然后去做个dfs，看最长路径是多少。然后再找出全局的最长路径。使用cache保存已经访问过的位置，这样能节省了很多搜索的过程，然后有个continue是为了剪枝。因为这个做法比较暴力，就没有什么好讲的了。

最坏情况下的时间复杂度是O((MN)^2)，空间复杂度是O(MN)。

```python
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        cache = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                path = self.dfs(matrix, cache, m, n, i, j)
                res = max(res, path)
        return res
        
    def dfs(self, matrix, cache, m, n, i, j):
        if cache[i][j] != -1:
            return cache[i][j]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        res = 1
        for dire in directions:
            x, y = i + dire[0], j + dire[1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                continue
            path = 1 + self.dfs(matrix, cache, m, n, x, y)
            res = max(path, res)
        cache[i][j] = res
        return cache[i][j]
```


参考资料：

https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/90739/Python-DFS-bests-85.-Tips-for-all-DFS-in-matrix-question./181815

## 日期

2018 年 10 月 1 日 —— 欢度国庆！


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82917037
