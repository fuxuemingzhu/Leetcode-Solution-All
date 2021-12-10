
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/string-to-integer-atoi/

# 题目描述

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![此处输入图片的描述][1]

The above elevation map is represented by array `[0,1,0,2,1,0,1,3,2,1,2,1]`. 

In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6


# 题目大意

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 解题方法

## 暴力求解

让我们求总的能接多少雨水，这个题有两种解法，一种是每个**位置**都去判断能接多少雨水，一种是每个**区间**去判断接多少雨水。

最简单的暴力解法，求**每个位置**的储水量：

1. 遍历每个位置，找到这个位置左边和右边的最高柱子高度；
2. 求两个最高柱子中取最矮的高度（短板效应，短板决定盛水量）；
3. 减去当前柱子的高度就是储水量。

这个时间复杂度是O(N^2)，会**超时**。

C++代码如下。

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        const int N = height.size();
        int res = 0;
        auto begin = height.begin();
        auto end = height.end();
        for (int i = 0; i < N; ++i) {
            int left_max = *max_element(begin, begin + i + 1);
            int right_max = *max_element(begin + i, end);
            res += min(left_max, right_max) - height[i];
        }
        return res;
    }
};
```

## 保存左右最大值

在上面的暴力解法中，我们知道在每个位置都要求其左右的最大柱子的高度，因此是不是可以更快速的求出来这个值呢？

在很多题目里面，都有这种做法，为了能找出每个位置左右的最大值，可以提前计算并保存。比如，使用left_max和right_max数组，分别保存每个位置的左右两边的最大高度。计算时包含了当前位置，目的是防止出现两边的柱子比当前的位置矮，减的时候出现负值。

使用两边的高度的最小值 - 当前柱子的高度就是该位置的储水量。

C++代码如下：

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        const int N = height.size();
        int res = 0;
        vector<int> left_max(N, 0);
        vector<int> right_max(N, 0);
        for (int i = 0; i < N; ++i) {
            left_max[i] = i == 0 ? height[i] : max(left_max[i - 1], height[i]);
        }
        for (int i = N - 1; i >= 0; --i) {
            right_max[i] = i == N - 1 ? height[i] : max(right_max[i + 1], height[i]);
        }
        for (int i = 0; i < N; ++i) {
            res += min(left_max[i], right_max[i]) - height[i];
        }
        return res;
    }
};
```

## 单调栈

如果你考虑的是一个**区间**能接多少雨水的话可以使用单调栈。

考虑单调栈的原因是我们从左向右看的时候，发现只有先下降、后上升的情况，才会存储水。

图片来源[甜姨的题解][2]：

![此处输入图片的描述][3]

我们看到每次都要向左边找到左边最高的柱子，然后求这个区间内的面积。

![此处输入图片的描述][4]

我们看到其实是一层一层的向上累计的。

那么，我们使用一个单调递减栈，每次遇到一个新的位置，都把栈中的元素遍历出来，找出所有的比当前位置矮的，累积计算这部分面积。

计算面积公式：`（两柱子的最小高度 - 两柱子之间的最大高度）* 距离`。


C++代码如下：

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        const int N = height.size();
        if (N < 3) return 0;
        int res = 0;
        stack<int> st;
        int idx = 0;
        while (idx < N) {
            if (st.empty() || height[idx] <= height[st.top()]) {
                st.push(idx);
                idx ++;
            } else {
                int last = st.top(); st.pop();
                if (st.empty()) continue;
                int distance = idx - st.top() - 1;
                res += distance * (min(height[st.top()], height[idx]) - height[last]);
            }
        }
        return res;
    }
};
```

 **欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 4 日 —— 全国哀悼日


  [1]: https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png
  [2]: https://leetcode-cn.com/problems/trapping-rain-water/solution/dan-diao-zhan-jie-jue-jie-yu-shui-wen-ti-by-sweeti/
  [3]: https://pic.leetcode-cn.com/7d5ff9af88634d417d7925e8987b7db92d3a26766bd9078215ab63df424fa745-water.gif
  [4]: https://pic.leetcode-cn.com/1d1c62807d886ac9a10229cbae229465989bd6aa707449e9620a639772ba3f07-image.png
