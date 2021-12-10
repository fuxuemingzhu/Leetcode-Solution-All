- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/reducing-dishes/

# 题目描述

一个厨师收集了他 n 道菜的满意程度 `satisfaction` ，这个厨师做出每道菜的时间都是 1 单位时间。

一道菜的 「喜爱时间」系数定义为烹饪这道菜以及之前每道菜所花费的时间乘以这道菜的满意程度，也就是 `time[i]*satisfaction[i]` 。

请你返回做完所有菜 「喜爱时间」总和的最大值为多少。

你可以按 任意 顺序安排做菜的顺序，你也可以选择放弃做某些菜来获得更大的总和。

 

示例 1：

    输入：satisfaction = [-1,-8,0,5,-9]
    输出：14
    解释：去掉第二道和最后一道菜，最大的喜爱时间系数和为 (-1*1 + 0*2 + 5*3 = 14) 。每道菜都需要花费 1 单位时间完成。

示例 2：

    输入：satisfaction = [4,3,2]
    输出：20
    解释：按照原来顺序相反的时间做菜 (2*1 + 3*2 + 4*3 = 20)

示例 3：

    输入：satisfaction = [-1,-4,-5]
    输出：0
    解释：大家都不喜欢这些菜，所以不做任何菜可以获得最大的喜爱时间系数。

示例 4：

    输入：satisfaction = [-2,5,-1,0,3,-3]
    输出：35

提示：

1. `n == satisfaction.length`
1. `1 <= n <= 500`
1. `-10^3 <= satisfaction[i] <= 10^3`


# 题目大意

合理安排做菜的顺序，让 `等菜时间 * 满意度` 的和最大

# 解题方法

## 贪心

这个题我想了动态规划等方法，但是没实现出来。其实需要一些技巧的。

首先的思路是：满意度越高的菜应该越在后面做，这样可以乘以等菜时间，实现喜爱时间最大化。

显然，我们需要对满意度进行排序。

这个题难就难在会有一些满意度是负数的菜，这些要不要上？从 示例 1 中我们看到如果添加上一个负数，能让后面的正数的满意度扩大，所以有可能会让负数添加到前面。

这个题的做法：
1. 先把满意度进行排序
2. 从满意度最大的开始，向满意度小的遍历。每次添加的一个新的满意度对应的等菜时间是 1， 而已经添加过的菜的喜爱时间需要再增加一次。

使用 before 保存前面已经添加过的所有菜的喜爱时间。使用 sum_time 保存现在为止添加了所有的菜的总的喜爱时间。

所以：

    sum_time += before + satisfaction[i];
    before += satisfaction[i];

最后找出 sum_time 的最大值即为所求。

C++代码如下。

```cpp
class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        const int N = satisfaction.size();
        sort(satisfaction.begin(), satisfaction.end());
        int res = 0;
        int sum_time = 0;
        int before = 0;
        for (int i = N - 1; i >= 0; --i) {
            sum_time += before + satisfaction[i];
            before += satisfaction[i];
            res = max(res, sum_time);
        }
        return res;
    }
};
```

 **欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 5 日 —— 好久不打周赛了


  [1]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_4_1728.png
  [2]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_2_1728.png
  [3]: https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_6_1728.png
