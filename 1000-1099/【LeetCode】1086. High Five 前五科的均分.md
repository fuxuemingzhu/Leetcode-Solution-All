
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/high-five/

## 题目描述

Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry `items[i]` has `items[i][0]` the student's id, and `items[i][1]` the student's score.  The average score is calculated using integer division.

Example 1:

    Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    Output: [[1,87],[2,88]]
    Explanation: 
    The average of the student with id = 1 is 87.
    The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.

Note:

1. `1 <= items.length <= 1000`
1. `items[i].length == 2`
1. The IDs of the students is between 1 to 1000
1. The score of the students is between 1 to 100
1. For each student, there are at least 5 scores


## 题目大意

给你一个不同学生的分数列表，请按 学生的 id 顺序 返回每个学生 最高的五科 成绩的 平均分。
对于每条 items[i] 记录， items[i][0] 为学生的 id，items[i][1] 为学生的分数。平均分请采用整数除法计算。

## 解题方法

### 大根堆

给每个学生一个大根堆，把其所有的成绩都放入堆中，最后堆中最大的5个数字就是最高的5科成绩。

C++代码如下：

```cpp
class Solution {
public:
    vector<vector<int>> highFive(vector<vector<int>>& items) {
        vector<priority_queue<int>> scores(1010);
        for (auto& item : items) {
            scores[item[0]].push(item[1]);
        }
        vector<vector<int>> res;
        for (int i = 0; i < scores.size(); ++i) {
            auto& queue = scores[i];
            if (queue.empty()) continue;
            int sum = 0;
            for (int j = 0; j < 5; ++j) {
                sum += queue.top(); queue.pop();
            }
            res.push_back({i, sum / 5});
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
