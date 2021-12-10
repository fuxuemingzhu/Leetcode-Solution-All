作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/maximum-length-of-pair-chain/description/

## 题目描述

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair ``(c, d)`` can follow another pair ``(a, b)`` if and only if ``b < c``. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:

	Input: [[1,2], [2,3], [3,4]]
	Output: 2
	Explanation: The longest chain is [1,2] -> [3,4]

Note:

1. The number of given pairs will be in the range [1, 1000].

## 题目大意

给出了很多区间，找出能够成的连续增长的区间的个数。区间是闭区间，不能有任何重叠。

## 解题方法

### 贪心算法

题目给的提示是DP，我用Python的DP竟然超时了。其实我第一想法是贪心算法，在机试指南中的39页，题目是《今年暑假不AC》，原题是能收看到的最多的电视节目的数量。

这题的做法是按照每个区间的右边界进行排序，我们优先选择结束时间最早的区间，这样的贪心做法能保证最后得到的区间的数目是最多的。

![这里写图片描述](https://img-blog.csdn.net/20180405151123730?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1eHVlbWluZ3podQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

Python代码：

```python
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])
        currTime, ans = float('-inf'), 0
        for x, y in pairs:
            if currTime < x:
                currTime = y
                ans += 1
        return ans
```

## 日期

2018 年 4 月 5 日 —— 清明节假期开始，小长假真好～～


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79821305
