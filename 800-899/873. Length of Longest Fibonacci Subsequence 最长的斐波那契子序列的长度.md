# 【LeetCode】873. Length of Longest Fibonacci Subsequence 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/

## 题目描述：

A sequence X_1, X_2, ..., X_n is fibonacci-like if:

- n >= 3
- X_i + X_{i+1} = X_{i+2} for all i + 2 <= n

Given a ``strictly increasing`` array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

 

Example 1:

    Input: [1,2,3,4,5,6,7,8]
    Output: 5
    Explanation:
    The longest subsequence that is fibonacci-like: [1,2,3,5,8].

Example 2:

    Input: [1,3,7,11,12,14,18]
    Output: 3
    Explanation:
    The longest subsequence that is fibonacci-like:
    [1,11,12], [3,11,14] or [7,11,18].

Note:

- 3 <= A.length <= 1000
- 1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
- (The time limit has been reduced by 50% for submissions in Java, C, and C++.)

## 题目大意

找出一个严格递增的数组中最长的费布拉奇子序列长度。注意子序列可以不连续，而子数组必须连续。

## 解题方法

使用最简单的方法竟然也能过。只需要双重循环，循环的含义是找出以这两个元素为起始点的费布拉奇数列。然后继续向后面遍历，使用set用O(1)的时间复杂度来查找下面的一个费布拉奇数字是否在set之中，然后继续再找下一个费布拉奇数字即可。

费布拉奇数字计算的时间复杂度接近于O(logM)，M代表数组A中的最大值。所以整个时间复杂度是O(n^2 * longM)。

代码如下：

```python
class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set(A)
        n = len(A)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                a, b = A[i], A[j]
                count = 2
                while a + b in s:
                    a, b = b, a + b
                    count += 1
                    res = max(res, count)
        return res if res > 2 else 0
```

方法二：

DP.

使用一维DP解决不了这个问题，因为一维DP只保存了到某个为止的最长费布拉奇数列，但是新的数字到来之后能不能满足之前的费布拉奇数列是未知的。所以使用二维DP.

这个DP[i][j]数组的含义是，以i和j为结尾两个数字的费布拉奇数列长度（i < j）。因此，转移方程可以这么写：

dp[j][k] = dp[i][j] + 1
条件是 A[i] + A[j] = A[k]。

我们求解的过程是用j,k去遍历，然后查找满足条件的i。

使用字典保存每个数字和其下标的对应值，能用O(1)的时间复杂度求出i。

题目要求的结果是整个dp的最大值。

另外，如果出现A[i] >= A[j]直接break内层循环，因为我们指定了i < j。

这个题和一般dp不同的是，普通的dp的下标转移方程是固定的，而这个题需要我们先找出之前的i坐标，然后才去更新dp值。

这个算法的时间复杂度是O(n^2)，空间复杂度是O(n^2).

```python
class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        m = dict()
        for i, a in enumerate(A):
            m[a] = i
        res = 0
        # dp[i][j] := max len of seq ends with A[i], A[j]
        dp = [[2 for i in range(n)] for j in range(n)]
        for j in range(n):
            for k in range(j + 1, n):
                a_i = A[k] - A[j]
                if a_i >= A[j]:
                    break
                if a_i in m:
                    i = m[a_i]
                    dp[j][k] = dp[i][j] + 1
                    res = max(res, dp[j][k])
        return res
```

参考资料：

https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/discuss/152343/C++JavaPython-Check-Pair
https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-873-length-of-longest-fibonacci-subsequence/

## 日期

2018 年 9 月 15 日 ———— 天气转冷，小心着凉