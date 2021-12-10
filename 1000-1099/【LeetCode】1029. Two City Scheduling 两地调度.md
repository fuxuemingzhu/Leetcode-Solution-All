
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/two-city-scheduling/

## 题目描述

There are `2N` people a company is planning to interview. The cost of flying the `i`-th person to city `A` is `costs[i][0]`, and the cost of flying the `i`-th person to city `B` is `costs[i][1]`.

Return the minimum cost to fly every person to a city such that exactly `N` people arrive in each city.

 

Example 1:

    Input: [[10,20],[30,200],[400,50],[30,20]]
    Output: 110
    Explanation: 
    The first person goes to city A for a cost of 10.
    The second person goes to city A for a cost of 30.
    The third person goes to city B for a cost of 50.
    The fourth person goes to city B for a cost of 20.

    The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:

1. `1 <= costs.length <= 100`
1. `It is guaranteed that costs.length is even.`
1. `1 <= costs[i][0], costs[i][1] <= 1000`


## 题目大意

给出了偶数个候选人去A和B两个城市的花费，现在要合理分配，让两个城市的人一样多，并且总花费最少。求最少花费。

## 解题方法

### 小根堆

思路怎么来的，是我划了一个表格：

|编号|甲|乙|丙|丁|
|--|--|--|--|--|
|  去A的花费|    10   |   30    |   400 |   30  |
|去B的花费| 20  | 200 |   50  |   40  |
|B-A| +20  | +170 | -350    |   -10   |

根据表格我们可以想到，如果让丙去A，那么会比让丙去B多花350，这样多花费的钱划不来。所以，我们一定让去B比去A花费节省最多的人去B，反之，去A比去B花费节省最多的人去A。故这是一个贪心算法。

具体做法是我们求出每个人B-A的值，让去B能省下最省钱的一半人先去B，剩下的一半人去A.我们可以使用堆或者排序去完成这个事情。

```cpp
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        heap = []
        for i, cost in enumerate(costs):
            heapq.heappush(heap, (cost[1] - cost[0], i))
        res = 0
        count = 0
        while heap:
            cost, pos = heapq.heappop(heap)
            if count < len(costs) / 2:
                res += costs[pos][1]
            else:
                res += costs[pos][0]
            count += 1
        return res
```

### 排序

道理和上面类似。

```cpp
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        _len = len(costs)
        cost_diff = []
        for i, cost in enumerate(costs):
            cost_diff.append((cost[1] - cost[0], i))
        cost_diff.sort()
        res = 0
        count = 0
        for i, (diff, pos) in enumerate(cost_diff):
            if i < _len / 2:
                res += costs[pos][1]
            else:
                res += costs[pos][0]
        return res
```



## 日期

2019 年 8 月 31 日 —— 赶在月底做个题
