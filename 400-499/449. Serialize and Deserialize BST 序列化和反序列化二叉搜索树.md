# 【LeetCode】449. Serialize and Deserialize BST 解题报告（Python） 

标签： LeetCode

---

题目地址：https://leetcode.com/problems/serialize-and-deserialize-bst/description/

## 题目描述：

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a ```binary search tree```. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

``The encoded string should be as compact as possible.``

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.



## 题目大意

用字符串编码一个BST，并实现解编码成BST的函数。

## 解题方法

看到BST，就一定想到了一个性质： BST的中序遍历是有序的。但我们又知道，只知道树的一种遍历方式，是没法确定这个树的，BST也不例外。

因此，这个题采用前序遍历的方式，这样，遍历得到的第一个数组就是BST的根节点，数组后面的这些数中比根节点的值小的是根节点的左子树，比根节点值大的是根节点的右子树（BST的最重要性质）。

因此，重要结论：``BST的前序遍历能唯一的确定一颗BST``

解编码过程是通过一个队列进行操作。其实也可以是list，不过队列的效率更高。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        vals = []
        def preOrder(root):
            if root:
                vals.append(root.val)
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return ' '.join(map(str, vals))

    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(int(val) for val in data.split())
        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                root = TreeNode(val)
                root.left = build(minVal, val)
                root.right = build(val, maxVal)
                return root
        return build(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

## 日期

2018 年 3 月 12 日 
