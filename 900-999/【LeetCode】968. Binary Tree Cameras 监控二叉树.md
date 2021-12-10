作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/binary-tree-cameras/


## 题目描述

Given a binary tree, we install cameras on the nodes of the tree. 

Each camera at a node can monitor ``its parent, itself, and its immediate children``.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

 
Example 1:

![此处输入图片的描述][1]

    Input: [0,0,null,0,0]
    Output: 1
    Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:

![此处输入图片的描述][2]

    Input: [0,0,null,0,null,0,null,null,0]
    Output: 2
    Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Note:

1. The number of nodes in the given tree will be in the range ``[1, 1000]``.
1. ``Every`` node has value 0.


## 题目大意

如果放置一个摄像机，能覆盖当前节点、两个孩子节点、父亲节点。求最少的放置相机的个数。

## 解题方法

首先分析，每种节点能被多少种方案覆盖：

1. 树中间的节点可以被当前节点、两个孩子节点、父亲节点四种方式覆盖。
1. 根节点，可以被当前节点、两个孩子节点三种方式覆盖。
1. 如果是叶子节点，可以被当前节点和父亲节点两种方式覆盖。

综上，我们最好的方案应该是从下向上，先设置叶子节点，然后移除所有覆盖的节点；再重复这个步骤。

具体方法是：

我们定义了一个函数dfs，

1. 如果这个节点是叶子节点，返回0
2. 如果这个节点是叶子节点的父节点，并且这个节点应该放相机，返回1
3. 如果这个节点被子节点覆盖了，并且这个节点没有相机，返回2.

对于每个节点的话，

1. 如果这个节点有子节点，并且这个子节点是叶子节点（节点0），那么当前节点需要相机0；
2. 如果这个节点有子节点，并且这个子节点放置了相机（节点1），那么当前节点被覆盖了；

如果节点需要相机，那么对返回结果+1，并且返回1.
如果节点被覆盖了，返回2.
否则返回0.


C++代码如下：

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int minCameraCover(TreeNode* root) {
        if (dfs(root) == State::NONE)
            ++ans_;
        return ans_;
    }
private:
    enum class State {NONE = 0, COVERED = 1, CAMERA = 2};
    int ans_ = 0;
    State dfs(TreeNode* root) {
        if (!root) return State::COVERED;
        State l = dfs(root->left);
        State r = dfs(root->right);
        if (l == State::NONE || r == State::NONE) {
            ++ans_;
            return State::CAMERA;
        }
        if (l == State::CAMERA || r == State::CAMERA) {
            return State::COVERED;
        }
        return State::NONE;
    }
};
```

参考资料：https://leetcode.com/problems/binary-tree-cameras/discuss/211180/JavaC%2B%2BPython-Greedy-DFS


## 日期

2019 年 1 月 7 日 —— 新的一周开始啦啦啊


  [1]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png
  [2]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png
