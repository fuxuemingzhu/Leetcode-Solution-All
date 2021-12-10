作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

@[TOC](目录)

题目地址：https://leetcode.com/problems/koko-eating-bananas/description/

## 题目描述

Koko loves to eat bananas.  There are ``N`` piles of bananas, the ``i-th`` pile has ``piles[i] ``bananas.  The guards have gone and will come back in ``H`` hours.

Koko can decide her bananas-per-hour eating speed of ``K``.  Each hour, she chooses some pile of bananas, and eats ``K`` bananas from that pile.  If the pile has less than ``K`` bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer ``K`` such that she can eat all the bananas within ``H`` hours.

 

Example 1:

    Input: piles = [3,6,7,11], H = 8
    Output: 4

Example 2:

    Input: piles = [30,11,23,4,20], H = 5
    Output: 30

Example 3:

    Input: piles = [30,11,23,4,20], H = 6
    Output: 23
 

Note:

1. 1 <= piles.length <= 10^4
1. piles.length <= H <= 10^9
1. 1 <= piles[i] <= 10^9

## 题目大意

coco去吃香蕉，时间最多只有H小时，但这个吃货会享受，她想在用最慢的速度去吃。吃的速度是K，代表一个小时吃多少香蕉。这吃货懒到什么地步？当一个小时以内她就把这堆里边的香蕉吃完了，那她就停下来歇着，等待下一个小时继续吃。求她吃东西的最慢的速度。

## 解题方法

### 二分查找

二叉搜索的变种题目。因为有个最慢的速度而且是整数。

这个速度的范围一定在1和max(piles)之间，如果大于max(piles)肯定不是最慢速度。然后我们使用二分，计算在某个速度之下吃完的时间是否满足时间H。如果时间比H大，说明她吃的太快了，应该降低速度；反之应该加快速度。

吃每堆香蕉的时间是math.ceil(pile / speed)。

时间复杂度是O(logn)，空间复杂度是O(1)。

Python代码如下：

```python
class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        minSpeed, maxSpeed = 1, max(piles)
        while minSpeed <= maxSpeed:
            speed = minSpeed + (maxSpeed - minSpeed) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / speed)
            if hour <= H:
                maxSpeed = speed - 1
            else:
                minSpeed = speed + 1
        return minSpeed
```

二刷的时候，使用了现在习惯的[left, right)左闭右开区间进行二分查找。代码如下：

```python
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        l, r = 1, sum(piles)
        # [l, r)
        while l < r:
            K = l + (r - l) / 2
            curH = 0
            for p in piles:
                curH += p // K + (1 if p % K else 0)
            if curH > H:
                l = K + 1
            else:
                r = K
        return l
```


参考资料：

https://leetcode.com/problems/koko-eating-bananas/discuss/152506/Logical-Thinking-with-Java-Code

## 日期

2018 年 9 月 15 日 —— 天气转冷，小心着凉
2019 年 3 月 24 日 —— 二刷还是挺好的
