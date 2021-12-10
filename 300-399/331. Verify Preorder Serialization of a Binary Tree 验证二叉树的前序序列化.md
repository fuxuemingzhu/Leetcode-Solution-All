# 【LeetCode】331. Verify Preorder Serialization of a Binary Tree 解题报告（Python）

标签： LeetCode

---

题目地址：https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/

## 题目描述：

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.
    
         _9_
        /   \
       3     2
      / \   / \
     4   1  #  6
    / \ / \   / \
    # # # #   # #

For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

    Example 1:
    "9,3,4,#,#,1,#,#,2,#,6,#,#"
    Return true
    
    Example 2:
    "1,#"
    Return false
    
    Example 3:
    "9,#,#,1"
    Return false



## 题目大意

给了一个先序遍历，判断能不能构成合法的二叉树。这个字符串中，#表示空节点。

## 解题方法

我们的思路应该是这样的：判断一个二叉树是否合法的情况，那么应该是个递归或者循环问题。那么解决问题的思路是从顶部向下分析还是从底下向顶部分析呢？正确的结果应该是从二叉树的底部向上进行分析，因为我们可以通过#号判断是否是空节点，然后判断最底下的叶子节点是否含有两个空孩子的方式，循环向上解决这个问题。

所以这个题的思路就很明了了：用一个栈，从字符串的左侧向右依次进栈，如果满足栈的后三位是``数字，#，#``的模式时，说明可以构成合法的叶子节点，把这个叶子节点换成#号，代表空节点，然后继续遍历。最后应该只剩下一个#，那么就是一个合法的二叉树。

    如：”9,3,4,#,#,1,#,#,2,#,6,#,#” 遇到x # #的时候，就把它变为 #
    
    模拟一遍过程：
    
    9,3,4,#,# => 9,3,# 继续读
    9,3,#,1,#,# => 9,3,#,# => 9,# 继续读
    9,#2,#,6,#,# => 9,#,2,#,# => 9,#,# => #

```python
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        for node in preorder.split(','):
            stack.append(node)
            while len(stack) >= 3 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
                stack.pop(), stack.pop(), stack.pop()
                stack.append('#')
        return len(stack) == 1 and stack.pop() == '#'
```

方法二：

这个方法还是第一次使用：看出度和入度的差。

我们知道一个树（甚至图），所有节点的入度之和等于出度之和。那么可以根据这个条件进行有效性的判断。

对于二叉树，我们把空的地方也作为叶子节点（如题目中的#），那么有

1. 所有的非空节点提供2个出度和1个入度（根除外）
1. 所有的空节点但提供0个出度和1个入度

我们在遍历的时候，计算diff = outdegree – indegree. 当一个节点出现的时候，diff – 1，因为它提供一个入度；当节点不是#的时候，diff+2(提供两个出度) 如果序列式合法的，那么遍历过程中diff >=0 且最后结果为0.

这里解释一下为什么diff的初始化为1.因为，我们加入一个非空节点时，都会先减去一个入度，再加上两个出度。但是由于根节点没有父节点，所以其入度为0，出度为2.因此diff初始化为1，是为了再加入根节点的时候，先减去一个入度，再加上两个出度，正好应该是2.

```python
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        diff = 1
        for node in nodes:
            diff -= 1
            if diff < 0:
                return False
            if node != '#':
                diff += 2
        return diff == 0
```

参考：https://www.hrwhisper.me/leetcode-verify-preorder-serialization-of-a-binary-tree/

## 日期

2018 年 3 月 13 日 