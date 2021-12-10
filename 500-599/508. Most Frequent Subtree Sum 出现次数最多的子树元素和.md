
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/most-frequent-subtree-sum/description/

## 题目描述

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1

    Input:
    
      5
     /  \
    2   -3
    return [2, -3, 4], since all the values happen only once, return all of them in any order.
    Examples 2
    Input:
    
      5
     /  \
    2   -5
    return [2], since 2 happens twice, however -5 only occur once.

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.



## 题目大意

先找出树的每个节点的值与所有子节点的和，然后找出和中出现频率最大的值。

## 解题方法

按照题目大意的思路，先进行求和遍历，找出所有的节点月其子节点的和，然后使用Counter()找出每个词的频率，返回出现频率最大的值即可。

注意哈，在getSum()函数中，别忘了返回当前求得的和，如果这个忘写了，那么返回的就是None.

Python解法如下：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        vals = []
        def getSum(root):
            if not root:
                return 0
            s = getSum(root.left) + root.val + getSum(root.right)
            vals.append(s)
            # 别忘了返回s
            return s
        getSum(root)
        count = collections.Counter(vals)
        frequent = max(count.values())
        return [x for x, v in count.items() if v == frequent]
```

二刷的思路是这样的，对于每个节点都去一个函数求和，然后用dfs遍历每个节点。这样说来，时间复杂度略高。

统计出每个节点的和之后，需要用字典统计。

第一版代码C++如下：

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
    vector<int> findFrequentTreeSum(TreeNode* root) {
        dfs(root);
        map<int, int> d;
        int most_common = 0;
        for (int s : sums) {
            d[s] ++;
            most_common = max(most_common, d[s]);
        }
        vector<int> res;
        for (auto p : d){
            if (p.second == most_common)
                res.push_back(p.first);
        }
        return res;
    }
private:
    vector<int> sums;
    void dfs(TreeNode* root) {
        if (!root) return;
        dfs(root->left);
        sums.push_back(getSum(root));
        dfs(root->right);
    }
    int getSum(TreeNode* root) {
        if (!root) return 0;
        int l = getSum(root->left);
        int r = getSum(root->right);
        return root->val + l + r;
    }
};
```

然后稍加思索就发现，遍历了两次，所以可以把两个函数只保留一个，代码如下：

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
    vector<int> findFrequentTreeSum(TreeNode* root) {
        getSum(root);
        vector<int> res;
        for (auto p : d)
            if (p.second == most_common)
                res.push_back(p.first);
        return res;
    }
private:
    vector<int> sums;
    int most_common = 0;
    map<int, int> d;
    int getSum(TreeNode* root) {
        if (!root) return 0;
        int l = getSum(root->left);
        int r = getSum(root->right);
        int s = root->val + l + r;
        sums.push_back(s);
        d[s]++;
        most_common = max(most_common, d[s]);
        return s;
    }
};
```

## 日期

2018 年 3 月 4 日 
2018 年 12 月 13 日 —— 时间匆匆，如何才能提高时间利用率？
