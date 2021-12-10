# 【LeetCode】813. Largest Sum of Averages 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/largest-sum-of-averages/description/

## 题目描述：

We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:

    Input: 
    A = [9,1,2,3,9]
    K = 3
    Output: 20
    Explanation: 
    The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
    We could have also partitioned A into [9, 1], [2], [3, 9], for example.
    That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
 

Note:

1. 1 <= A.length <= 100.
1. 1 <= A[i] <= 10000.
1. 1 <= K <= A.length.
1. Answers within 10^-6 of the correct answer will be accepted as correct.



## 题目大意

把一个数组分成K个区间，使得各个平均数的和最大化。

## 解题方法

典型的dp求解的题目。不过dfs方式去做速度还挺快。看到A的大小是100，那么时间复杂度应该在O(n^3)。

我们定义一个函数LSA，这个函数的含义是，把A这个数组的前n个元素分成k个组得到的最大平均数和。使用m_二维数组完成记忆化，使得搜索速度变快。用sum_保存前i项数组的和，使得可以快速求平均数。

所以递归的方式：

把A这个数组的前i个元素分成k个组得到的最大平均数和 = max(把A这个数组的前j个元素分成k-1个组得到的最大平均数和 + 数组A从j+1到i个元素的平均值）。

如果读不懂上面这句话，可以直观的理解成k个组的最大平均数和 是怎么组成的？它是由前k-1个组与后面一个组放在一起组成，所以求怎么划分的情况下，前部分和后部分的求平均数的和最大。

代码如下：

```python
class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        n = len(A)
        m_ = [[0 for i in range(n + 1)] for j in range(K + 1)]
        sum_ = [0] * (n + 1)
        for i in range(1, n + 1):
            sum_[i] = sum_[i - 1] + A[i - 1]
        return self.LSA(A, sum_, m_, n, K)

    # Largest sum of averages for first n elements in A partioned into K groups
    def LSA(self, A, sum_, m_, n, k):
        if m_[k][n] > 0: return m_[k][n]
        if k == 1: return sum_[n] / n
        for i in range(k - 1, n):
            m_[k][n] = max(m_[k][n], self.LSA(A, sum_, m_, i, k - 1) + (sum_[n] - sum_[i]) / (n - i))
        return m_[k][n]
```

还可以用dp求解，待续。


参考资料：

https://www.youtube.com/watch?v=IPdShoUE9z8

## 日期

2018 年 9 月 14 日 ———— 脚踏实地，不要迷茫了