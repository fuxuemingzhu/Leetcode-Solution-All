
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/subtree-of-another-tree/#/description][1]


## 题目描述

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:

    Given tree s:
    
         3
        / \
       4   5
      / \
     1   2
    Given tree t:
       4 
      / \
     1   2
    Return true, because t has the same structure and node values with a subtree of s.

Example 2:

    Given tree s:
    
         3
        / \
       4   5
      / \
     1   2
        /
       0
    Given tree t:
       4
      / \
     1   2
    Return false.

## 题目大意

判断 t 是不是 s 的一个子树。

## 解题方法

### 方法一：先序遍历
先序遍历把树转成字符串，判断是否为子串。

在当节点为空的时候给一个“#”表示，这样就能表示出不同的子树，因此只需要遍历一次就能得到结果。每次遍历到树的结尾的时候能够按照#区分，另外每个树的节点值之间用","分割。
在提交的时候又遇到一个问题，就是12和2的结果是一样的，那么我在每个遍历结果的开头位置再加上一个逗号就完美解决了。
另外注意，不要判断左右子树不为空再去遍历树，这样就不能添加上“#”了。

Java 代码如下：

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
    StringBuilder spre = new StringBuilder();
    StringBuilder tpre = new StringBuilder();
    public boolean isSubtree(TreeNode s, TreeNode t) {
        preOrder(s, spre.append(","));
        preOrder(t, tpre.append(","));
        System.out.println(spre.toString());
        System.out.println(tpre.toString());
        return spre.toString().contains(tpre.toString());
    }
    public void preOrder(TreeNode root, StringBuilder str){
        if(root == null){
            str.append("#,");
            return;
        }
        str.append(root.val).append(",");
        preOrder(root.left, str);
        preOrder(root.right, str);
    }
}
```

### 方法二：DFS + DFS

要判断一个树 t 是不是另外一个树 s 的子树，那么可以判断 t 是否和树 s 的任意子树是否相等。那么就和[100. Same Tree][2]挺像了。所以这个题的做法就是在判断两棵树是否相等的基础上，添加上任意子树是否相等的判断。


判断 t 是否为 s 的子树的方式是：

1. 当前两棵树相等；
2. 或者，s 的左子树和 t 相等
3. 或者，s 的左子树和 t 相等

这三个条件是**或**的关系。

注意，判断两个树是否相等是**与**的关系，即：

1. 当前两个树的根节点值相等
2. 并且，s 的左子树和 t 的左子树相等
3. 并且，s 的左子树和 t 的右子树相等


判断是否是子树与是否是相同的树的代码简直是对称美啊~

Python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
```

### 方法三：BFS + DFS

因为 t 的根节点可能对应着 s 中的任意一个节点，那么我们使用 BFS 来遍历 s 的每个节点，然后对每个节点进行判断是否与 t 相等。

Python代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or not t:
            return False
        que = collections.deque()
        que.append(s)
        while que:
            node = que.popleft()
            if not node:
                continue
            if self.isSameTree(node, t):
                return True
            que.append(node.left)
            que.append(node.right)
        return False
        
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
```

## 日期

2017 年 5 月 9 日 
2018 年 10 月 19 日 —— 自古逢秋悲寂寥，我言秋日胜春朝
2018 年 11 月 21 日 —— 又是一个美好的开始
2020年 5 月 7 日 —— 先把工作忙完，再搞其他的

  [1]: https://leetcode.com/problems/subtree-of-another-tree/#/description
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/51285076
