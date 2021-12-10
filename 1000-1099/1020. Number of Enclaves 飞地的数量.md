作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

## 题目描述


Given an array ``A`` of integers, return ``true`` if and only if we can partition the array into three **non-empty** parts with equal sums.

Formally, we can partition the array if we can find indexes ``i+1 < j`` with ``(A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])``


Example 1:

    Input: [0,2,1,-6,6,-7,9,1,2,0,1]
    Output: true
    Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:

    Input: [0,2,1,-6,6,7,9,-1,2,0,1]
    Output: false

Example 3:

    Input: [3,3,6,5,-2,2,5,1,-9,4]
    Output: true
    Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

Note:

1. 3 <= A.length <= 50000
1. -10000 <= A[i] <= 10000


## 题目大意

给定一个数组能不能分成``和相等``的连续三部分。每部分至少一个数字。

## 解题方法

这个题其实很简单，有同学没做出来的原因是把题目的连续条件给忘了、按照回溯法做这个题的话，看到数组A的长度是50000肯定会超时。

既然是连续相等的三部分，那么可以先求出数组总体的和_sum，除以3就得到了每部分的和target。易知这题的时间复杂度要求是O(N)，所以当我们进行搜索的时候，只要找到一个连续子子数组的和是target，那么就重新开始计算后面部分的和，统计有多少个连续子数组的和是target。

当我们遍历完成一遍的时候，如果count大于等于3，说明一定可以分成连续相等的三部分。

这里解释下为什么需要count >= 3，因为如果有0出现或者有多个部分的和都是0的话，那么count可以大于3。比如`[0,0,0,0,0]`的测试用例，count是5，但是也可以分为三个和相等的部分。例如`[1, -1, 1, -1, 1, -1, 0]`，count是4，也可以分为三个和相等的部分。

Python代码如下：

```python
class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        _sum = sum(A)
        if _sum % 3 != 0:
            return False
        target = _sum / 3
        count = 0
        cursum = 0
        for a in A:
            cursum += a
            if cursum == target:
                count += 1
                cursum = 0
        return count >= 3
```

参考资料：https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/discuss/260885/C%2B%2B-6-lines-O(n)-target-sum

## 日期

2019 年 3 月 24 日 —— 这个周赛太悲催了
