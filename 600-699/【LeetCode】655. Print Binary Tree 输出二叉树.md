
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/print-binary-tree/description/

## 题目描述

Print a binary tree in an m*n 2D string array following these rules:

- The row number m should be equal to the height of the given binary tree.
- The column number n should always be an odd number.
- The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
- Each unused space should contain an empty string "".
- Print the subtrees following the same rules.

Example 1:

    Input:
         1
        /
       2
    Output:
    [["", "1", ""],
     ["2", "", ""]]

Example 2:

    Input:
         1
        / \
       2   3
        \
         4
    Output:
    [["", "", "", "1", "", "", ""],
     ["", "2", "", "", "", "3", ""],
     ["", "", "4", "", "", "", ""]]

Example 3:

    Input:
          1
         / \
        2   5
       / 
      3 
     / 
    4 
    Output:
    
    [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
     ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
     ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
     ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]


Note: The height of binary tree is in the range of [1, 10].
    


## 题目大意

使用二维数组打印出二叉树。如果某个位置是空节点，也应该给它留出对应的位置。

## 解题方法

### DFS

最初认为，给空节点留下位置加大了题目难度。其实真正理解题目要考察的内容之后，发现这个条件让我们可以使用``完全二叉树``的数学公式，所以使题目变得简单了。

这个题首先要求出树的高度，然后求出完全二叉树的宽度。根据高度和宽度构建出二维数组，再利用递归求出每个层次的每个节点对应的二维数组的位置，设为节点的值即可。

如果是DFS去做的话，每次向下搜索的时候，需要传入这个子区间的起始位置。根节点放在中间。

说的容易，难的再求这些公式，真的就是完全二叉树的一些知识。具体的就看这两篇文章吧，很详细。

1. https://leetcode.com/problems/print-binary-tree/discuss/106273/Simple-Python-with-thorough-explanation

1. https://leetcode.com/problems/print-binary-tree/discuss/106250/Python-Straight-Forward-Solution

代码：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root: return [""]
        def getDepth(root):
            if not root:
                return 0
            return 1 + max(getDepth(root.left), getDepth(root.right))
        d = getDepth(root)
        cols = 2 ** d - 1
        self.res = [["" for i in range(cols)] for j in range(d)]
        def helper(root, d, pos):
            self.res[-d - 1][pos] = str(root.val)
            if root.left: helper(root.left, d - 1, pos - 2 ** (d - 1))
            if root.right: helper(root.right, d - 1, pos + 2 ** (d - 1))
        helper(root, d - 1, 2 ** (d - 1) - 1)
        return self.res
```

上面的python代码不够直观，如果使用类似二分查找的方式，使用left和right表示左右区间，那么代码可以写成下面这样。

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
    vector<vector<string>> printTree(TreeNode* root) {
        const int h = depth(root);
        int w = pow(2, h) - 1;
        vector<vector<string>> res(h, vector<string>(w, ""));
        dfs(root, res, 0, 0, w);
        return res;
    }
private:
    int depth(TreeNode* root) {
        if (!root) return 0;
        return max(depth(root->left), depth(root->right)) + 1;
    }
    // [left, right)
    void dfs(TreeNode* root, vector<vector<string>>& res, int depth, int left, int right) {
        if (!root || depth == res.size()) return;
        int mid = left + (right - left) / 2;
        res[depth][mid] = to_string(root->val);
        dfs(root->left, res, depth + 1, left, mid);
        dfs(root->right, res, depth + 1, mid + 1, right);
    }
};
```

### BFS

使用BFS的话，就是类似于层次遍历的解法。这个题困难的地方在于不好找出节点要放置的位置。所以使用了两个BFS，一个BFS用来遍历节点，另一个BFS用来保存每个节点对应的起始位置。每次把根节点放到中间的地方，也就有点类似于二分查找。

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
    vector<vector<string>> printTree(TreeNode* root) {
        const int h = depth(root);
        int w = pow(2, h) - 1;
        int curH = -1;
        vector<vector<string>> res(h, vector<string>(w, ""));
        queue<TreeNode*> q;
        q.push(root);
        // [first, second)
        queue<pair<int, int>> idxQ;
        idxQ.push({0, w});
        while (!q.empty()) {
            curH++;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front(); q.pop();
                auto idx = idxQ.front(); idxQ.pop();
                if (!node) continue;
                int left = idx.first, right = idx.second;
                int mid = left + (right - left) / 2;
                res[curH][mid] = to_string(node->val);
                q.push(node->left);
                q.push(node->right);
                idxQ.push({left, mid});
                idxQ.push({mid + 1, right});
            }
        }
        return res;
    }
private:
    int depth(TreeNode* root) {
        if (!root) return 0;
        return max(depth(root->left), depth(root->right)) + 1;
    }
};
```

上面需要同时维护两个队列，其实可以使用一个队列，这个队列同时维护了该节点以及该节点所在的区间的左右位置。而在BFS中是不用维护当前的高度的，BFS可以存储当前属于哪一层。

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
    vector<vector<string>> printTree(TreeNode* root) {
        int d = depth(root);
        int w = (1 << d) - 1;
        queue<pair<TreeNode*, pair<int, int>>> q; // TreeNode*, start, end
        q.push({root, {0, w}});
        vector<vector<string>> res(d, vector<string>(w));
        int curd = 0;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                auto f = q.front(); q.pop();
                TreeNode* node = f.first;
                int start = f.second.first;
                int end = f.second.second;
                if (!node) continue;
                int mid = start + (end - start) / 2;
                res[curd][mid] = to_string(node->val);
                q.push({node->left, {start, mid - 1}});
                q.push({node->right, {mid + 1, end}});
            }
            ++curd;
        }
        return res;
    }
    int depth(TreeNode* root) {
        if (!root) return 0;
        return max(depth(root->left), depth(root->right)) + 1;
    }
};
```

## 日期

2018 年 3 月 4 日 
2018 年 12 月 18 日 —— 改革开放40周年
2019 年 2 月 25 日 —— 二月就要完了
