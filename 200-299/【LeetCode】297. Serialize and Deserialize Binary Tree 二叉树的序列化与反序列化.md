# 【LeetCode】297. Serialize and Deserialize Binary Tree 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

## 题目描述：

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

        1
       / \
      2   3
         / \
        4   5

as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.


Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

## 题目大意

序列化，解序列化一棵二叉树。

## 解题方法

和[449. Serialize and Deserialize BST][1]多么的像呀！之前我说，只知道前序遍历是没法确定一个树的，我说的不严谨。如果前序遍历的过程中记录下哪些位置是空节点的话，就是可以确定这棵树的。LeetCode的官方树的构建就是这样的。

因此，我们采用和上题同样的方法，只不过需要把空节点记录下来。然后在反序列化时把它再变成空节点即可。

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
            if not root:
                vals.append('#')
            else:
                vals.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(val for val in data.split())
        def build():
            if vals:
                val = vals.popleft()
                if val == '#':
                    return None
                root = TreeNode(int(val))
                root.left = build()
                root.right = build()
                return root
        return build()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```


## 日期

2018 年 3 月 15 日 --雾霾消散，春光明媚


  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79529337