
作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/smallest-range-i/description/

## 题目描述

Given an array A of integers, for each integer A[i] we may choose any x with ``-K <= x <= K``, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.
 
Example 1:

    Input: A = [1], K = 0
    Output: 0
    Explanation: B = [1]

Example 2:

    Input: A = [0,10], K = 2
    Output: 6
    Explanation: B = [2,8]

Example 3:

    Input: A = [1,3,6], K = 3
    Output: 0
    Explanation: B = [3,3,3] or B = [4,4,4]
 

Note:

1. 1 <= A.length <= 10000
1. 0 <= A[i] <= 10000
1. 0 <= K <= 10000

## 题目大意

A中的每个数值都可以加上另外一个数字x (-K <= x <= K). 这样对A中所有的数字进行了上述操作之后，求得到的新的数组B的最大值和最小值之差。

## 解题方法

### 数学计算

要求的是新的数组最大值和最小值之差，所以，我们应该把所有的数字向中间靠拢。即A中的最小值+K, 最大值-K，判断这样操作之后，能否有重叠，如果能重叠所求的结果就是0；如果不能重叠，所求的结果就是两者的差值。

时间复杂度是O(N)，空间复杂度是O(1).

代码如下：

```python
class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(max(A) - min(A) - 2 * K, 0)
```

参考资料：

## 日期

2018 年 9 月 23 日 —— 今天是实验室第一个打卡的
2018 年 11 月 5 日 —— 打了羽毛球，有点累

  [1]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
