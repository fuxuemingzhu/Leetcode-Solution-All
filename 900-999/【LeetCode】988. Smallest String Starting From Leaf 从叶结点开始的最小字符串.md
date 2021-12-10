作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/smallest-string-starting-from-leaf/


## 题目描述

Given the ``root`` of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, ``"ab"`` is lexicographically smaller than ``"aba"``.  A leaf of a node is a node that has no children.)

 

Example 1:

![此处输入图片的描述][1]

    Input: [0,1,2,3,4,3,4]
    Output: "dba"

Example 2:

![此处输入图片的描述][2]

    Input: [25,1,3,1,3,0,2]
    Output: "adz"

Example 3:

![此处输入图片的描述][3]

    Input: [2,2,1,null,1,0,null,0]
    Output: "abc"
 

Note:

1. The number of nodes in the given tree will be between 1 and 1000.
1. Each node in the tree will have a value between 0 and 25.
 

## 题目大意

一个二叉树每个节点上面是个0~25的数字代表了a~z各个数字，从叶子节点走向根节点的路径可以看做一个字符串，现在求所有字符串中字典顺序最小的那个是什么。

## 解题方法

### DFS

既然题目说了，要求所有字符串字典顺序中最小的那个，我们简单的方法就是把所有的字符串都求出来然后排序啊！

可以使用DFS把所有的根节点到叶子节点的路径保存下来，由于DFS遍历一定是由上向下的，但是题目要求的是叶子节点到根节点才是路径，所以拼接的时候把每个节点的字符放到路径的前面即可。

这就是普通的DFS，需要提醒注意的是：1.dfs()函数的声明中，path必须是个值传递，res必须是个引用传递。原因是每条路径的path不同，所以需要值传递进行拷贝，但是res是我们定义的同一个res，所以必须使用引用传递。2.在C++中，char可以直接和string相加，无论谁在前谁在后，这个是C++的运算符重载和友元函数定义共同构成的特性。3.没有使用常见的当遍历到空节点的时候才把结果放进去，假如这样做，每个叶子节点会放进去两个相同的字符串，倒也不影响最终的结果。4.题目中已经说了，给出的树最少有一个节点，所以直接dfs的时候不会有空指针。

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
    string smallestFromLeaf(TreeNode* root) {
        vector<string> res;
        dfs(root, "", res);
        sort(res.begin(), res.end());
        return res[0];
    }
    void dfs(TreeNode* root, string path, vector<string>& res) {
        if (!root->left && !root->right) {
            res.push_back(char('a' + root->val) + path);
            return;
        }
        if (root->left)
            dfs(root->left, char('a' + root->val) + path, res);
        if (root->right)
            dfs(root->right, char('a' + root->val) + path, res);
    }
};
```

python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.dfs(root, "", res)
        res.sort()
        return res[0]
    
    def dfs(self, root, path, res):
        if not root.left and not root.right:
            res.append(chr(root.val + ord('a')) + path)
            return
        if root.left:
            self.dfs(root.left, chr(root.val + ord('a')) + path, res)
        if root.right:
            self.dfs(root.right, chr(root.val + ord('a')) + path, res)
```

### BFS

这个题同样也可以使用BFS来解决，遍历的方法也是从上向下进行遍历，我们使用的方式是使用队列同时保存节点和当前节点未加入字符串时的字符串。然后同样当这个节点是叶子节点的时候，把路径保存到列表中。后面排序取字典序最小的即可。

我发现我容易犯一个手误，那就是在BFS的while循环中，把node不知不觉得就写成了root造成了死循环……注意啊！

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
    string smallestFromLeaf(TreeNode* root) {
        queue<pair<TreeNode*, string>> q;
        q.push({root, ""});
        vector<string> res;
        while (!q.empty()) {
            auto h = q.front(); q.pop();
            TreeNode* node = h.first;
            string path = h.second;
            if (!node->left && !node->right) {
                res.push_back(char(node->val + 'a') + path);
                continue;
            }
            if (node->left)
                q.push({node->left, char(node->val + 'a') + path});
            if (node->right)
                q.push({node->right, char(node->val + 'a') + path});
        }
        sort(res.begin(), res.end());
        return res[0];
    }
};
```

python版本的BFS如下。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        q = collections.deque()
        q.append((root, ""))
        res = []
        while q:
            node, path = q.popleft()
            if not node.left and not node.right:
                res.append(chr(node.val + ord('a')) + path)
                continue
            if node.left:
                q.append((node.left, chr(node.val + ord('a')) + path))
            if node.right:
                q.append((node.right, chr(node.val + ord('a')) + path))
        res.sort()
        return res[0]
```

## 日期

2019 年 2 月 20 日 —— 少刷知乎多做题


  [1]: https://assets.leetcode.com/uploads/2019/01/30/tree1.png
  [2]: https://assets.leetcode.com/uploads/2019/01/30/tree2.png
  [3]: https://assets.leetcode.com/uploads/2019/02/01/tree3.png
  [4]: https://assets.leetcode.com/uploads/2019/01/31/tree2.png
  [5]: https://assets.leetcode.com/uploads/2019/01/31/tree2.png
  [6]: https://assets.leetcode.com/uploads/2019/01/31/tree2.png
  [7]: https://assets.leetcode.com/uploads/2019/01/31/tree2.png
  [8]: https://assets.leetcode.com/uploads/2019/01/31/tree2.png
  [9]: https://assets.leetcode.com/uploads/2019/01/31/tree2.png
