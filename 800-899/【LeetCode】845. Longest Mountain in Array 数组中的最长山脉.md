作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/longest-mountain-in-array/description/


## 题目描述

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

- ``B.length >= 3``
- There exists some ``0 < i < B.length - 1`` such that ``B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]``
(Note that B could be any subarray of A, including the entire array A.)

Given an array ``A`` of integers, return the length of the longest mountain. 

Return ``0`` if there is no mountain.

Example 1:

    Input: [2,1,4,7,3,2,5]
    Output: 5
    Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

    Input: [2,2,2]
    Output: 0
    Explanation: There is no mountain.

Note:

1. 0 <= A.length <= 10000
1. 0 <= A[i] <= 10000

Follow up:

- Can you solve it using only one pass?
- Can you solve it in O(1) space?


## 题目大意

找出一个数组中最长的山形数组的长度。所谓山形数组就是前半段是单调递增的，后半段是单调递减的。

## 解题方法

### 双数组

题目做多了之后会发现是有共性的，比如这个题和[926. Flip String to Monotone Increasing][1]就很神似，926题是把数组变成单调递增的，需要统计每个数字位置前面的0的个数和后面的1的个数。而这个题需要我们统计每个位置前面的递增数组的个数和后面递减数组的和。

最简单的方法就是使用两个数组，第一个数组是inc数组，记录的是到目前位置的最长递增连续子数组的长度；第二个数组是dec数组，记录的是当前最长递减连续子数组的长度。所以我们最后需要再次遍历这个数组一次，求当前位置inc和dec的和，还需要减去1，得到的就是当前位置为山峰的最长山形数组。

解释下为什么需要减去1：因为我们inc和dec数组初始化为1，也就是说，我们默认每个位置的数组都是一个长度为1的递增/递减数组。这个想法很显然的，因为如果有两个数字的话就是长度为2的递增或者递减数组。

举例说明：

    输入：[2,1,4,7,3,2,5,1]
    inc: [1, 1, 2, 3, 1, 1, 2, 1]
    dec: [2, 1, 1, 3, 2, 1, 2, 1]


所以当我在求山形数组的时候把inc或者dec为1的位置过滤掉了，因为该位置为1说明这个位置前面或者后面没有跟他构成递增或者递减的数组，那肯定也不是一个山形。

时间复杂度是O(3N)，空间复杂度是O(N).

```python
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        inc = [1] * N
        dec = [1] * N
        for i in range(1, N):
            if A[i] - A[i - 1] > 0:
                inc[i] = inc[i - 1] + 1
        for i in range(N - 2, -1, -1):
            if A[i] - A[i + 1] > 0:
                dec[i] = dec[i + 1] + 1
        res = 0
        for i in range(1, N - 1):
            if inc[i] != 1 and dec[i] != 1:
                res = max(res, inc[i] + dec[i] - 1)
        return res
```


## 参考资料

https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-845-longest-mountain-in-array/

## 日期

2018 年 10 月 26 日 —— 项目验收结束了！


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/83247054
