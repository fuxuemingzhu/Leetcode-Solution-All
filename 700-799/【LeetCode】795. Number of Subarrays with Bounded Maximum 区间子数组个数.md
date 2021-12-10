
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/

## 题目描述

We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

Example :

    Input: 
    A = [2, 1, 4, 3]
    L = 2
    R = 3
    Output: 3
    Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Note:

- L, R  and A[i] will be an integer in the range [0, 10^9].
- The length of A will be in the range of [1, 50000].


## 题目大意

给定了一个数组和L,R两个数字。现在我们要求在这个数组中能有多少个连续的子数组，使得这个子数组的最大值在L和R之间。

## 解题方法

### 动态规划

第一感觉是dfs，但是看了下A的长度范围发现基本只能用O(n)的算法了，因此只能使用dp去求了。

我们设定dp数组，其dp[i]的含义是以A[i]为结尾的子数组中满足题目要求的数组个数。所以我们在这个定义的基础上，能得到下面的关系式：

1. A[i] < L
这个情况，以A[i]为结尾的子数组的最大值没有改变，因此dp[i] = dp[i - 1]
2. A[i] > R
此时，以A[i]为结尾的子数组的最大值已经大于了R，所以dp[i] = 0.把这个位置设定为新的开始，记录该位置为prev.
3. L <= A[i] <= R
从prev到i之间的任意起始位置到i的子数组都满足题目条件，因此dp[i] = i - prev.

根据上面的关系式可以写出代码，最后的结果是整个dp之和。

该代码的时间复杂度是O(n)，空间复杂度也是O(n)。

代码如下：

```python
class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        if not A: return 0
        dp = [0] * len(A)
        prev = -1
        for i, a in enumerate(A):
            if a < L and i > 0:
                dp[i] = dp[i - 1]
            elif a > R:
                dp[i] = 0
                prev = i
            elif L <= a <= R:
                dp[i] = i - prev
        return sum(dp)
```

因为dp[i]只和dp[i-1]有关，所以可以把空间复杂度将为O(1)。

```python
class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        dp = 0
        res = 0
        prev = -1
        for i, a in enumerate(A):
            if a < L and i > 0:
                res += dp
            elif a > R:
                dp = 0
                prev = i
            elif L <= a <= R:
                dp = i - prev
                res += dp
        return res
```

### 暴力搜索+剪枝

如果二重循环可以求出每个数组，但是肯定会超时。不过，如果我们考虑一下剪枝，外层循环里面当前值大于R的时候，就移到下一个位置；内层循环里面，如果当前值大于R，那么后面的全部都不满足，所以直接break掉。这样就能过了！！

```cpp
class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& A, int L, int R) {
        const int N = A.size();
        int res = 0;
        for (int i = 0; i < N; ++i) {
            if (A[i] > R) continue;
            int curMax = INT_MIN;
            for (int j = i; j < N; ++j) {
                curMax = max(curMax, A[j]);
                if (curMax > R) break;
                if (curMax >= L) ++res;
            }
        }
        return res;
    }
};
```

### 线性遍历

定一个函数count()：数组中最大值小于等于bound的子数组个数。所以，我们的最终结果是就是count(R) - count(L-1)。

count函数很好设计，因为只需要线性遍历一次，就知道了。每次遍历的时候，如果当前的值小于等于bound，那么就等于在前面的子数组上又加上了一个新的数组。所以我们需要一个变量来保存前面的数组有多少个了。

```cpp
class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& A, int L, int R) {
        return count(A, R) - count(A, L - 1);
    }
    int count(vector<int>& A, int bound) {
        int res = 0, cur = 0;
        for (int x : A) {
            cur = (x <= bound) ? cur + 1 : 0;
            res += cur;
        }
        return res;
    }
};
```


我最初的想法其实就是双指针，类似虫取法。虽然想法简单，但是如果思路不够清除，根本写不出来。下面就是这个虫取法求子数组的方法。

```cpp
class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& A, int L, int R) {
        const int N = A.size();
        int res = 0;
        int left = -1, right = -1;
        for (int i = 0; i < N; ++i) {
            if (A[i] > R) left = i;
            if (A[i] >= L) right = i;
            res += right - left;
        }
        return res;
    }
};
```

参考资料：
http://www.cnblogs.com/grandyang/p/9237967.html

## 日期

2018 年 9 月 14 日 —— 现在需要的还是夯实基础，算法和理论
2018 年 12 月 16 日 —— 周赛好难
