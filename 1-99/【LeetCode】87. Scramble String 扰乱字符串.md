
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/scramble-string/description/


## 题目描述

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = ``"great"``:

        great
       /    \
      gr    eat
     / \    /  \
    g   r  e   at
               / \
              a   t

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node ``"gr"`` and swap its two children, it produces a scrambled string ``"rgeat"``.

        rgeat
       /    \
      rg    eat
     / \    /  \
    r   g  e   at
               / \
              a   t

We say that ``"rgeat"`` is a scrambled string of ``"great"``.

Similarly, if we continue to swap the children of nodes ``"eat"`` and ``"at"``, it produces a scrambled string ``"rgtae"``.

        rgtae
       /    \
      rg    tae
     / \    /  \
    r   g  ta  e
           / \
          t   a

We say that ``"rgtae"`` is a scrambled string of ``"great"``.

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

    Input: s1 = "great", s2 = "rgeat"
    Output: true

Example 2:
    
    Input: s1 = "abcde", s2 = "caebd"
    Output: false

## 题目大意

题目是混杂的字符串。一个字符串s1可以表达成一棵二叉树的形式，从而把一棵二叉树的所有叶子节点从左到右遍历一遍就能得到源字符串。现在我们要做一些翻转二叉树的操作，即把某些位置的二叉树进行翻转，这样从左到右的叶子节点又会串成另外一个字符串s2。现在要我们判断给定s1能不能通过翻转某些位置的二叉树形式得到另外一个字符串s2.

## 解题方法

### 递归

这个题某种意义上来说就是让我们来判断两棵二叉树是否能够通过翻转某些子树而互相得到，也就是[951. Flip Equivalent Binary Trees][1]翻转二叉树子节点的题目。这个题不过是把树变成了字符串而已。

这个题的重点之一就是要合理的划分字符串从而形成两棵不同的左右子树，进而对左右子树递归。因为事先不知道在哪里进行分割，所以直接对每个可以划分的位置进行遍历分割。判断是否两个子串能否通过翻转变成相等的时候，需要保证传给函数的子串长度是相同的。因此：

1. s1的[0:i]和s2[0:i]作为左子树，s1[i:N]和s2[i:N]作为右子树
2. s1的[0:i]和s2[N - i:N]作为左子树，s1的[i:N]和s2[0:N-i]作为右子树

其中左子树的两个字符串的长度都是i,右子树的两个字符串的长度都是N - i.如果上面两种情况有一种能够成立，则源字符串s1能够变成s2。

由于使用了递归，所以终止条件一定要写，很简单的对长度是0、长度是1、两个字符串排序之后是否相等进行判断。

Python代码如下：

```python
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        N = len(s1)
        if N == 0: return True
        if N == 1: return s1 == s2
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, N):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            elif self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False
```

C++代码如下：

```cpp
class Solution {
public:
    bool isScramble(string s1, string s2) {
        if (s1.size() != s2.size()) return false;
        const int N = s1.size();
        if (N == 0) return true;
        if (N == 1) return s1 == s2;
        string s1copy = s1;
        string s2copy = s2;
        sort(s1copy.begin(), s1copy.end());
        sort(s2copy.begin(), s2copy.end());
        if (s1copy != s2copy) return false;
        for (int i = 1; i < N; i++) {
            if ((isScramble(s1.substr(0, i), s2.substr(0, i)) && isScramble(s1.substr(i), s2.substr(i))))
                return true;
            if ((isScramble(s1.substr(0, i), s2.substr(N - i)) && isScramble(s1.substr(i), s2.substr(0, N - i))))
                return true;
        }
        return false;
    }
};
```

### 动态规划

待补。


## 日期

2018 年 12 月 11 日 —— 双十一已经过去一个月了，真快啊。。


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/84728645
