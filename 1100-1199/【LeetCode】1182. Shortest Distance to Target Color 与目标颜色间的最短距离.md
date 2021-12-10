
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/shortest-distance-to-target-color/

## 题目描述

You are given an array colors, in which there are three colors: `1, 2 and 3`.

You are also given some queries. Each query consists of two integers `i` and `c`, return the shortest distance between the given index `i` and the target color `c`. If there is no solution return -1.

Example 1:

    Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
    Output: [3,0,3]
    Explanation: 
    The nearest 3 from index 1 is at index 4 (3 steps away).
    The nearest 2 from index 2 is at index 2 itself (0 steps away).
    The nearest 1 from index 6 is at index 3 (3 steps away).

Example 2:

    Input: colors = [1,2], queries = [[0,3]]
    Output: [-1]
    Explanation: There is no 3 in the array.

Constraints:

1. `1 <= colors.length <= 5*10^4`
1. `1 <= colors[i] <= 3`
1. `1 <= queries.length <= 5*10^4`
1. `queries[i].length == 2`
1. `0 <= queries[i][0] < colors.length`
1. `1 <= queries[i][1] <= 3`



## 题目大意

给你一个数组 colors，里面有  1、2、 3 三种颜色。
我们需要在 colors 上进行一些查询操作 queries，其中每个待查项都由两个整数 i 和 c 组成。
现在请你帮忙设计一个算法，查找从索引 i 到具有目标颜色 c 的元素之间的最短距离。
如果不存在解决方案，请返回 -1。

## 解题方法

### 字典+二分查找

这个题让我们找到和`nums[i]`最接近的target = `c`的位置。看了下数据规模，**O(N^2)**的方法就放弃吧，这个题的最大时间复杂度限制在了**O(N*log(N))**。

本题困难的地方在于，我们如何快速的找到距离`i`最近的`c`的位置？一个直观的想法当然是找出所有的`c`的位置，然后从中找出和`i`位置最接近的那个。为了保存每个数字的所有出现过的位置，当然使用字典比较好，字典的格式是`unordered_map<int, vector<int>>`，即键是数字，值是一个有序的列表表示了该数字所有的出现过的位置。所以，问题抽象成了：如何在一个有序的列表中，找出最接近的target的数字？

想到时间复杂度的限制，很明显的思路就来了：使用二分查找，找到最接近的target。可以使用`lower_bound()`找出`num[j] >= target`的`j`，最接近于target的数字应该是`nums[j - 1]`或者`nums[j]`。故这里需要做个判断，到底是哪个数字最接近target。

举题目的例子说明：

    Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
    
    字典m如下：
    {
        {1: 0, 1, 3},
        {2: 2, 5, 6},
        {3: 4, 7, 8}
    }
    
    对于query = [1,3]，即找出离colors[1] = 1最近的3。在m[3]中做二分查找找出最接近1的数字，找到了4，所以距离是4 - 1 = 3；
    对于query = [2,2]，即找出离colors[2] = 2最近的2。在m[2]中做二分查找找出最接近2的数字，找到了2，所以距离是2 - 2 = 0；
    对于query = [6,1]，即找出离colors[6] = 2最近的1。在m[1]中做二分查找找出最接近6的数字，找到了3，所以距离是6 - 3 = 3；
    
    
如果题目出现的是：

    对于query = [5,3]，即找出离colors[5] = 2最近的3。在m[3]中做二分查找找出最接近5的数字，lower_bound()找到了7（说明最接近的值是4或者7，经过判断最终选择了4），所以距离是5 - 4 = 1；

C++代码如下：

```cpp
class Solution {
public:
    vector<int> shortestDistanceColor(vector<int>& colors, vector<vector<int>>& queries) {
        const int N = colors.size();
        unordered_map<int, vector<int>> m;
        for (int i = 0; i < N; ++i) {
            m[colors[i]].push_back(i);
        }
        vector<int> res;
        for (auto& query : queries) {
            int cur = INT_MAX;
            int target = query[0];
            if (!m.count(query[1])) {
                res.push_back(-1);
                continue;
            }
            int pos = closest(m[query[1]], target);
            res.push_back(abs(pos - target));
        }
        return res;
    }
    int closest(vector<int>& nums, int target) {
        int pos = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        if (pos == 0) return nums[0];
        if (pos == nums.size()) return nums[nums.size() - 1];
        if (nums[pos] - target < target - nums[pos - 1])
            return nums[pos];
        return nums[pos - 1];
    }
};
```

参考资料：
https://cloud.tencent.com/developer/ask/90642
https://www.bilibili.com/video/av31199112

## 日期

2019 年 9 月 23 日 —— 昨夜睡的早，错过了北京的烟火
