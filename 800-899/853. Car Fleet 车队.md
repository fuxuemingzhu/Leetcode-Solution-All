## 【LeetCode】853. Car Fleet 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/car-fleet/description/

## 题目描述：

``N`` cars are going to the same destination along a one lane road.  The destination is ``target`` miles away.

Each car i has a constant speed ``speed[i]`` (in miles per hour), and initial position ``position[i]`` miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?

 

Example 1:

    Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    Output: 3
    Explanation:
    The cars starting at 10 and 8 become a fleet, meeting each other at 12.
    The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
    The cars starting at 5 and 3 become a fleet, meeting each other at 6.
    Note that no other cars meet these fleets before the destination, so the answer is 3.

Note:

1. 0 <= N <= 10 ^ 4
1. 0 < target <= 10 ^ 6
1. 0 < speed[i] <= 10 ^ 6
1. 0 <= position[i] < target
1. All initial positions are different.

## 题目大意

有N辆车，事先知道了他们的位置和速度，他们要去postion的位置。如果在路上后面的车追上了前面的车，那么不能超过这个车，只能保险杠挨着保险杠用前车的速度继续前进，那么这个叫做一个车队。单辆车也是一个车队，最后需要求的是总共有多少个车队到达终点。

## 解题方法

一遍就AC的题还是很有成就感的。

我的想法是这样的，把车按照位置大小进行排序，计算出每个车在无阻拦的情况下到达终点的时间，如果后面的车到达终点所用的时间比前面车小，那么说明后车应该比前面的车先到。但是由于后车不能超过前车，所以这种情况下就会合并成一个车队，也就是说后车“消失了”。

然后像这种需要判断是否存在的题目一般都是用栈进行解决，对时间遍历，把哪些应该消失的车不进栈就行了。

代码如下：

```python3
class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = [(pos, spe) for pos, spe in zip(position, speed)]
        sorted_cars = sorted(cars)
        times = [(target - pos) / spe for pos, spe in sorted_cars]
        stack = []
        for time in times[::-1]:
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)
        return len(stack)
```

写完之后发现，按照位置正序排列的话，求是否进栈的时候又得逆序过来。所以直接使用逆序排列可以省点事。

```python3
class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = [(pos, spe) for pos, spe in zip(position, speed)]
        sorted_cars = sorted(cars, reverse=True)
        times = [(target - pos) / spe for pos, spe in sorted_cars]
        stack = []
        for time in times:
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)
        return len(stack)
```

## 日期

2018 年 8 月 20 日 ———— 又是一个美好的周一啦！时间真快啊！