

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/height-checker/

## 题目描述

Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

 

Example 1:

    Input: [1,1,4,2,1,3]
    Output: 3
    Explanation: 
    Students with heights 4, 3 and the last 1 are not standing in the right positions.
 

Note:

1. 1 <= heights.length <= 100
1. 1 <= heights[i] <= 100

## 题目大意

一组数字和排序后的这组数字有多少个位置是不一致的？

## 解题方法

### 排序比较

这个题这么直白啊，直接问和排序后的数字有多少个位置是不一样的。所以排序之后比较就行了呀。看了下数字的范围，竟然只有100个！哪怕是100000直接排序比较也应该会通过！

时间复杂度是O(NlogN)。

Python代码如下：

```python
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return sum(a != b for a, b in zip(sorted(heights), heights))
```

C++代码如下：


```cpp
class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> sortedHeights(heights);
        sort(heights.begin(), heights.end());
        int res = 0;
        for (int i = 0; i < heights.size(); ++i) {
            if (heights[i] != sortedHeights[i])
                ++res;
        }
        return res;
    }
};
```

## 日期

2019 年 6 月 8 日 —— 刷题尽量不要停
