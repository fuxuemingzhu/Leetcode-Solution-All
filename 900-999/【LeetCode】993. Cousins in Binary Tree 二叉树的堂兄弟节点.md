
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/cousins-in-binary-tree/


## 题目描述

In a binary tree, the root node is at depth ``0``, and children of each depth ``k`` node are at depth ``k+1``.

Two nodes of a binary tree are *cousins* if they have the same depth, but have different parents.

We are given the ``root`` of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return ``true`` if and only if the nodes corresponding to the values ``x`` and ``y`` are cousins.


Example 1:

![此处输入图片的描述][1]

    Input: root = [1,2,3,4], x = 4, y = 3
    Output: false

Example 2:

![此处输入图片的描述][2]

    Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
    Output: true

Example 3:

![此处输入图片的描述][3]

    Input: root = [1,2,3,null,4], x = 2, y = 3
    Output: false
 
Note:

1. The number of nodes in the tree will be between 2 and 100.
1. Each node has a unique integer value from 1 to 100.



## 题目大意

如果一个二叉树中的两个节点的父亲不同，但是高度相同，那么这两个节点是堂兄弟。判断给出的两个值为x和y的节点是不是堂兄弟。

## 解题方法

### DFS

如果做过[987. Vertical Order Traversal of a Binary Tree][4]，那么这个题肯定很快就能写出来。

题目要求的判断条件有两个1.父节点不同，2.高度相同，所以最直白的方法就是把每个节点的父节点和高度都求出来，然后判断x和y这两个节点是不是符合要求即可。

这个题中每个节点的值都不会重复，所以可以直接用值当做key来存储，代码很简单。

python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.m = collections.defaultdict(tuple)
        self.dfs(root, None, 0)
        px, dx = self.m[x]
        py, dy = self.m[y]
        return dx == dy and px != py
    
    def dfs(self, root, parent, depth):
        if not root: return
        self.m[root.val] = (parent, depth)
        self.dfs(root.left, root, depth + 1)
        self.dfs(root.right, root, depth + 1)
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
    bool isCousins(TreeNode* root, int x, int y) {
        m_.clear();
        dfs(root, nullptr, 0);
        auto px = m_[x], py = m_[y];
        return px.first != py.first && px.second == py.second;
    }
private:
    unordered_map<int, pair<TreeNode*, int>> m_;
    void dfs(TreeNode* root, TreeNode* parent, int depth) {
        if (!root) return;
        m_[root->val] = make_pair(parent, depth);
        dfs(root->left, root, depth + 1);
        dfs(root->right, root, depth + 1);
    }
};
```

### BFS

相似的，BFS也可以做，不过更简单一点的是不用在队列里保存每个节点的高度了，因为在BFS中搜完每一层才向下一层搜索，所以可以很方便的计算每个节点的高度。

Python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        m = collections.defaultdict(tuple)
        q = collections.deque()
        q.append((root, None))
        depth = 0
        while q:
            size = len(q)
            for i in range(size):
                node, p = q.popleft()
                if not node: continue
                m[node.val] = (p, depth)
                q.append((node.left, node))
                q.append((node.right, node))
            depth += 1
        px, dx = m[x]
        py, dy = m[y]
        return dx == dy and px != py
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
    bool isCousins(TreeNode* root, int x, int y) {
        queue<pair<TreeNode*, TreeNode*>> q;
        q.push(make_pair(root, nullptr));
        unordered_map<int, pair<TreeNode*, int>> m_;
        int depth = 0;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                auto p = q.front(); q.pop();
                if (!p.first) continue;
                m_[p.first->val] = make_pair(p.second, depth);
                q.push(make_pair(p.first->left, p.first));
                q.push(make_pair(p.first->right, p.first));
            }
            ++depth;
        }
        auto px = m_[x], py = m_[y];
        return px.first != py.first && px.second == py.second;
    }
};
```

## 日期

2019 年 2 月 21 日 —— 一放假就再难抓紧了


  [1]: https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png
  [2]: https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png
  [3]: https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png
  [4]: https://blog.csdn.net/fuxuemingzhu/article/details/87829987
