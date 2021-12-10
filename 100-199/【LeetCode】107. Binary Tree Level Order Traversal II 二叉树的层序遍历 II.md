- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/binary-tree-level-order-traversal-ii/](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

Total Accepted: 55876 Total Submissions: 177210 Difficulty: Easy


## 题目描述


Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:

	Given binary tree [3,9,20,null,null,15,7],
	    3
	   / \
	  9  20
	    /  \
	   15   7
	return its bottom-up level order traversal as:
	[
	  [15,7],
	  [9,20],
	  [3]
	]

## 题目大意

从叶子向根进行层次遍历。

## 解题方法

### 方法一：DFS

通过直接的每行元素放到一个List中，再把List放到要返回的List中的方法。最后需要翻转。

标准的DFS解法如下。我都已经背会了。

Python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.levelOrder(root, res, 0)
        return res[::-1]
    
    def levelOrder(self, root, res, level):
        if not root: return
        if level >= len(res):
            res.append([])
        res[level].append(root.val)
        self.levelOrder(root.left, res, level + 1)
        self.levelOrder(root.right, res, level + 1)
```

下面的C++代码没有使用反转结果数组的方式，而是先算了树的高度，然后把第一层的节点放到结果数组的最后，这样实现了逆序。

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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        int d = depth(root);
        vector<vector<int>> res(d);
        dfs(root, res, d - 1);
        return res;
    }
    void dfs(TreeNode* root, vector<vector<int>>& res, int depth) {
        if (!root) return;
        res[depth].push_back(root->val);
        dfs(root->left, res, depth - 1);
        dfs(root->right, res, depth - 1);
    }
    int depth(TreeNode* root) {
        if (!root) return 0;
        return max(depth(root->left), depth(root->right)) + 1;
    }
};
```

### 方法二：迭代

迭代方法也很经典，把每层的节点都放进一个队列里，把每一层的节点依次退出队列，把节点值放入这一层的结果中，并且在队列中放入下一层的节点。最后判断这一层的结果不是空的话，那么就放到最终结果里去。最后，把最终结果翻转。

python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        que = collections.deque()
        que.append(root)
        level = 0
        while que:
            levelVal = []
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if not node:
                    continue
                levelVal.append(node.val)
                que.append(node.left)
                que.append(node.right)
            level += 1
            if levelVal:
                res.append(levelVal)
        return res[::-1]
```

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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        queue<TreeNode*> que;
        que.push(root);
        while (!que.empty()) {
            vector<int> level;
            int size = que.size();
            while (size --) {
                TreeNode* node = que.front(); que.pop();
                if (!node) continue;
                level.push_back(node->val);
                que.push(node->left);
                que.push(node->right);
            }
            if (!level.empty()) {
                res.push_back(level);
            }
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

## 日期

2015/10/14 0:02:45 
2018 年 11 月 17 日 —— 美妙的周末，美丽的天气
2019 年 9 月 20 日 —— 是选择中国互联网式加班？还是外企式养生？
