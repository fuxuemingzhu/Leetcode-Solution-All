
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/all-possible-full-binary-trees/description/

## 题目描述

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.


Example 1:

    Input: 7
    Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
    Explanation:

![此处输入图片的描述][1]
 

Note:

- 1 <= N <= 20



## 题目大意

给出了个N，代表一棵二叉树有N个节点，求所能构成的树。

## 解题方法

所有能构成的树，并且返回的不是数目，而是真正的树。所以一定会把所有的节点都求出来。一般就使用了递归。

这个题中，重点是返回一个列表，也就是说每个能够成的树的根节点都要放到这个列表里。而且当左子树、右子树的节点个数固定的时候，也会出现排列组合的情况，所以使用了两重for循环来完成所有的左右子树的组合。

另外的一个技巧就是，左右子树的个数一定是奇数个。

代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        N -= 1
        if N == 0: return [TreeNode(0)]
        res = []
        for l in range(1, N, 2):
            for left in self.allPossibleFBT(l):
                for right in self.allPossibleFBT(N - l):
                    node = TreeNode(0)
                    node.left = left
                    node.right = right
                    res.append(node)
        return res
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
    vector<TreeNode*> allPossibleFBT(int N) {
        N--;
        vector<TreeNode*> res;
        if (N == 0) {
            res.push_back(new TreeNode(0));
            return res;
        }
        for (int i = 1; i < N; i += 2) {
            for (auto& left : allPossibleFBT(i)) {
                for (auto& right : allPossibleFBT(N - i)) {
                    TreeNode* root = new TreeNode(0);
                    root->left = left;
                    root->right = right;
                    res.push_back(root);
                }
            }
        }
        return res;
    }
};
```

参考资料：https://leetcode.com/problems/all-possible-full-binary-trees/discuss/163429/Simple-Python-recursive-solution.


## 日期

2018 年 8 月 26 日 —— 珍爱生命，远离DD！
2018 年 12 月 2 日 —— 又到了周日

  [1]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/81748335
  [3]: http://ww2.sinaimg.cn/bmiddle/006x6MW7jw1fawdiy39nqj305i05iaa2.jpg
