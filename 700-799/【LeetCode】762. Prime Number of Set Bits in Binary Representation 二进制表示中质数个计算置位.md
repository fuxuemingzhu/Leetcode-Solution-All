
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/][1]


## 题目描述

Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:
    
    Input: L = 6, R = 10
    Output: 4
    Explanation:
    6 -> 110 (2 set bits, 2 is prime)
    7 -> 111 (3 set bits, 3 is prime)
    9 -> 1001 (2 set bits , 2 is prime)
    10->1010 (2 set bits , 2 is prime)

Example 2:
    
    Input: L = 10, R = 15
    Output: 5
    Explanation:
    10 -> 1010 (2 set bits, 2 is prime)
    11 -> 1011 (3 set bits, 3 is prime)
    12 -> 1100 (2 set bits, 2 is prime)
    13 -> 1101 (3 set bits, 3 is prime)
    14 -> 1110 (3 set bits, 3 is prime)
    15 -> 1111 (4 set bits, 4 is not prime)
Note:

1. L, R will be integers L <= R in the range [1, 10^6].
2. R - L will be at most 10000.

## 题目大意

判断在[L, R]闭区间内，有多少数字的二进制表示中1的个数是质数。

## 解题方法

### 遍历数字+质数判断

理解题意之后很简单，要判断所有介于L 和 R之间的数的二进制表示中1的个数是质数的个数。

分解为以下几步：

1. 找到所有介于L 和 R之间的数的二进制表示
2. 判断每个二进制数表示中1的个数是否为质数
3. 求为质数的个数

很容易想到如果是质数返回1否则为0，使用`sum()`函数即可求得为质数的个数。

```python
import math
class Solution(object):
    def isPrime(self, num):
        if num == 1:
            return 0
        elif num == 2:
            return 1
        for i in xrange(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return 0
        return 1
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        return sum(self.isPrime(bin(num)[2:].count('1')) for num in xrange(L, R+1))
```

精简了代码，两行就能搞定。
```python
class Solution(object):
    def countPrimeSetBits(self, L, R):
        isPrime = lambda num : 0 if ((num == 1) or (num % 2 == 0 and num > 2)) else int(all(num % i for i in xrange(3, int(num ** 0.5) + 1, 2)))
        return sum(isPrime(bin(num)[2:].count('1')) for num in xrange(L, R+1))
```

一个数的二进制表示最多只有32位，所以直接保存32以内的质数进行查找判断即可。空间换时间的一个思路。

```python
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        res = 0
        for num in range(L, R + 1):
            if bin(num).count("1") in primes:
                res += 1
        return res
```


## 日期

2018 年 1 月 17 日 
2018 年 11 月 ９ 日 —— 睡眠可以

  [1]: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/
