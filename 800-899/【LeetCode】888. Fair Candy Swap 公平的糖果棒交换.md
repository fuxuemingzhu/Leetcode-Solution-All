
作者： 负雪明烛
id：	fuxuemingzhu
个人公众号：	**负雪明烛**
本文关键词：力扣，LeetCode，算法题，算法，Python

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/fair-candy-swap/description/

# 题目描述

Alice and Bob have candy bars of different sizes: ``A[i]`` is the size of the i-th bar of candy that Alice has, and ``B[j]`` is the size of the j-th bar of candy that Bob has.

Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)

Return an integer array ``ans`` where ``ans[0]`` is the size of the candy bar that Alice must exchange, and ``ans[1]`` is the size of the candy bar that Bob must exchange.

If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.

 

Example 1:

    Input: A = [1,1], B = [2,2]
    Output: [1,2]

Example 2:

    Input: A = [1,2], B = [2,3]
    Output: [1,2]

Example 3:

    Input: A = [2], B = [1,3]
    Output: [2,3]

Example 4:

    Input: A = [1,2,5], B = [2,4]
    Output: [5,4]
 

Note:

1. 1 <= A.length <= 10000
1. 1 <= B.length <= 10000
1. 1 <= A[i] <= 100000
1. 1 <= B[i] <= 100000
1. It is guaranteed that Alice and Bob have different total amounts of candy.
1. It is guaranteed there exists an answer.

# 题目大意

交换A,B两个数组中的一个数字，使得两个数组的和相等。要返回的结果是个要交换的两个数字，分别来自A,B。

# 解题方法
题目是个 Easy 题目，看了数据范围小于等于 10000， 就不要想太多了，可以直接上 O(N) 的解法！


当两个小朋友交换完了糖果🍬之后，两人手中的糖果大小总和就相等了。那这个数字是多少呢？很显然是两个小朋友目前手中糖果的平均数。


所以，我们可以先求出最终两者手中的糖果大小之和是多少，设为 `target` 。然后逐个判断 Alice 的糖果 `A[i]` ，计算如果把该糖果交换出去，Bob 应该给 Alice 多大的糖果呢？答案应该是 `target - (Alice的糖果总和 - A[i])` ,即 Alice 期望的糖果大小之和 target，减去 Alice 剩余的糖果大小之和。


那么问题来了：如果 Alice 想要用 `A[i]`  跟 Bob 交换，那么 Bob 手里面有没有 Alice 此时想要的糖果大小呢？即 `target - (Alice的糖果总和 - A[i])` 是否在数组 B 中？


由于遍历 Alice 的糖果需要 O(N) 时间复杂度，此时留给 Bob 查找手里是否有 Alice 想要的这个糖果的时间复杂度只剩 O(1) 了。因为如果也用 O(N) 的时间复杂度查找出来，那么总时间复杂度是 `O(N ^ 2)` ，数组长度是 10000， 导致总计算量到达 `10 ^ 8` ，可能会超时。


在常用的数据结构中，只有 Set 能够满足在 O(1) 时间内，判断一个元素是否存在。我们使用 Set 在 Bob 手中查找是否包含目标糖果。

# 代码


本题的代码比较简单。


1. 求数组 A、数组 B 所有糖果大小的总和；使用 set 保存 B 中的各个元素；
1. 求出两个小朋友手中糖果大小总和相等时的目标 target；
1. 遍历 A 中的每个糖果，求如果把该糖果交换出去，期望 Bob 交换的糖果大小 expect_b。
1. 从 B 的 set 中查找是否包含 expect_b，如果包含则说明 `[a, expect_b]` 是一种可以满足要求的交换。



时间复杂度：O(N)，因为只对数组 A 遍历了一次。
空间复杂度：O(N)，因为用了 set 保存数组 B 的所有元素。

使用 Python2 写的代码如下。

```python
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_A, sum_B, set_B = sum(A), sum(B), set(B)
        target = (sum_A + sum_B) // 2
        for a in A:
            expect_b = target - (sum_A - a)
            if expect_b in set_B:
                return [a, expect_b]
        return []
```

# 刷题心得


今天这个题虽然简单，但还是有可以积累的新知识的：


1. 时间复杂度的估计，要学会根据数据规模，判断应该用什么时间复杂度的算法。
1. 根据时间复杂度寻找合适的算法/数据结构，因此需要牢记算法/数据结构的时间复杂度。
1. set 是一种拿空间换时间的数据结构，能够在 `O(1)` 的时间内判断某个元素是否存在其中。

# 关于作者

我是本文的作者是**负雪明烛**，毕业于北京邮电大学，目前就职于阿里巴巴。坚持刷算法题 5 年，共计刷了 800 多道算法题。做过的每个算法题都在 CSDN 上写题解博客，获得好评无数，CSDN 的累计阅读量已经 160万 次！博客地址是：[https://blog.csdn.net/fuxuemingzhu](https://blog.csdn.net/fuxuemingzhu)

「**每日算法题**」公众号是我维护的一个算法题解公众号，主要讲解算法题的解法，也会分享找工作的经验。欢迎关注。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210201104331157.jpg)


# 日期

2018 年 8 月 24 日 —— Keep fighting!
2018 年 11 月 ９ 日 —— 睡眠可以
