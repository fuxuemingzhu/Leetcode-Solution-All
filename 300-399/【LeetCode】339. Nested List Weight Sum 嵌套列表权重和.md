
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/nested-list-weight-sum/

## 题目描述

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an `integer`, or a `list` -- whose elements may also be integers or other lists.

Example 1:

    Input: [[1,1],2,[1,1]]
    Output: 10 
    Explanation: Four 1's at depth 2, one 2 at depth 1.

Example 2:

    Input: [1,[4,[6]]]
    Output: 27 
    Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.


## 题目大意

给定一个嵌套的整数列表，请返回该列表按深度加权后所有整数的总和。

每个元素要么是整数，要么是列表。同时，列表中元素同样也可以是整数或者是另一个列表。

## 解题方法

### dfs

既然是个嵌套的结构，那么最简单的肯定是使用dfs去解决。函数的输入是个vector,所以对里面的每个元素进行遍历，判断是整数还是嵌套列表，如果是整数，把结果累加上整数*depth，否则dfs即可。

C++代码如下：

```cpp
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    int depthSum(vector<NestedInteger>& nestedList) {
        return dfs(nestedList, 1);
    }
    int dfs(vector<NestedInteger>& nestedList, int depth) {
        if (nestedList.empty())
            return 0;
        int res = 0;
        for (auto& nest : nestedList) {
            if (nest.isInteger()) {
                res += nest.getInteger() * depth;
            } else {
                res += dfs(nest.getList(), depth + 1);
            }
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 19 日 —— 举杯邀明月，对影成三人


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
