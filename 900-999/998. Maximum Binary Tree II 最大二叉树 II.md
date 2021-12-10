作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/maximum-binary-tree-ii/


## 题目描述

We are given the ``root`` node of a maximum tree: a tree where every node has a value greater than any other value in its subtree.

Just as in the ``previous problem``, the given tree was constructed from an list ``A (root = Construct(A))`` recursively with the following ``Construct(A)`` routine:

- If ``A`` is empty, return ``null``.
- Otherwise, let ``A[i]`` be the largest element of ``A``.  Create a root node with value ``A[i]``.
- The left child of root will be ``Construct([A[0], A[1], ..., A[i-1]])``
- The right child of root will be ``Construct([A[i+1], A[i+2], ..., A[A.length - 1]])``
- Return ``root``.

Note that we were not given A directly, only a root node ``root = Construct(A)``.

Suppose B is a copy of A with the value val appended to it.  It is guaranteed that B has unique values.

Return ``Construct(B)``.


Example 1:

![此处输入图片的描述][1]

    Input: root = [4,1,3,null,null,2], val = 5
    Output: [5,4,null,1,3,null,null,2]
    Explanation: A = [1,4,2,3], B = [1,4,2,3,5]

Example 2:

![此处输入图片的描述][2]

    Input: root = [5,2,4,null,1], val = 3
    Output: [5,2,4,null,1,null,3]
    Explanation: A = [2,1,5,4], B = [2,1,5,4,3]

Example 3:
    
![此处输入图片的描述][3]
    
    Input: root = [5,2,3,null,1], val = 4
    Output: [5,2,4,null,1,3]
    Explanation: A = [2,1,5,3], B = [2,1,5,3,4]
 

Note:

1. ``1 <= B.length <= 100``


## 题目大意

给出了一个最大树A，在最大树A的数组表示的末尾添加一个val构成一个新的数组表示，并生成最大树B，返回新最大树的root节点。

最大树就是找出数组中最大的元素作为根节点，该最大元素左边元素当做左子树、右边元素当做右子树。

## 解题方法

### 递归

本来拿到这个题，想的第一种方法是先求出A的数组表示，其求法是对于最大树，从左到右竖着看，和每个节点相交的顺序拼起来就是答案。不过这个做法我们写出来。

然后就直接用递归了，这个题最重要的一个信息就是在最大树A的数组表示的``末尾添加``val，也就是单词append.如果会python的应该都明白，不过也发现有的同学不懂append的含义，然后不明白题目意思了。

递归最重要的是明白递归函数的意义：``insertIntoMaxTree(TreeNode* root, int val)``代表了向root子树的数组表示法的末尾添加一个值为val的新节点，并把结果进行返回。

1. 如果原来的A不存在，那么很简单要返回该新节点。
1. 如果A存在，在A的数组表示的最后新添加了一个val，两种情况：
    - 如果val > root.val，已知root.val是数组中最大的元素了，所以，此时会形成一个新的根节点，并把原来的A当做该根节点的左子树
    - 如果val < root.val，那么仍然要记住该节点是在最大元素的右边，所以根节点的右子树变成了在根节点的右子树插入val的新子树。

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
    TreeNode* insertIntoMaxTree(TreeNode* root, int val) {
        if (!root) return new TreeNode(val);
        if (val > root->val) {
            TreeNode* newRoot = new TreeNode(val);
            newRoot->left = root;
            return newRoot;
        } else {
            root->right = insertIntoMaxTree(root->right, val);
        }
        return root;
    }
};
```

## 日期

2019 年 2 月 24 日 —— 周末又结束了


  [1]: https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-1-2.png
  [2]: https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-2-1.png
  [3]: https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-3-1.png
