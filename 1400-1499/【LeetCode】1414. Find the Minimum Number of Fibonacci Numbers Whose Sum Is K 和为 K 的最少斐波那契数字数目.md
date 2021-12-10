
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/contest/biweekly-contest-24/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

# 题目描述

给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。

斐波那契数字定义为：

- `F1 = 1`
- `F2 = 1`
- `Fn = Fn-1 + Fn-2` ， 其中 n > 2 。

数据保证对于给定的 k ，一定能找到可行解。


示例 1：

    输入：k = 7
    输出：2 
    解释：斐波那契数字为：1，1，2，3，5，8，13，……
    对于 k = 7 ，我们可以得到 2 + 5 = 7 。

示例 2：

    输入：k = 10
    输出：2 
    解释：对于 k = 10 ，我们可以得到 2 + 8 = 10 。

示例 3：

    输入：k = 19
    输出：3 
    解释：对于 k = 19 ，我们可以得到 1 + 5 + 13 = 19 。
 

提示：

1. `1 <= k <= 10^9`

# 题目大意

在斐波那契数列中，至少取多少个数字（可重复），从而构成k.

# 解题方法

## 贪心

看 k 的数字规模是 `10 ^ 9`，但是我们应该关注斐波那契数列的规模有多大。当斐波那契数列越往后，越接近与 `2 ^ x`，那么估算 `2 ** 30 = 1073741824`，所以本题中的斐波那契数列不会超过30.

那就暴力求就行了啊！

只要 k 没变成0， 那么就**贪心**地从斐波那契数列中找出比 k 小的那个最大数字，让k减去它。计算总的减了多少次。

因为数列中有1的存在，所以 k 最后一定会变成0。

Python代码如下：

```python
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])
        res = 0
        while k != 0:
            for i in range(len(fib) - 1, -1, -1):
                if fib[i] <= k:
                    k -= fib[i]
                    res += 1
                    break
        return res
```


**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 18 日 —— 个人赛蒙了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79451733
