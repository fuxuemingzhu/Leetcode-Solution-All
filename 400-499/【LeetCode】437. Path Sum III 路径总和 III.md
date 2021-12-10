
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/path-sum-iii/#/description][1]


## 题目描述


You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

	root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

	      10
	     /  \
	    5   -3
	   / \    \
	  3   2   11
	 / \   \
	3  -2   1

	Return 3. The paths that sum to 8 are:
	
	1.  5 -> 3
	2.  5 -> 2 -> 1
	3. -3 -> 11

## 题目大意

找到二叉树中从某个顶点向下找的路径中，有多少条等于sum.


## 解题方法

### DFS + DFS

使用DFS解决。dfs函数有两个参数，一个是当前的节点，另一个是要得到的值。当节点的值等于要得到的值的时候说明是一个可行的解。再求左右的可行的解的个数，求和之后是所有的。

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
    public int pathSum(TreeNode root, int sum) {
        if(root == null){
            return 0;
        }
        return dfs(root, sum) + pathSum(root.left, sum) + pathSum(root.right, sum);
    }
    
    public int dfs(TreeNode root, int sum){
        int res = 0;
        if(root == null){
            return res;
        }
        if(root.val == sum){
            res++;
        }
        res += dfs(root.left, sum - root.val);
        res += dfs(root.right, sum - root.val);
        return res;
    }
}
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root: return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    
    def dfs(self, root, sum):
        res = 0
        if not root: return res
        sum -= root.val
        if sum == 0:
            res += 1
        res += self.dfs(root.left, sum)
        res += self.dfs(root.right, sum)
        return res
```

### BFS + DFS

使用BFS找到每个顶点作为起点的情况下，用dfs计算等于sum的路径个数。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        res = [0]
        que = collections.deque()
        que.append(root)
        while que:
            node = que.popleft()
            if not node:
                continue
            self.dfs(node, res, 0, sum)
            que.append(node.left)
            que.append(node.right)
        return res[0]
    
    def dfs(self, root, res, path, target):
        if not root: return
        path += root.val
        if path == target:
            res[0] += 1
        self.dfs(root.left, res, path, target)
        self.dfs(root.right, res, path, target)
```

## 日期

2017 年 5 月 2 日 
2018 年 11 月 20 日 —— 真是一个好天气


  [1]: https://leetcode.com/problems/path-sum-iii/#/description
