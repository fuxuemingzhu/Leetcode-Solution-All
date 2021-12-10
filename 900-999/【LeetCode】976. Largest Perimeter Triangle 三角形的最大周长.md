

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/largest-perimeter-triangle/


## 题目描述

Given an array ``A`` of positive lengths, return the largest perimeter of a triangle with ``non-zero area``, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return ``0``.

 

Example 1:

    Input: [2,1,2]
    Output: 5

Example 2:

    Input: [1,2,1]
    Output: 0

Example 3:

    Input: [3,2,3,4]
    Output: 10

Example 4:

    Input: [3,6,2,3]
    Output: 8
 

Note:

1. 3 <= A.length <= 10000
1. 1 <= A[i] <= 10^6

## 题目大意

从一个数组中选择3条边构成三角形，求该三角形最大的周长。

## 解题方法

### 排序

首先，我们肯定需要排序的，这个不解释。

假设排序完成之后的数组为[a, b, c, d, e, f]，其中a <= b <= c <= d <= e <= f.为了尽可能构成周长最大的三角形，我们从右向左进行遍历。只需要对连续的三条边进行判断即可找出周长最大的三角形。理由如下。

抽出三条边，假设为d,e,f，那么这三条边组成三角形的充分条件是d + e > f。下面进行证明：

对于任意三条边，能组成三角形的充分条件是两边之和大于第三边，两边之差小于第三边。由于d <= e <= f，显然有e + f > d，d + f > e。又d + e > f，则满足任意两边之和大于第三边。由于d <= e <= f，则e - d < f。又d + e > f，则f - e < d, f - d < e，则满足任意两边只差小于第三边。所以，当d + e > f时能够成三角形。

下面证明选取的次大边和最大边必须相邻，即如果最大边选择f，则次大边必须选择e。由d + e > f知， 最大边 - 次大边 < 最小边。当我们次大边选择e时，假如最小边无论如何选择不能构成三角形，即target = f - e > d。那么，次大边选择更小的数字时，target会更大，仍然有target = f - d > f - e > d > c。总之，如果当次大边选择和最大边相邻时，如果不能构成三角形，则次大边和最大边不相邻，更不能构成三角形。

再下面证明，最小边必须和次大边必须相邻，即如果最大边选择f、次大边选择e时，最小边必须选择d。这个很好证明，由于d + e > f，即target = f - e < 最小边，我们肯定只能在满足该条件的边中选择最大的，才能使得构成三角形的周长最大。而数组是已经排了序的，所以，最小边选择d时，要么不能构成三角形，要么就构成在最大边和次大边为f,e时周长最大的三角形。

综上，在排序了的数组中选择三条边构成最大周长的三角形的充分条件是，三条边必须连续选择，且尽可能选择最大的边。

python代码如下：

```python
class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        N = len(A)
        res = 0
        # A[i - 2], A[i - 1], A[i]
        for i in range(N - 1, 1, -1):
            if A[i - 2] + A[i - 1] > A[i]:
                return A[i - 2] + A[i - 1] + A[i]
        return 0
```


## 日期

2019 年 1 月 13 日 —— 时间太快了


  [1]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png
  [2]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png
