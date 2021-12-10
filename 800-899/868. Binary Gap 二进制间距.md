
作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/binary-gap/description/

## 题目描述

Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.

 

Example 1:

    Input: 22
    Output: 2
    Explanation: 
    22 in binary is 0b10110.
    In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
    The first consecutive pair of 1's have distance 2.
    The second consecutive pair of 1's have distance 1.
    The answer is the largest of these two distances, which is 2.

Example 2:

    Input: 5
    Output: 2
    Explanation: 
    5 in binary is 0b101.

Example 3:

    Input: 6
    Output: 1
    Explanation: 
    6 in binary is 0b110.

Example 4:
    
    Input: 8
    Output: 0
    Explanation: 
    8 in binary is 0b1000.
    There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.
 

Note:

- 1 <= N <= 10^9

## 题目大意

求一个数的二进制中，最远的两个1之间的距离。如果只有一个1，那么返回0.

## 解题方法

### 线性扫描

先求二进制，然后统计二进制中每个1离左边1的距离即可。用left保存左边1出现的位置，距离就是当前1的index减去left。然后求这个列表中的最大值即可。

题目给出的N的范围是``1 <= N <= 10^9``，直接求还是比较合适的。

时间复杂度是O(N)，空间复杂度是O(32).

代码如下：

```python
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = bin(N)[2:]
        dists = [0] * len(binary)
        left = 0
        for i, b in enumerate(binary):
            if b == '1':
                dists[i] = i - left
                left = i
        return max(dists)
```

可以优化空间复杂度，使用结果进行保存每个位置的最大值就行了。

```python
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        nbins = bin(N)[2:]
        index = -1
        res = 0
        for i, b in enumerate(nbins):
            if b == "1":
                if index != -1:
                    res = max(res, i - index)
                index = i
        return res
```



## 日期

2018 年 7 月 17 日 —— 连天大雨，这种情况很少见，但是很舒服
2018 年 11 月 8 日 —— 项目进展缓慢
