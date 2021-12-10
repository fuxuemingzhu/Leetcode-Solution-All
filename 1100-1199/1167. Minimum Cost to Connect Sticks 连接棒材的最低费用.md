

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/minimum-cost-to-connect-sticks/

## 题目描述

You have some sticks with positive integer lengths.

You can connect any two sticks of lengths `X` and `Y` into one stick by paying a cost of `X + Y`.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

Example 1:

    Input: sticks = [2,4,3]
    Output: 14

Example 2:

    Input: sticks = [1,8,3,5]
    Output: 30

Constraints:

1. `1 <= sticks.length <= 10^4`
1. `1 <= sticks[i] <= 10^4`



## 题目大意

为了装修新房，你需要加工一些长度为正整数的棒材 sticks。
如果要将长度分别为 X 和 Y 的两根棒材连接在一起，你需要支付 X + Y 的费用。 由于施工需要，你必须将所有棒材连接成一根。
返回你把所有棒材 sticks 连成一根所需要的最低费用。注意你可以任意选择棒材连接的顺序。

## 解题方法

### 小根堆

这个题是遇到过的微软面试题。

其实题目是让我们生成一个哈弗曼树，做法是使用小根堆，每次选用最小的两根棒材，拼接到一块，然后放入小根堆中。重复这个操作，直至小根堆中只有一个棒材为止。


C++代码如下：

```cpp
class Solution {
public:
    int connectSticks(vector<int>& sticks) {
        priority_queue<int, vector<int>, greater<int>> que;
        for (int stick : sticks) {
            que.push(stick);
        }
        int res = 0;
        while (!que.empty()) {
            int first = que.top(); que.pop();
            if (!que.empty()) {
                int second = que.top(); que.pop();
                int sum = first + second;
                res += sum;
                que.push(sum);
            }
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 23 日 —— 昨夜睡的早，错过了北京的烟火
