# 【LeetCode】481. Magical String 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/magical-string/description/

## 题目描述：

A magical string S consists of only '1' and '2' and obeys the following rules:

The string S is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string S itself.

The first few elements of string S is the following: S = "1221121221221121122……"

If we group the consecutive '1's and '2's in S, it will be:

1 22 11 2 1 22 1 22 11 2 11 22 ......

and the occurrences of '1's or '2's in each group are:

1 2	2 1 1 2 1 2 2 1 2 2 ......

You can see that the occurrence sequence above is the S itself.

Given an integer N as input, return the number of '1's in the first N number in the magical string S.

Note: N will not exceed 100,000.

Example 1:

    Input: 6
    Output: 3
    Explanation: The first 6 elements of magical string S is "12211" and it contains three 1's, so return 3.

## 题目大意

有一个遵守一个规则的字符串S，求这个S前n位共有多少个1.这个规则是这样的：把相同的数字合并成一个组，然后统计这个组的长度，我们发现这个组的长度组成的新的字符串和S是完全相等的。

## 解题方法

一定要手动推算一下才明白这个逻辑。因为只有1和2两个数字，组的长度和S是相同的，所以是可以确定S的每个位置的。

S的开头一定是1,2,2；合并就是1个1、2个2，所以到了第三个数字，这个数字是2，所以一定是2个1，故S的下两位是1，即S是1,2,2,1,1；到了S的第四个数字是1，所以下面是1个2；即S是1,2,2,1,1,2……

通过上面的规律看出，需要一个列表一个指针，指针每次向后走一个位置，S增加的是指针指向的这个位置的数字 个 （3-列表最后一个数字）。

注意，因为列表每次可能会增加一个或者两个数字，我们需要的是前n个数字，所以最后统计1的时候，需要对S进行切片。

代码如下：

```python
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        S = [1, 2, 2]
        idx = 2
        while len(S) < n:
            S += [3 - S[-1]] * S[idx]
            idx += 1
        return S[:n].count(1)
```

参考资料：

https://leetcode.com/problems/magical-string/discuss/96472/Short-Python-using-queue

## 日期

2018 年 9 月 7 日 ———— 中午不睡，下午崩溃