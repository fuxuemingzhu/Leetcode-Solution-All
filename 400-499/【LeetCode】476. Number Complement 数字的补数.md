- 作者： 负雪明烛
- id： fuxuemingzhu
- 个人博客： http://fuxuemingzhu.cn/
- 公众号：负雪明烛
- 本文关键词：Leetcode, 力扣，476, 补数，二进制，Python, C++, Java

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/number-complement/][1]

 - Difficulty: Easy

# 题目描述

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:

1. The given integer is guaranteed to fit within the range of a 32-bit signed integer.
2. You could assume no leading zero bit in the integer’s binary representation.

Example 1:

	Input: 5
	Output: 2
	Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:

	Input: 1
	Output: 0
	Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
    
# 解题方法
今天题目重点是：**补数。**

> 补数是对该数的二进制取反。

​

注意二进制中是没有前导 0 的，也就是说二进制 表示的数字中，第一位必然是 1。


## 方法一：取反


位运算中有一个运算符 `~` 表示取反，可不可以用它呢？我们实验一下：
```python
>>> Integer.toBinaryString(5)
101
>>> Integer.toBinaryString(~5)
11111111111111111111111111111010
```
我们看到，虽然 5 的二进制 101 被取反了，但是其前导 0 也被取反。
​

所以我们不能直接用 `~` 运算符。
​

下面的思路就是找到数字的二进制中，第一个 1 的位置了。


对于 Java 而言，有库函数可以使用 `Integer.highestOneBit(num)` ，它的作用是只保留 `num` 二进制的最高位的 1 的情况下的数字。
​

```python
>>> Integer.highestOneBit(5)
4
```
​

我们想得到和 `num` 的二进制位置相等的全 1 的数字，可以用 `((Integer.highestOneBit(num)) << 1) - 1`。
​

Java 语言的代码如下：
​

```java
public class Solution {
    public int findComplement(int num) {
        return ~num & ((Integer.highestOneBit(num) << 1) - 1);
    }
}
```


复杂度分析：

- 时间复杂度：$O(1)$，和数据规模无关；
- 空间复杂度：$O(1)$，只使用了常数个空间。
## 方法二：异或


注意到求补数，就是把现有的二进制表示各位进行了 0, 1 互换，很容易想到**异或**操作。


> 0 ^ 1 = 1
> 1 ^ 1 = 0


所以我们应该把原本的数字的每一位都和 1 进行异或计算。


我们需要构建和源数字的二进制位数相等的全 1 数字。求源数字的二进制数字长度可以用方法一，也可以直接获取二进制字符串长度。
​

Python 代码如下：
​

```python
class Solution:
    def findComplement(self, num):
        return num ^ ((1 << (len(bin(num)) - 2)) - 1)
```
​
复杂度分析：
- 时间复杂度：$O(1)$，和数据规模无关；
- 空间复杂度：$O(1)$，只使用了常数个空间。



## 方法三：二进制字符串


另一种常见的思路是先把输入数字 `num` 转成二进制字符串，将二进制字符串中的 `'0'` 和 `'1'` 互换，再转成 10 进制数字。


Python 语言的代码如下：


```python
class Solution:
    def findComplement(self, num):
        bin_num = bin(num)[2:]
        bin_ans = map(lambda x: '0' if x == '1' else '1', bin_num)
        return int(''.join(bin_ans), 2)
```


复杂度分析：

- 时间复杂度：$O(1)$，和数据规模无关；
- 空间复杂度：$O(1)$，只使用了常数个空间。

# 总结


1. 这个题的重点是获取二进制数字的长度。
1. 除了上面的方法外，还可以逐位遍历，找到其二进制的第一个 1。

​
# 日期

2017 年 1 月 15 日 
2018 年 7 月 4 日 
2018 年 11 月 6 日 —— 腰酸背痛要废了
2021 年 10 月 18 日

  [1]: https://leetcode.com/problems/max-consecutive-ones/
