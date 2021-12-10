

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/path-sum-iv/

## 题目描述

If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:

1. The hundreds digit represents the depth `D` of this node, `1 <= D <= 4.`
1. The tens digit represents the position `P` of this node in the level it belongs to, `1 <= P <= 8`. The position is the same as that in a full binary tree.
1. The units digit represents the value `V` of this node, `0 <= V <= 9`.

Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5, you need to return the sum of all paths from the root towards the leaves.

Example 1:

    Input: [113, 215, 221]
    Output: 12
    Explanation: 
    The tree that the list represents is:
        3
       / \
      5   1
    
    The path sum is (3 + 5) + (3 + 1) = 12.

Example 2:

    Input: [113, 221]
    Output: 4
    Explanation: 
    The tree that the list represents is: 
        3
         \
          1
    
    The path sum is (3 + 1) = 4.

## 题目大意

给定一个包含三位整数的升序数组，表示一棵深度小于 5 的二叉树，请你返回从根到所有叶子结点的路径之和。

## 解题方法

### DFS

这个题很新颖，很少见。我们知道树的表示方法有两种，一种是链表方式，一种是数组方式。这个题考的就是我们的数组方式。数组方式也是很有用的，比如在堆排序中，就很实用。

![此处输入图片的描述][1]

在一个数组表示的树中，如果一个节点的索引是index，那么其左孩子是index * 2，右孩子是index * 2 + 1。

我们先把给出的nums数组进行拆解，把每个数放入数组中对应的节点中。数组的默认数字是-1，也就是说-1表示空节点。

再计算带权路径和的时候，需要找到每个叶子节点的路径，判断是否是叶子节点的方法是看其两个孩子的值是不是都是-1。题目给定的数组的深度是5，那么最多有32个叶子节点，为了方便叶子节点的判断，选择了大小为64的数组。

如果一个节点是叶子节点，那么累加路径长度到最后的结果中就行了。

C++代码如下：

```cpp
class Solution {
public:
    int pathSum(vector<int>& nums) {
        vector<int> tree(64, -1);
        for (int n : nums) {
            int v = n % 10; n /= 10;
            int p = n % 10; n /= 10;
            int d = n % 10;
            tree[(int)pow(2, d - 1) + p - 1] = v;
        }
        dfs(tree, 1, 0);
        return sum;
    }
    void dfs(vector<int>& tree, int index, int parent) {
        if (tree[index] == -1) return;
        if (tree[index * 2] == -1 && tree[index * 2 + 1] == -1) {
            sum += parent + tree[index];
            return;
        }
        dfs(tree, index * 2, parent + tree[index]);
        dfs(tree, index * 2 + 1, parent + tree[index]);
    }
private:
    int sum = 0;
};
```

## 日期

2019 年 9 月 24 日 —— 梦见回到了小学，小学已经芳草萋萋破败不堪


  [1]: https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3958884440,3883801982&fm=26&gp=0.jpg
