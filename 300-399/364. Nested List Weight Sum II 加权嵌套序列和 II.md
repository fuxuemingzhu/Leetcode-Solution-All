

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/nested-list-weight-sum-ii/

## 题目描述

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an `integer`, or a `list` -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:

    Input: [[1,1],2,[1,1]]
    Output: 8 
    Explanation: Four 1's at depth 1, one 2 at depth 2.

Example 2:

    Input: [1,[4,[6]]]
    Output: 17 
    Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.



## 题目大意

给一个嵌套整数序列，请你返回每个数字在序列中的加权和，它们的权重由它们的深度决定。
序列中的每一个元素要么是一个整数，要么是一个序列（这个序列中的每个元素也同样是整数或序列）。
与 前一个问题 不同的是，前一题的权重按照从根到叶逐一增加，而本题的权重从叶到根逐一增加。
也就是说，在本题中，叶子的权重为1，而根拥有最大的权重。

## 解题方法

### 递归

这个题的创新点在于，根的权重是最大的，最下面的叶子的权重是1。所以我们需要先求出深度，然后再递归求带权和，递归时给根节点设置权重是深度，每次向叶子方向递归时权重-1，则最下面的叶子节点深度是1.

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
    int depthSumInverse(vector<NestedInteger>& nestedList) {
        int d = depth(nestedList);
        return depthSum(nestedList, d);
    }
    int depthSum(vector<NestedInteger>& nestedList, int depth) {
        if (nestedList.empty()) return 0;
        int res = 0;
        for (NestedInteger ni : nestedList) {
            if (ni.isInteger()) {
                res += ni.getInteger() * depth;
            } else {
                res += depthSum(ni.getList(), depth - 1);
            }
        }
        return res;
    }
    int depth(vector<NestedInteger>& nestedList) {
        if (nestedList.empty()) return 0;
        int max_children = 0;
        for (NestedInteger ni : nestedList) {
            max_children = max(max_children, depth(ni.getList()));
        }
        return max_children + 1;
    }
};
```


## 日期

2019 年 9 月 21 日 —— 莫生气，我若气病谁如意


  [1]: https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png
  [2]: https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png
  [3]: https://assets.leetcode.com/uploads/2018/10/12/bstdllreturnbst.png
  [4]: https://blog.csdn.net/fuxuemingzhu/article/details/79294461
