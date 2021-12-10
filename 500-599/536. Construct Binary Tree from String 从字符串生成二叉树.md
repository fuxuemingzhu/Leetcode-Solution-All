- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/construct-binary-tree-from-string/

## 题目描述

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
Note:
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".



## 题目大意

判断一个多边形是不是凸多边形。

## 解题方法

### 统计字符串出现的次数

看到括号匹配，大部分做法当然是用栈来解决，其实可以直接用统计的方法完成。

即从左向右统计括号出现的次数count，如果是`'('`则增加1，如果是`')'`则减小1，如果count == 0了，说明已经完成了一个括号匹配。

这个题中的格式是`root(left)(right)`，最多只会出现两个完美匹配的外部括号，分别找出两个左括号的位置first和second，然后使用剪切字符串并递归生成左右孩子。

C++代码如下：

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* str2tree(string s) {
        if (s.empty()) return nullptr;
        TreeNode* root = new TreeNode(s[0]);
        int cnt = count(s.begin(), s.end(), '(');
        int first = -1;
        int second = -1;
        int count = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                count ++;
                if (count == 1) {
                    if (first == -1)
                    first = i;
                else
                    second = i;
                }
            } else if (s[i] == ')') {
                count --;
            }
        }
        if (first == -1) {
            root->val = atoi(s.c_str());
        } else if (second == -1) {
            root->val = atoi(s.substr(0, first).c_str());
            root->left = str2tree(s.substr(first + 1, s.size() - first));
        } else {
            root->val = atoi(s.substr(0, first).c_str());
            root->left = str2tree(s.substr(first + 1, second - first));
            root->right = str2tree(s.substr(second + 1, s.size() - second));
        }
        return root;
    }
};
```

## 日期

2019 年 9 月 20 日 —— 是选择中国互联网式加班？还是外企式养生？


  [1]: https://assets.leetcode.com/uploads/2018/10/13/polygon_convex.png
  [2]: https://assets.leetcode.com/uploads/2018/10/13/polygon_not_convex.png
