
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/construct-string-from-binary-tree/description/][1]


## 题目描述

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:

    Input: Binary tree: [1,2,3,4]
           1
         /   \
        2     3
       /    
      4     
    
    Output: "1(2(4))(3)"

    Explanation: Originallay it needs to be "1(2(4)())(3()())", 
    but you need to omit all the unnecessary empty parenthesis pairs. 
    And it will be "1(2(4))(3)".

Example 2:

    Input: Binary tree: [1,2,3,null,4]
           1
         /   \
        2     3
         \  
          4 
    
    Output: "1(2()(4))(3)"
    
    Explanation: Almost the same as the first example, 
    except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

## 题目大意

把二叉树转换成字符串，形式是节点值（左子树形式）（右子树形式），其中左子树形式和右子树形式也是同样的形式。注意，有个省略规则，当右子树为空可以省略，或者当左右子树都为空都可以省略。

## 解题方法

### 方法一：先序遍历

题目中也说了，这个是个前序遍历。难点在于括号存在不存在的问题。有以下思路：

1. 对于左子树，如果左孩子或者右孩子存在，那么左子树一定有括号；如果左右子树都不存在，那么为空字符串
2. 对于右子树，如果右子树存在，则是有括号的；如果有子树不存在，那么就是空字符串；
3. 最后的结果是根节点的值加上左右子树的字符串

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t : return ''
        subleft = '({})'.format(self.tree2str(t.left)) if t.left or t.right else ''
        subright = '({})'.format(self.tree2str(t.right)) if t.right else ''
        return '{}{}{}'.format(t.val, subleft, subright)
```

## 日期

2018 年 1 月 21 日 
2018 年 11 月 11 日 —— 剁手节快乐

  [1]: https://leetcode.com/problems/construct-string-from-binary-tree/description/
