作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/contest/weekly-contest-110/problems/range-sum-of-bst/


## 题目描述

Given the ``root`` node of a binary search tree, return the sum of values of all nodes with value between ``L`` and ``R`` (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:

    Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
    Output: 32

Example 2:

    Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
    Output: 23
     

Note:

1. The number of nodes in the tree is at most 10000.
1. The final answer is guaranteed to be less than 2^31.


## 题目大意

找出一个BST中，计算在[L,R]双闭区间内的所有节点的值的和。

## 解题方法

### 递归

看见BST，就想起来它特殊的性质。所以这个题肯定能用上性质。

如果root不存在，返回0。如果root节点在[L,R]内，那么把结果加上root的值，然后再分别加上左右子树的值。为什么？因为这个时候左右子树都可能存在满足[L,R]区间，所以必须都加上。

如果root的值比L还小，说明左子树一定不会满足[L,R]区间，那么直接向右边找就行。

如果root的值比R还大，说明右子树一定不会满足[L,R]区间，那么直接向左边找就行。

时间复杂度是O(N)，空间复杂度是O(1)。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        if L <= root.val <= R:
            res += root.val
            res += self.rangeSumBST(root.left, L, R)
            res += self.rangeSumBST(root.right, L, R)
        elif root.val < L:
            res += self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            res += self.rangeSumBST(root.left, L, R)
        return res
```

也可以直接判断寻找的方向，能简化一点代码。如果root节点小于R，说明右边可以继续搜索；如果root节点大于L，说明左边可以继续搜索。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        res = [0]
        self.dfs(root, L, R, res)
        return res[0]
    
    def dfs(self, root, L, R, res):
        if not root:
            return
        if L <= root.val <= R:
            res[0] += root.val
        if root.val < R:
            self.dfs(root.right, L, R, res)
        if root.val > L:
            self.dfs(root.left, L, R, res)
```

C++版本的代码如下：

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
    int rangeSumBST(TreeNode* root, int L, int R) {
        dfs(root, L, R);
        return res;
    }

private:
    int res = 0;
    void dfs(TreeNode* root, int L, int R) {
        if (root == nullptr) return;
        if (root->val <= R && root->val >= L) res += root->val;
        if (root->val > L) dfs(root->left, L, R);
        if (root->val < R) dfs(root->right, L, R);
    }
};
```

## 日期

2018 年 11 月 11 日 —— 剁手节快乐
2018 年 12 月 2 日 —— 又到了周日

  [1]: https://assets.leetcode.com/uploads/2018/10/12/island.png
  [2]: https://charlesliuyx.github.io/2018/10/11/%E3%80%90%E7%9B%B4%E8%A7%82%E7%AE%97%E6%B3%95%E3%80%91Egg%20Puzzle%20%E9%B8%A1%E8%9B%8B%E9%9A%BE%E9%A2%98/
