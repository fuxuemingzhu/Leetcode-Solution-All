

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies/

# 题目描述

给你一个数组 `candies` 和一个整数 `extraCandies` ，其中 `candies[i]` 代表第 `i` 个孩子拥有的糖果数目。

对每一个孩子，检查是否存在一种方案，将额外的 `extraCandies` 个糖果分配给孩子们之后，此孩子有 最多 的糖果。注意，允许有多个孩子同时拥有 最多 的糖果数目。

示例 1：

    输入：candies = [2,3,5,1,3], extraCandies = 3
    输出：[true,true,true,false,true] 
    解释：
    孩子 1 有 2 个糖果，如果他得到所有额外的糖果（3个），那么他总共有 5 个糖果，他将成为拥有最多糖果的孩子。
    孩子 2 有 3 个糖果，如果他得到至少 2 个额外糖果，那么他将成为拥有最多糖果的孩子。
    孩子 3 有 5 个糖果，他已经是拥有最多糖果的孩子。
    孩子 4 有 1 个糖果，即使他得到所有额外的糖果，他也只有 4 个糖果，无法成为拥有糖果最多的孩子。
    孩子 5 有 3 个糖果，如果他得到至少 2 个额外糖果，那么他将成为拥有最多糖果的孩子。

示例 2：

    输入：candies = [4,2,1,1,2], extraCandies = 1
    输出：[true,false,false,false,false] 
    解释：只有 1 个额外糖果，所以不管额外糖果给谁，只有孩子 1 可以成为拥有糖果最多的孩子。

示例 3：

    输入：candies = [12,1,12], extraCandies = 10
    输出：[true,false,true]
 

提示：

1. `2 <= candies.length <= 100`
1. `1 <= candies[i] <= 100`
1. `1 <= extraCandies <= 50`


# 题目大意

如果把剩下的 extraCandies 分给某个孩子，这个孩子能否变为拥有最多糖果的小朋友？

# 解题方法

## 遍历

我们按照题目意思，我们要判断这个小朋友变成拥有糖果最多的小朋友，那么应该先知道再没给糖果之前，小朋友拥有的最多糖果数目是多少。

把糖果依次给各个小朋友，即让各个小朋友的现有的数目 加上 附加糖果数，是否大于等于最多糖果数目。

Python 代码如下：

```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies)
        return [extraCandies + candy >= max_ for candy in candies]
```

**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 5 月 2 日 —— 双周赛最后一题不会，是时候多练练hard题了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79451733
