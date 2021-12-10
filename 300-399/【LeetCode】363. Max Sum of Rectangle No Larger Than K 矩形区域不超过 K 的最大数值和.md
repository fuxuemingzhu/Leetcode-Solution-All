作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/

## 题目描述：

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

    Input: matrix = [[1,0,1],[0,-2,3]], k = 2
    Output: 2 
    Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
                 and 2 is the max number no larger than k (k = 2).


Note:

1. The rectangle inside the matrix must have an area > 0.
1. What if the number of rows is much larger than the number of columns?


## 题目大意

找出一个矩阵中的子长方形，使得这个长方形的和是最大的。

## 解题方法

### 方法一：暴力求解(TLE)

求和最大的矩形，很容易让人想到先把(0, 0)到所有(i, j)位置的矩形的和求出来，然后再次遍历，求出所有子矩形中和最大的那个。

很无奈，超时了。（好像C++可以通过，python伤不起）

时间复杂度是O((MN)^2)，空间复杂度是O(MN)。

```python
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        sums = [[0] * N for _ in range(M)]
        res = float("-inf")
        for m in range(M):
            for n in range(N):
                t = matrix[m][n]
                if m > 0:
                    t += sums[m - 1][n]
                if n > 0:
                    t += sums[m][n - 1]
                if m > 0 and n > 0:
                    t -= sums[m - 1][n - 1]
                sums[m][n] = t
                for r in range(m + 1):
                    for c in range(n + 1):
                        d = sums[m][n]
                        if r > 0:
                            d -= sums[r - 1][n]
                        if c > 0:
                            d -= sums[m][c - 1]
                        if r > 0 and c > 0:
                            d += sums[r - 1][c - 1]
                        if d <= k:
                            res = max(res, d)
        return res
```

### 方法二：Kadane's algorithm (TLE)

看了[印度小哥的视频][1]，真的很好理解，告诉我们使用一个数组的情况下，如何找出整个二维子矩阵的最大值。我看了视频之后，写出了这个算法，但是很无奈，直接用这个算法仍然超时。

我分析，这个算法时间复杂度仍然没有降下来，主要问题是获取子数组的最大区间和这一步太耗时了。

时间复杂度是O((MN)^2)，空间复杂度是O(M)。

```python
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        L, R = 0, 0
        curSum, maxSum = float('-inf'), float('-inf')
        maxLeft, maxRight, maxUp, maxDown = 0, 0, 0, 0
        M, N = len(matrix), len(matrix[0])
        for L in range(N):
            curArr = [0] * M
            for R in range(L, N):
                for m in range(M):
                    curArr[m] += matrix[m][R]
                curSum = self.getSumArray(curArr, M, k)
                if curSum > maxSum:
                    maxSum = curSum
        return maxSum
            
    def getSumArray(self, arr, M, k):
        sums = [0] * (M + 1)
        for i in range(M):
            sums[i + 1] = arr[i] + sums[i]
        res = float('-inf')
        for i in range(M):
            for j in range(i + 1, M + 1):
                curSum = sums[j] - sums[i]
                if curSum <= k and curSum > res:
                    res = curSum
        return res
```

### 方法二：Kadane's algorithm + 二分查找 (Accepted)

上面的算法慢就慢在查找子数组的最大和部分。其实没必要使用求最大和的方式。因为题目要求我们找出不超过K的和，所以只需要在数组中是否存在另外一个数使得两者的差不超过K即可。这个查找的效率能达到O(NlogN).

在C++中能使用set和lowwer_bound实现，在python中使用bisect_left函数能也实现。

这个过程可以在[这个文章][2]中看到更详细的说明。

在时间复杂度中可以看到M影响更大，另外一个优化的策略是重新设置矩形的长和宽，这样也可以优化速度。

时间复杂度是O(MN*M*logM)，空间复杂度是O(M)。

```python
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        
        M = max(m, n)
        N = min(m, n)
        ans = None
        for x in range(N):
            sums = [0] * M
            for y in range(x, N):
                slist, num = [], 0
                for z in range(M):
                    sums[z] += matrix[z][y] if m > n else matrix[y][z]
                    num += sums[z]
                    if num <= k:
                        ans = max(ans, num)
                    i = bisect.bisect_left(slist, num - k)
                    if i != len(slist):
                        ans = max(ans, num - slist[i])
                    bisect.insort(slist, num)
        return ans or 0
```


参考资料：

http://bookshadow.com/weblog/2016/06/22/leetcode-max-sum-of-sub-matrix-no-larger-than-k/
http://www.cnblogs.com/grandyang/p/5617660.html
https://www.quora.com/Given-an-array-of-integers-A-and-an-integer-k-find-a-subarray-that-contains-the-largest-sum-subject-to-a-constraint-that-the-sum-is-less-than-k
https://www.youtube.com/watch?v=yCQN096CwWM&t=589s

## 日期

2018 年 10 月 11 日 —— 做Hard题真的很难


  [1]: https://www.youtube.com/watch?v=yCQN096CwWM
  [2]: https://www.quora.com/Given-an-array-of-integers-A-and-an-integer-k-find-a-subarray-that-contains-the-largest-sum-subject-to-a-constraint-that-the-sum-is-less-than-k
