
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/contest/biweekly-contest-24/problems/minimum-value-to-get-positive-step-by-step-sum/

# 题目描述

给你一个整数数组 nums 。你可以选定任意的 正数 startValue 作为初始值。

你需要从左到右遍历 nums 数组，并将 startValue 依次累加上 nums 数组中的值。

请你在确保累加和始终大于等于 1 的前提下，选出一个最小的 正数 作为 startValue 。

 

示例 1：

    输入：nums = [-3,2,-3,4,2]
    输出：5
    解释：如果你选择 startValue = 4，在第三次累加时，和小于 1 。
                    累加求和
                    startValue = 4 | startValue = 5 | nums
                      (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
                      (1 +2 ) = 3  | (2 +2 ) = 4    |   2
                      (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
                      (0 +4 ) = 4  | (1 +4 ) = 5    |   4
                      (4 +2 ) = 6  | (5 +2 ) = 7    |   2

示例 2：

    输入：nums = [1,2]
    输出：1
    解释：最小的 startValue 需要是正数。

示例 3：

    输入：nums = [1,-2,-3]
    输出：5
     

提示：

1. `1 <= nums.length <= 100`
1. `-100 <= nums[i] <= 100`


# 题目大意

让你找个最小的正数startValue，使得startValue从左到右累加一遍的时候保证和至少为1.

# 解题方法

## 求和

让我们求最小的 startValue，就是让我们求从左到右累加所有数字的时候，出现的最小的和 min_sum。

1. 当 min_sum > 0 的时候，比如示例2，我们让startValue设置为1.
2. 当 min_sum <= 0 的时候，让 startValue + min_sum >= 1，就让 startValue 为 1 - min_sum即可。

Python代码如下：

```python
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num
            min_sum = min(min_sum, cur_sum)
        return 1 if min_sum > 0 else 1 - min_sum
```


**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 18 日 —— 周赛死于第4题


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79451733
