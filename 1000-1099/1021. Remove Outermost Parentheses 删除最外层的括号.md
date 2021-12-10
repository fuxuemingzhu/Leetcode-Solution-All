

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/best-sightseeing-pair/

## 题目描述


Given an array ``A`` of positive integers, ``A[i]`` represents the value of the ``i``-th sightseeing spot, and two sightseeing spots ``i`` and ``j`` have distance ``j - i`` between them.

The score of a pair (``i < j``) of sightseeing spots is (``A[i] + A[j] + i - j``) : the sum of the values of the sightseeing spots, **minus** the distance between them.

Return the maximum score of a pair of sightseeing spots.


Example 1:

    Input: [8,1,5,2,6]
    Output: 11
    Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
 

Note:

1. ``2 <= A.length <= 50000``
1. ``1 <= A[i] <= 1000``

## 题目大意

对于数组中的两个下标i, j，求``A[i] + A[j] + i - j``最大值.

## 解题方法
一般暴力解法是两重循环，即先找到一个位置 `i` 之后，从其后位置 `j` 继续循环遍历，这样的复杂度是`O(N ^ 2)` 的。看到题目给出的数据范围，数组的长度是 50000， 对于这个题`O(N ^ 2)` 的时间复杂度肯定不可取。

对于这个题，我们知道肯定只能用 `O(N)` 的解法，把公式稍加变化成`(A[i] + i) + (A[j] - j)`，我们可以看出要找出这两部分和的最大值。

具体方法是保存每个位置 `j` ，时刻维护其前面的`A[i] + i`的最大值出现的位置 `pre_i`。最后结果就是对于每个位置`j`对应的``A[i] + A[j] + i - j``最大值。


Python代码如下：

```python
class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        pre_i = 0
        res = 0
        for j in range(1, len(A)):
            res = max(A[j] - j + A[pre_i] + pre_i, res)
            if A[j] + j > A[pre_i] + pre_i:
                pre_i = j
        return res
```

参考资料：https://leetcode.com/problems/best-sightseeing-pair/discuss/260850/JavaC%2B%2BPython-One-Pass

## 日期

2019 年 3 月 24 日 —— 这个周赛太悲催了
