
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/path-sum/#/description][1]


## 题目描述

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

## 题目大意

从根节点到叶子节点是否存在一条路径，它的所有节点的和等于target.

## 解题方法

### DFS

这个题要背下来！！

首先是 DFS 解法，该解法的想法是一直向下找到**叶子节点**，如果到**叶子节点**时`sum == 0`，说明找到了一条符合要求的路径。

我自己第一遍做的时候犯了一个错误，把递归函数写成了下面的解法：

```python
def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if not root:
        return sum == 0
    return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
```

这种代码的错误在，**没有判断 root 是否为叶子节点**。比如 root 为空的话，题目的意思是要返回 False 的，而上面的代码会返回 sum == 0。又比如，对于测试用例 树为`[1,2]`, sum = 0 时，上面的结果也会返回为 True，因为对于上述代码，只要左右任意一个孩子的为空时 sum == 0 就返回 True 。

当题目中提到了**叶子节点**时，正确的做法一定要同时判断节点的**左右子树同时为空**才是叶子节点。

Python 代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
```

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
    public boolean hasPathSum(TreeNode root, int sum) {
        if(root == null){
            return false;
        }
        if(root.left == null && root.right == null){
            return root.val == sum;
        }
        return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
        
    }
}
```

### 回溯

这里的回溯指 利用 DFS 找出从根节点到叶子节点的所有路径，只要有任意一条路径的 和 等于 sum，就返回 True。

下面的代码并非是严格意义上的回溯法，因为没有重复利用 path 变量。

Python 代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        res = []
        return self.dfs(root, sum, res, [root.val])
        
    def dfs(self, root, target, res, path):
        if not root: return False
        if sum(path) == target and not root.left and not root.right:
            return True
        left_flag, right_flag = False, False
        if root.left:
            left_flag = self.dfs(root.left, target, res, path + [root.left.val])
        if root.right:
            right_flag = self.dfs(root.right, target, res, path + [root.right.val])
        return left_flag or right_flag
```


### BFS

BFS 使用 **队列** 保存遍历到每个节点时的**路径和**，如果该节点恰好是叶子节点，并且 路径和 正好等于 sum，说明找到了解。

Python 代码如下：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        que = collections.deque()
        que.append((root, root.val))
        while que:
            node, path = que.popleft()
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                que.append((node.left, path + node.left.val))
            if node.right:
                que.append((node.right, path + node.right.val))
        return False
```

### 栈

除了上面的 队列 解法以外，也可以使用 **栈**，同时保存节点和到这个节点的路径和。但是这个解法已经不是 BFS。因为会优先访问 后进来 的节点，导致会把根节点的右子树访问结束之后，才访问左子树。

可能会有朋友好奇很少见到这种写法，为什么代码可行？答案是：栈中同时保存了 `(节点，路径和)`，也就是说只要能把所有的节点访问一遍，那么就一定能找到正确的结果。无论是用 队列 还是 栈，都是一种 树的遍历 方式，只不过访问顺序有所有不同罢了。

Python 代码如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = []
        stack.append((root, root.val))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                stack.append((node.left, path + node.left.val))
            if node.right:
                stack.append((node.right, path + node.right.val))
        return False
```


## 日期

2017 年 5 月 12 日 
2018 年 6 月 22 日 
2018 年 11 月 24 日 —— 周六快乐
2020 年 7 月 7 日 —— 昨日 A 股涨了5.7%，5 年来的最高单日涨幅

  [1]: https://leetcode.com/problems/path-sum/#/description
