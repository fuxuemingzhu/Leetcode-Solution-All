- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)


---
@[TOC](目录)

题目地址：https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/

## 题目描述

Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a ``3-ary`` tree:

![此处输入图片的描述][1]
 
Return its preorder traversal as: ``[1,3,5,6,2,4]``.
 
Note: Recursive solution is trivial, could you do it iteratively?

## 题目大意

N叉树的前序遍历。

## 解题方法

### 递归

首先得明白，这个N叉树是什么样的数据结构定义的。val是节点的值，children是一个列表，这个列表保存了其所有节点。

前序遍历，即首先把根节点的值放到list中，然后再遍历其子节点们的值，同时对于每一个子节点也做同样的操作。

时间复杂度是O(N)，空间复杂度是O(1).

Python代码如下：

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        res.append(root.val)
        for child in root.children:
            res.extend(self.preorder(child))
        return res
```

C++代码如下：

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> res;
        if (!root) return res;
        res.push_back(root->val);
        for (Node* child : root->children) {
            vector<int> child_vector = preorder(child);
            res.insert(res.end(), child_vector.begin(), child_vector.end());
        }
        return res;
    }
};
```

### 迭代

就像题目说的，递归方法很繁琐，能不能用迭代的方法去实现呢？答案很显然想到用**栈**！！

栈是一种后进先出的数据结构，先把root送入栈中，把它的数值放入结果中，然后需要把它的所有子节点**逆序**放入栈中。为什么是逆序？因为后进先出啊！我们需要在下一轮遍历它的最左孩子！

时间复杂度是O(N)，空间复杂度是O(N).

Python代码如下：

```python3
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        stack = []
        stack.append(root)
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
        return res
```

C++代码如下：

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> res;
        if (!root) return res;
        stack<Node*> s;
        s.push(root);
        while (!s.empty()) {
            Node* node = s.top(); s.pop();
            if (!node) continue;
            res.push_back(node->val);
            for (int i = node->children.size() - 1; i >= 0; --i) {
                s.push(node->children[i]);
            }
        }
        return res;
    }
};
```

## 日期

2018 年 7 月 12 日 —— 天阴阴地潮潮，已经连着两天这样了
2018 年 11 月 5 日 —— 打了羽毛球，有点累
2019 年 9 月 20 日 —— 是选择中国互联网式加班？还是外企式养生？

  [1]: https://leetcode.com/static/images/problemset/NaryTreeExample.png
