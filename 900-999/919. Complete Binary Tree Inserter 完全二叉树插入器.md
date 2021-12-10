
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址: https://leetcode.com/problems/complete-binary-tree-inserter/description/

## 题目描述

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure ``CBTInserter`` that is initialized with a complete binary tree and supports the following operations:

- ``CBTInserter(TreeNode root)`` initializes the data structure on a given tree with head node root;
- ``CBTInserter.insert(int v)`` will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, **and returns the value of the parent of the inserted TreeNode**;
- ``CBTInserter.get_root()`` will return the head node of the tree.
 

Example 1:

    Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
    Output: [null,1,[1,2]]

Example 2:

    Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
    Output: [null,3,4,[1,2,3,4,5,6,7,8]]
 

Note:

1. The initial given tree is complete and contains between 1 and 1000 nodes.
1. CBTInserter.insert is called at most 10000 times per test case.
1. Every value of a given or inserted node is between 0 and 5000.

## 题目大意

编写一个完全二叉树的数据结构，需要完成构建、插入、获取root三个函数。函数的参数和返回值如题。

## 解题方法

周赛第三题，因为第二题我不会，就把这个题给放弃了……现在一看很简单啊。

完全二叉树是每一层都满的，因此找出要插入节点的父亲节点是很简单的。如果用数组tree保存着所有节点的层次遍历，那么新节点的父亲节点就是tree[(N -1)/2]，N是未插入该节点前的树的元素个数。

构建树的时候使用层次遍历，也就是BFS把所有的节点放入到tree里。插入的时候直接计算出新节点的父亲节点。获取root就是数组中的第0个节点。

时间复杂度是O(N)，空间复杂度是O(N)。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.tree = list()
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            self.tree.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        _len = len(self.tree)
        father = self.tree[(_len - 1) / 2]
        node = TreeNode(v)
        if not father.left:
            father.left = node
        else:
            father.right = node
        self.tree.append(node)
        return father.val
        

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.tree[0]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
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
class CBTInserter {
public:
    CBTInserter(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* node = q.front(); q.pop();
            if (!node) continue;
            tree.push_back(node);
            q.push(node->left);
            q.push(node->right);
        }
    }
    
    int insert(int v) {
        TreeNode* node = new TreeNode(v);
        tree.push_back(node);
        TreeNode* parent = tree[tree.size() / 2 - 1];
        if (!parent->left)
            parent->left = node;
        else
            parent->right = node;
        return parent->val;
    }
    
    TreeNode* get_root() {
        return tree[0];
    }
private:
    vector<TreeNode*> tree;
};

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter* obj = new CBTInserter(root);
 * int param_1 = obj->insert(v);
 * TreeNode* param_2 = obj->get_root();
 */
```


## 日期

2018 年 10 月 7 日 —— 假期最后一天！！
2018 年 12 月 11 日 —— 双十一已经过去一个月了，真快啊。。
