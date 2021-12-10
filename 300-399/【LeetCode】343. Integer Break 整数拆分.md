
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/integer-break/description/

## 题目描述


Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

	Input: 2
	Output: 1
	Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:

	Input: 10
	Output: 36
	Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

Note: You may assume that n is not less than 2 and not larger than 58.

## 题目大意

一个整数可以拆分成几个较小的整数之和。求如何拆分才能使这几个较小的整数乘积最大。

## 解题方法

### 数学解法

也是一个扔了几个月的题目。有时候会发现，扔了很久的题目，不是太难，而是方法比较少见，其实很简单的罢了。


这个题，我是看了[\[LeetCode\] Integer Break 整数拆分][1]才懂的。下面把分析引用如下：


> 这道题给了我们一个正整数n，让我们拆分成至少两个正整数之和，使其乘积最大，题目提示中让我们用O(n)来解题，而且告诉我们找7到10之间的规律，那么我们一点一点的来分析：
> 
> 正整数从1开始，但是1不能拆分成两个正整数之和，所以不能当输出。
> 
> 那么2只能拆成1+1，所以乘积也为1。
> 
> 数字3可以拆分成2+1或1+1+1，显然第一种拆分方法乘积大为2。
> 
> 数字4拆成2+2，乘积最大，为4。
> 
> 数字5拆成3+2，乘积最大，为6。
> 
> 数字6拆成3+3，乘积最大，为9。
> 
> 数字7拆为3+4，乘积最大，为12。
> 
> 数字8拆为3+3+2，乘积最大，为18。
> 
> 数字9拆为3+3+3，乘积最大，为27。
> 
> 数字10拆为3+3+4，乘积最大，为36。
> 
> ....
> 
> 那么通过观察上面的规律，我们可以看出从5开始，数字都需要先拆出所有的3，一直拆到剩下一个数为2或者4，因为剩4就不用再拆了，拆成两个2和不拆没有意义，而且4不能拆出一个3剩一个1，这样会比拆成2+2的乘积小。那么这样我们就可以写代码了，先预处理n为2和3的情况，然后先将结果res初始化为1，然后当n大于4开始循环，我们结果自乘3，n自减3，根据之前的分析，当跳出循环时，n只能是2或者4，再乘以res返回即可。

我试着证明一下：

当m,n>=2时，有m * n >= m + n。所以把一个整数(m+n)拆开成较小整数（m,n>=2）之后的乘积(m*n)会比原整数(m+n)更大。由归纳法，当拆开的较小整数(m,n)>=4或5时，可以把大于等于4,5的整数拆成更小的整数2和3从而得到不小于4，5的乘积。总之，把任意整数拆成若干2和3的和，此时得到的乘积是最大的。

这里需要说明任意大于等于2的正整数N都能拆解成2*x + 3*y，其中x,y属于自然数。 2*x + 3*y = 2*(x + y) + y。由这个式子可知，当y = 1时，该式子能表示出所有>=3的奇数；当y = 0时，该式子能表示出所有>=2的偶数。因此N = 2*x+3*y至少有一组解。

下面需要求解的是N = 2*x + 3*y时，如何分配x,y才能使得target = 2^x * 3^y是最大的。

首先有y = (N - 2 * x)/3，优化的目标函数两边同时取对数得，log(target) = x*log2 + y*log3.

⇒ log(target) = x * log2 + ((N - 2 * x) / 3) * log3
⇒ x * log2 + (N/3) * log3 - (2x/3) * log3
⇒ (log2 - 2/3 * log3) * x + N/3 * log3
⇒ -0.017 * x + N/3 * log3

由于要优化的log(target)是递增函数，而右式是个递减函数，所以当x越小，则log(target)越大。

综上可知，我们应该把n拆成若干2和3的和，其中2的个数尽可能少，3的个数尽可能多。得到的所有2和3的乘积就是最大乘积。


python代码如下：

```python
class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2: return 1
        if n == 3: return 2
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n
```

C++代码如下：

```cpp
class Solution {
public:
    int integerBreak(int n) {
        if (n == 2) return 1;
        if (n == 3) return 2;
        int res = 1;
        while (n > 4) {
            res *= 3;
            n -= 3;
        }
        return res * n;
    }
};
```


### 动态规划
这个题的动态规划公式是``dp[i] = dp[i - 3] * 3``，当n >= 7时成立。

```python
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 0, 1, 2, 4, 6, 9]
        for i in range(7, n + 1):
            dp.append(dp[i - 3] * 3)
        return dp[n]
```


## 日期

2018 年 5 月 28 日 —— 太阳真的像日光灯～
2019 年 1 月 24 日 —— 快要回家了


  [1]: http://www.cnblogs.com/grandyang/p/5411919.html
