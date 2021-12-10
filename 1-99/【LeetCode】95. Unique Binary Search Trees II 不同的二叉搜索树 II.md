# 【LeetCode】95. Unique Binary Search Trees II 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/unique-binary-search-trees-ii/description/

## 题目描述：

Given an integer n, generate all structurally unique BST's (binary search trees) that store values ``1 ... n``.

Example:

    Input: 3
    Output:
    [
      [1,null,3,2],
      [3,2,null,1],
      [3,1,null,null,2],
      [2,1,3],
      [1,null,2,null,3]
    ]

Explanation:

    The above output corresponds to the 5 unique BST's shown below:
    
       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3

## 题目大意

输出用1--n这几个数字能组成的所有BST.

## 解题方法

这个题目又是基于之前的[96. Unique Binary Search Trees][1]改进版的题目。之前的题目的做法是只用求出有多少组BST即可，做法是卡特兰数。

这个题目难在构造出来。一般构造树都需要递归。从1--n中任意选择一个数当做根节点，所以其左边的数字构成其左子树，右边的数字当做右子树。因为要求出所有的子树，所以当左子树固定的时候，把所有可能的右子树都构成，然后再变换左子树。

这个代码难理解的地方在于left_nodes 和 right_nodes的求法，这个一定要结合递归的终止条件去看，当选择的根节点的值i比left小的时候，那么其实左子树就是空了。如果把这个理解了，那么下面的对左右子树的遍历应该也不难理解。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        return self.generateTreesDFS(1, n)
    
    def generateTreesDFS(self, left, right):
        if left > right:
            return [None]
        res = []
        for i in range(left, right + 1):
            left_nodes = self.generateTreesDFS(left, i - 1)
            right_nodes = self.generateTreesDFS(i + 1, right)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    res.append(root)
        return res
```

## 日期

2018 年 6 月 22 日 ———— 这周的糟心事终于完了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79367789