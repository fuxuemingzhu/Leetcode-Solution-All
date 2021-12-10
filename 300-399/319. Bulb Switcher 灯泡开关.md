# 【LeetCode】319. Bulb Switcher 解题报告（Python）

标签（空格分隔）： LeetCode

---

题目地址：https://leetcode.com/problems/bulb-switcher/description/

## 题目描述：

There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

    Example:
    
    Given n = 3. 
    
    At first, the three bulbs are [off, off, off].
    After first round, the three bulbs are [on, on, on].
    After second round, the three bulbs are [on, off, on].
    After third round, the three bulbs are [on, off, off]. 
    
    So you should return 1, because there is only one bulb is on.

## 题目大意

n个灯泡，起始状态是灭的，需要按照1的倍数，2的倍数，3的倍数……的位置打开关闭n次，求最后亮了几个。

## 解题方法

真的是智力题，暴力解法超时，最后的结果是开平方就行。

对于这个题，在http://blog.csdn.net/baidu_23318869/article/details/50386323上有详细的解释，应该能看懂。就不多说了。

代码：

```python
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))
```

## 日期

2018 年 3 月 5 日 