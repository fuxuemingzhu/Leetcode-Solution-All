

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/minimum-number-of-refueling-stops/

## 题目描述


A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each ``station[i]`` represents a gas station that is ``station[i][0]`` miles east of the starting position, and has ``station[i][1]`` liters of gas.

The car starts with an infinite tank of gas, which initially has ``startFuel`` liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 

Example 1:

    Input: target = 1, startFuel = 1, stations = []
    Output: 0
    Explanation: We can reach the target without refueling.

Example 2:

    Input: target = 100, startFuel = 1, stations = [[10,100]]
    Output: -1
    Explanation: We can't reach the target (or even the first gas station).

Example 3:

    Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
    Output: 2
    Explanation: 
    We start with 10 liters of fuel.
    We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
    Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
    and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
    We made 2 refueling stops along the way, so we return 2.
     

Note:

1. ``1 <= target, startFuel, stations[i][1] <= 10^9``
1. ``0 <= stations.length <= 500``
1. ``0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target``

## 题目大意

一个车刚开始的时候有一些油，现在在一条直线上有一些加油站，第i个加油站距离出发点的距离和储油量是station[i][0]和station[i][1]，假设汽车的油箱是无限大的，现在求从出发点出发能否到达结束点target，如果可以的话，需要经历的最少加油站是多少。

## 解题方法

### 贪心算法

这个题是我遇到的腾讯面试题和2019年百度笔试题。

这个题的直观思路是当油箱剩的有油的时候，不能遇到加油站就去加油，因为可能在油用完之前遇到另一个存油量很多的加油站。所以在这个思路下，如何解呢？

这个题的方法是，我们使用一个大根堆保存所有经历过的加油站的存量，也就相当于把油放到后备箱里（注意不是油箱）。当我们无法到达某个加油站的时候，就是在半路熄火了，此时应该从后备箱中拿出最大的那个油桶进行加油，如果仍然不够到达加油站，则继续把后备箱的油拿出来加上。

所以，如果把后备箱的油全部都拿出来用完了仍然不能到达加油站的情况下，则返回-1.否则，由于是个贪心策略，所以使用了最少的加油站的油。

代码的思路是，使用一个大根堆保存经历过的加油站的油量，即放到了后备箱里。使用prev保存上一个加油站的位置，对所有的加油站进行遍历，判断从上一个加油站到当前加油站需要用掉多少油，如果油箱不够用了则贪心使用后备箱中最大的油桶。当后备箱的油全部用完了，仍然不能到达现在的加油站，则返回-1。

注意，python的heapq默认是小根堆，如果想用大根堆，需要在放入数字的时候添加负号。

Python代码如下：

```python
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        # [pos, fuel]
        stations.append([target, float("inf")])
        # -fuel
        que = []
        pos = 0
        tank = startFuel
        res = 0
        prev = 0
        for p, g in stations:
            tank -= p - prev
            while que and tank < 0:
                tank += -heapq.heappop(que)
                res += 1
            if tank < 0:
                return -1
            heapq.heappush(que, -g)
            prev = p
        return res
```

参考资料：https://leetcode.com/problems/minimum-number-of-refueling-stops/solution/

## 日期

2019 年 4 月 3 日 —— 好久不刷题了，越来越手生
