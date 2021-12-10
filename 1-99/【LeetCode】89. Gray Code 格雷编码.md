
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/gray-code/description/

## 题目描述

The ``gray code`` is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given ``n = 2``, return ``[0,1,3,2]``. Its gray code sequence is:

    00 - 0
    01 - 1
    11 - 3
    10 - 2

Note:

For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

## 题目大意

求n位的格雷码序列。格雷码是指相邻的两个数字的二进制只会有一位不同。

## 解题方法

这个题目是属于回溯法的题目。但是，查了一下百度百科的格雷码，根本用不到回溯啊摔！！

下面是百度百科告诉的如何求n位的格雷码的方法。

> 递归生成码表
> 
> 这种方法基于格雷码是反射码的事实，利用递归的如下规则来构造：
> 
> 1. 1位格雷码有两个码字
> 2. (n+1)位格雷码中的前2n个码字等于n位格雷码的码字，按顺序书写，加前缀0
> 3. (n+1)位格雷码中的后2n个码字等于n位格雷码的码字，按逆序书写，加前缀1 
> 4. n+1位格雷码的集合 = n位格雷码集合(顺序)加前缀0 + n位格雷码集合(逆序)加前缀1

简言之就是递归。第（n+1）位的格雷码序列=（'0'+第n位的正序） + （'1'+第n位的逆序）

题目中说了n是非负数，当n=0的时候，返回[0]即可。

所以循环版本：

```python
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        grays = dict()
        grays[0] = ['0']
        grays[1] = ['0', '1']
        for i in range(2, n + 1):
            n_gray = []
            for pre in grays[i - 1]:
                n_gray.append('0' + pre)
            for pre in grays[i - 1][::-1]:
                n_gray.append('1' + pre)
            grays[i] = n_gray
        return map(lambda x: int(x, 2), grays[n])
```

递归版本：

```python
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return map(lambda x: int(x, 2), self.bit_gray(n))
    
    def bit_gray(self, n):
        ans = None
        if n == 0:
            ans = ['0']
        elif n == 1:
            ans = ['0', '1']
        else:
            pre_gray = self.bit_gray(n - 1)
            ans = ['0' + x for x in pre_gray] + ['1' + x for x in pre_gray[::-1]]
        return ans
```

C++代码如下：

```cpp
class Solution {
public:
    vector<int> grayCode(int n) {
        if (n == 0) return {0};
        if (n == 1) return {0, 1};
        vector<int> res;
        vector<int> pre = grayCode(n - 1);
        for (int p : pre) {
            res.push_back(p);
        }
        for (auto p = pre.rbegin(); p < pre.rend(); p++) {
            res.push_back((1 << (n - 1)) + *p);
        }
        return res;
    }
};
```

## 日期

2018 年 6 月 12 日 —— 实验室上午放假2333刷题吧
2018 年 12 月 20 日 —— 感冒害的我睡不着

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/80661715
