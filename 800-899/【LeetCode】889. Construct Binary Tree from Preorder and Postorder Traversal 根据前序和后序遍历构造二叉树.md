
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/

## 题目描述

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

    Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
    Output: [1,2,3,4,5,6,7]
 

Note:

- 1 <= pre.length == post.length <= 30
- pre[] and post[] are both permutations of 1, 2, ..., pre.length.
- It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.

## 题目大意

根据先序遍历和后序遍历，重建二叉树。

## 解题方法

讲道理的话，只知道前序和后序遍历是没法确定一棵二叉树的。所以，这个题指明了不含重复元素，而且如果有多棵二叉树返回其中的一种即可。

其实做法还是很简单的。前序和后序的遍历并没有打乱整棵树的关系，一棵树的节点在两种遍历方式所得到的还都是在一块的。

所以pre[0]是根节点，也就是post[-1];

post[-2]时候右子树的根节点，因此在前序遍历中找到post[-2]的位置idx就能分开两棵子树。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre or not post: return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        idx = pre.index(post[-2])
        root.left = self.constructFromPrePost(pre[1:idx], post[:idx-1])
        root.right = self.constructFromPrePost(pre[idx:], post[idx-1:-1])
        return root
```

下面C++代码为了防止平凡的构建子数组，所以使用索引的方式切割数组。C++中，如果函数使用传值的方式进行参数传递，就会调用对象的拷贝构造函数，使得代码效率变慢。所以，一般使用传引用的方式加快函数传参的次数。下面的代码中，pre 和 post使用引用传递，[a,b]表示目前处理的pre区间，[c,d]表示目前处理的post区间。

代码如下：

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
    TreeNode* constructFromPrePost(vector<int>& pre, vector<int>& post) {
        const int N = pre.size();
        for (int i = 0; i < N; i++) m_[post[i]] = i;
        return construct(pre, post, 0, N - 1, 0, N - 1);
    }
private:
    unordered_map<int, int> m_;
    // pre[a, b], post[c, d]
    TreeNode* construct(vector<int>& pre, vector<int>& post, int a, int b, int c, int d) {
        TreeNode* root = new TreeNode(pre[a]);
        if (a == b) return root;
        int t = pre[a + 1];
        int idx = m_[t];
        int len = idx - c + 1;
        root->left = construct(pre, post, a + 1, a + len, c, c + len - 1);
        if (idx + 1 == d) return root;
        root->right = construct(pre, post, a + len + 1, b, idx + 1, d - 1);
        return root;
    }
};
```


参考资料：

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/161651/Easy-Python-Recursive-Solution-with-Explanation
## 日期

2018 年 9 月 4 日 ———— 迎接明媚的阳光！
2018 年 12 月 8 日 —— 今天球打的不错，很舒服
