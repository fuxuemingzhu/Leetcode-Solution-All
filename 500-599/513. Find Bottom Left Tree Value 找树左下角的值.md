
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/find-bottom-left-tree-value/#/description][1]


## 题目描述


Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:

	Input:
	
	    2
	   / \
	  1   3
	
	Output:
	1

Example 2: 

	Input:
	
	        1
	       / \
	      2   3
	     /   / \
	    4   5   6
	       /
	      7
	
	Output:
	7

Note: You may assume the tree (i.e., the given root node) is not NULL.

## 题目大意

求一个二叉树最下面一层的最左边节点。

## 解题方法

### BFS

这就是所谓的BFS算法。广度优先搜索，但是搜索的顺序是有要求的，因为题目要最底层的叶子节点的最左边的叶子，那么进入队列的顺序就是先右节点再左节点，这样能把每层的节点都能从右到左过一遍，那么用一个int保存最后的节点值就可以了。

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int findBottomLeftValue(TreeNode root) {
        int ans = 0;
        Queue<TreeNode> tree = new LinkedList<TreeNode>();
        tree.offer(root);
        while(!tree.isEmpty()){
            TreeNode temp = tree.poll();
            if(temp.right != null){
                tree.offer(temp.right);
            }
            if(temp.left != null){
                tree.offer(temp.left);
            }
            ans = temp.val;
        }
        return ans;
    }
}
```

Python做法是用层次遍历，用的是双向队列，所以注意append和popleft。代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = collections.deque()
        q.append(root)
        res = []
        while q:ruxai
            size = len(q)
            level = []
            for i in range(size):
                node = q.popleft()
                if not node: continue
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if level:
                res.append(level)
        return res[-1][0]
```

使用C++用的是BFS版本的层次遍历，代码如下：

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
    int findBottomLeftValue(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        vector<vector<int>> res;
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front(); q.pop();
                if (!node) continue;
                level.push_back(node->val);
                q.push(node->left);
                q.push(node->right);
            }
            if (!level.empty()) {
                res.push_back(level);
            }
        }
        return res[res.size() - 1][0];
    }
};
```

### DFS

使用DFS很简单了，直接把每一层的元素放到list里面，然后取出最后层的第一个节点即可。至于子树的遍历顺序，需要保证先遍历左子树再遍历右子树，这样才能把最下面一层的最左边节点放到最左侧，至于根节点的值在哪个位置进行append是不重要的。

python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.dfs(root, res, 0)
        return res[-1][0]
    
    def dfs(self, root, res, level):
        if not root: return
        if level == len(res): res.append([])
        res[level].append(root.val)
        self.dfs(root.left, res, level + 1)
        self.dfs(root.right, res, level + 1)
```

C++代码需要注意的是，我们应该对res传引用进来，否则不能对外部变量进行更改。

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
    int findBottomLeftValue(TreeNode* root) {
        dfs(root, res, 0);
        return res[res.size() - 1][0];
    }
private:
    vector<vector<int>> res;
    void dfs(TreeNode* root, vector<vector<int>>& res, int level) {
        if (!root) return;
        if (level == res.size()) res.push_back({});
        res[level].push_back(root->val);
        dfs(root->left, res, level + 1);
        dfs(root->right, res, level + 1);
    }
};
```

## Date

2017 年 4 月 13 日 


  [1]: https://leetcode.com/problems/find-bottom-left-tree-value/#/description
