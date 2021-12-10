
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/poor-pigs/description/

## 题目描述

There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. They all look the same. If a pig drinks that poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.

Answer this question, and write an algorithm for the follow-up general case.

**Follow-up:**

If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the "poison" bucket within p minutes? There is exact one bucket with poison.

## 题目大意

有1000个桶，其中有一个桶里有毒药，其他的都是正常的。一头猪喝了毒药之后，过了15分钟会上天。只给了60分钟，问至少需要多少头猪来找出有毒的桶？

下面给了一个Follow-up，是桶数（n），上天时间为m，在p分钟内检测出来，求猪数x。

## 解题方法

这个题让我想起来本科的时候的微机原理，那个时候有题目是拨号键盘。通过监测拨号键盘行和列有哪些有电平，来检测出按下了哪个键。

一只猪在一个小时内最多验多少桶呢？这个猪可以喝4桶水，如果有毒就会死亡，否则说明这4桶没问题。如果只有5桶水，那么第5桶一定有问题。

两只猪呢？那就是拨号键盘了，每15分钟喝一个行或者列的所有5桶水，根据两只猪死亡时间，按照拨号键盘的思路，知道了毒水在几行几列。也就是两头猪最多验出来25个桶。

    1    2   3   4   5
    
    6    7   8   9  10
    
    11  12  13  14  15
    
    16  17  18  19  20
    
    21  22  23  24  25


更多的猪，不难看出，就是一个多维的空间了，当有N只的时候，求出5^N>=1000，就能得出了N。


代码如下：

```python
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        tests = minutesToTest / minutesToDie + 1
        pigs = 0
        while tests ** pigs < buckets:
            pigs += 1
        return pigs
```

参考资料：https://blog.csdn.net/wilschan0201/article/details/72519147

## 日期

2018 年 7 月 17 日 —— 连天大雨，这种情况很少见，但是很舒服
2018 年 11 月 19 日 —— 周一又开始了

  [1]: http://www.cnblogs.com/grandyang/p/7500082.html
