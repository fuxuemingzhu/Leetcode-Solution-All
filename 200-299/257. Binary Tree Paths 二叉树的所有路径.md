
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

---

题目地址：[https://leetcode.com/problems/binary-tree-paths/#/description][1]


## 题目描述


Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

	Input:
	
	   1
	 /   \
	2     3
	 \
	  5
	
	Output: ["1->2->5", "1->3"]
	
	Explanation: All root-to-leaf paths are: 1->2->5, 1->3
    
## 题目大意

但引出所有的从根节点到叶子节点的路径。

## 解题方法

### 递归

把二叉树的从根节点到叶子节点的每条路径都打印出来，实用的方法就是很简单的递归调用。如果是叶子就把这个路径保存到list中，如果不是叶子就把这个节点的值放入到path中，然后再继续调用，直到达到叶子节点为止。

我用StringBuilder的结果会糅杂在一起，就不能用，也没想明白为什么= =

java版本：

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
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> ans = new ArrayList<String>();
        if(root != null){
            searchNode(root, "", ans);
        }
        return ans;
    }
    
    public void searchNode(TreeNode root, String path, List<String> ans){
        if(root.left == null && root.right == null){
            ans.add(path + root.val);
        }
        if(root.left != null){
            searchNode(root.left, path + root.val + "->", ans);
        }
        if(root.right != null){
            searchNode(root.right, path + root.val + "->", ans);
        }
    }
}
```

===========二刷

把path作为字符串，res作为数组保存字符串。一般递归都可以这么写的。

python版本：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        self.dfs(root, res, '' + str(root.val))
        return res
        
    def dfs(self, root, res, path):
        if root.left == None and root.right == None:
            res.append(path)
        if root.left != None:
            self.dfs(root.left, res, path + '->' + str(root.left.val))
        if root.right != None:
            self.dfs(root.right, res, path + '->' + str(root.right.val))
```

### 迭代

使用迭代的话，大家都知道需要用一个栈，那么感觉就是个模板题了，而且和上面的递归做法基本是一样的了。


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        stack = []
        res = []
        stack.append((root, str(root.val)))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
        return res
```

## 日期

2017 年 5 月 6 日 
2018 年 2 月 25 日
2018 年 11 月 19 日 —— 周一又开始了

  [1]: https://leetcode.com/problems/binary-tree-paths/#/description
