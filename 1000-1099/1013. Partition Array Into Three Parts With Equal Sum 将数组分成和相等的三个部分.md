作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

## 题目描述

In a list of songs, the ``i``-th song has a duration of ``time[i]`` seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by ``60``.  Formally, we want the number of indices ``i < j`` with ``(time[i] + time[j]) % 60 == 0``.

Example 1:

    Input: [30,20,150,100,40]
    Output: 3
    Explanation: Three pairs have a total duration divisible by 60:
    (time[0] = 30, time[2] = 150): total duration 180
    (time[1] = 20, time[3] = 100): total duration 120
    (time[1] = 20, time[4] = 40): total duration 60

Example 2:

    Input: [60,60,60]
    Output: 3
    Explanation: All three pairs have a total duration of 120, which is divisible by 60.

Note:

1. ``1 <= time.length <= 60000``
1. ``1 <= time[i] <= 500``

## 题目大意

统计有多少两个数，``i < j``并且``(time[i] + time[j]) % 60 == 0``。相当于two sum的改进。

## 解题方法

这个题怎么想？注意看Note给的提示！首先给出的数组长度是60000，那么是复杂度应该是O(N)，看到每个元素的大小是1~500，那么很容易想到，是不是可以对time的元素进行统计，然后统计每两个数字的和是不是60的倍数即可。

首先需要统计每个数字出现的次数。

如果两个数字不同的话，并且这两个数字的和是60的倍数，直接把两个数字的个数相乘。

当然第二个例子提醒了我们，可以在同样的数字中选择两个，所以从相同的数字中任意选择两个，公式是 N * (N - 1) / 2。

Python代码如下：

```python
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        count = collections.Counter(time)
        key = list(count.keys())
        N = len(key)
        res = 0
        for i, t in enumerate(key):
            for j in range(i, N):
                if (t + key[j]) % 60 == 0:
                    if i == j:
                        res += count[t] * (count[t] - 1) / 2
                    else:
                        res += count[t] * count[key[j]]
        return res
```


## 日期

2019 年 3 月 21 日 —— 好久不刷题，重拾有点难


  [1]: https://assets.leetcode.com/uploads/2019/03/06/1266.png
  [2]: https://assets.leetcode.com/uploads/2019/03/08/domino.png
