
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/sum-of-two-integers/description/


## 题目描述

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
    
    Example:
    Given a = 1 and b = 2, return 3.

## 题目大意

不使用+-号，完成两个数字的加法。

## 解题方法

### 位运算

在不准使用+和-的情况下实现两个整数的加法，那么肯定要用到位运算了。我们考虑位运算加法的四种情况：

    0 + 0 = 0
    
    1 + 0 = 1
    
    0 + 1 = 1
    
    1 + 1 = 0(with carry)

XOR的一个重要特性是不进位加法，那么只要再找到进位，将其和XOR的结果加起来，就是最后的答案。通过观察上面的四种情况我们可以发现，只有在两个加数的值都是1的时候才会产生进位，所以我们采用&来计算进位的情况，但是注意到由于是进位，所以我们必须要将&的结果左移一位，然后再和XOR的结果相加。

举例来看：
    
![此处输入图片的描述][1]
    
再举个例子: 11+5

    其二进制形式为11: 1011, 5: 0101
    
    1. 那么两个位置都为1的地方就需要进位, 所以进位值就为0001. 原位置两个数相加的结果为那个位置值的异或即1110, 即两个位置值如果不一样就为1, 一样的话要么两个位置原来值都为0结果也为0, 要么进位, 那么结果依然是0. 
    
    2. 接下来就要把进位位和下一位相加, 所以进位值左移一位,即0001变为0010, 重复上面操作可得新的**进位值**为0010, 原位置异或(即相加)结果为1100.
    
    3. 继续重复上面操作直到进位为0, 可得到最终结果10000, 即16

这个题的做法就是用a保存“直接加”（不考虑进位）的结果，用b保存进位；然后使a再与b相加，直至保存进位的b为0.

“直接加”通过XOR实现，进位通过and实现。

所以困扰了我两年的题终于想明白了。。

```python
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)
```

## 日期

2018 年 2 月 26 日 
2018 年 11 月 11 日 —— 剁手节快乐

参考： 
http://blog.csdn.net/qq508618087/article/details/51789576
https://www.cnblogs.com/dyzhao-blog/p/5662891.html

  [1]: https://images2015.cnblogs.com/blog/920491/201607/920491-20160712110859998-340357180.png
