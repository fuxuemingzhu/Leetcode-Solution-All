作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

## 题目描述

A conveyor belt has packages that must be shipped from one port to another within ``D`` days.

The ``i``-th package on the conveyor belt has a weight of ``weights[i]``.  Each day, we load the ship with packages on the conveyor belt (in the order given by ``weights``). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within ``D`` days.

Example 1:

    Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
    Output: 15
    Explanation: 
    A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
    1st day: 1, 2, 3, 4, 5
    2nd day: 6, 7
    3rd day: 8
    4th day: 9
    5th day: 10
    
    Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 

Example 2:

    Input: weights = [3,2,2,4,1,4], D = 3
    Output: 6
    Explanation: 
    A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
    1st day: 3, 2
    2nd day: 2, 4
    3rd day: 1, 4

Example 3:

    Input: weights = [1,2,3,1,1], D = 4
    Output: 3
    Explanation: 
    1st day: 1
    2nd day: 2
    3rd day: 3
    4th day: 1, 1
     

Note:

1. 1 <= D <= weights.length <= 50000
1. 1 <= weights[i] <= 500

## 题目大意

把一个数组按顺序输入，每天一艘船，并且每天船的承载量相同，在D天之内需要全部运出去。求每艘船的承载量最少是多少。

## 解题方法

非常类似[875. Koko Eating Bananas][1]这题，使用的方法是二分查找。

怎么分析出来的呢？还是看Note，为什么出了50000这个数字？如果是只和数组长度有关的算法，应该把这个数字设的更大才对。但是如果把50000和500放在一起看大概就明白了，应该是通过重量去遍历数组长度，那么500 × 50000 = 2500 0000的时间复杂度还是有点高。所以我们最终使用的是对重量进行二分，所以log(500) * 50000就能通过了。

对于要进行查找的重量，我们都去计算这个重量情况下，是不是能够在D天之内把所有的货物都拉出去。然后进行简单的二分就可以了。和猴子吃香蕉的题目如出一辙。

Python代码如下：

```python
class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        l = max(weights)
        r = sum(weights)
        # [l, r)
        while l < r:
            mid = l + (r - l) / 2
            need = 1
            cur = 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D:
                l = mid + 1
            else:
                r = mid
        return l
```

## 日期

2019 年 3 月 21 日 —— 好久不刷题，重拾有点难


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82716042
