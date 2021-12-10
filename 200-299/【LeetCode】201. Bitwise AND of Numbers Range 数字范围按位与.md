# 【LeetCode】201. Bitwise AND of Numbers Range 解题报告（Python） 

标签： LeetCode

---

题目地址：https://leetcode.com/problems/bitwise-and-of-numbers-range/description/

## 题目描述：

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

## 题目大意

计算区间[m,n]内所有数字的与。

## 解题方法

看题感觉需要对所有的[m,n]范围内的数字进行遍历一遍吧。。其实不需要的。

我们知道，数组的数字是连续的，那么m,n范围内的二进制表示的末尾相同位置一定会出现不同的0,1.我们只要找出m,n的做左边起的最长相同的二进制头部即可呀。

如[5, 7]里共有三个数字，分别写出它们的二进制为：

101　　110　　111

相与后的结果为100，仔细观察我们可以得出，最后的数是该数字范围内所有的数的左边共同的部分（即m,n左边的共同部分），如果上面那个例子不太明显，我们再来看一个范围[26, 30]，它们的二进制如下：

11010　　11011　　11100　　11101　　11110

也是前两位是11，后面3位在不同数字中一定会出现0和1、相与即为0了。

我的做法是把m,n同时向右平移，直到两者相等（头部相同了），再把最后的结果向左平移相同的步数。

这个文章讲了4种解法：http://www.cnblogs.com/grandyang/p/4431646.html

代码：

```python
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return m << i
```

## 日期

2018 年 3 月 9 日 
