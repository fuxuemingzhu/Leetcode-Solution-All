
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/combinations/description/

## 题目描述

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

    For example,
    If n = 4 and k = 2, a solution is:
    
    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]


## 题目大意

找出一个数组的所有可能的``组合``。

## 解题方法

### 方法一：递归

这个题要找到组合，组合和排列的不同之处在于组合的数字出现是没有顺序意义的。

剑指offer的做法是找出n个数字中m的数字的组合方法是，把n个数字分成两部分：第一个字符和其他的字符。如果组合中包括第一个字符，那么就在其余字符中找到m-1个组合；如果组合中不包括第一个字符，那么就在其余字符中找到m个字符。所以变成了递归的子问题。

我的做法如下，这个之中用到了if k > len(array)的做法，防止数组过界陷入死循环（其作用主要是对第二个递归而言的）。

```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(range(1, n + 1), k, res, [])
        return res
    
    def helper(self, array, k, res, path):
        if k > len(array):
            return
        if k == 0:
            res.append(path)
        else:
            self.helper(array[1:], k - 1, res, path + [array[0]])
            self.helper(array[1:], k, res, path)
```

### 方法二：回溯法

这样的思想是我们抽取第一个字符，然后从后面n-1个字符中抽出m-1个；抽取第二个字符，再从后面的n-2个字符抽出m-1个……这样循环下去。因为这样的操作每次都是往后进行寻找的，所以不用考虑去重的问题。

```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(range(1, n + 1), k, res, [])
        return res
    
    def helper(self, array, k, res, path):
        if k > len(array):
            return
        if k == 0:
            res.append(path)
        else:
            for i in range(len(array)):
                self.helper(array[i + 1:], k - 1, res, path + [array[i]])
```

C++代码如下：

```cpp
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<int> nums(n, 0);
        for (int i = 1; i <= n; i++) {
            nums[i - 1] = i;
        }
        vector<vector<int>> res;
        helper(nums, res, {}, 0, k);
        return res;
    }
    void helper(const vector<int>& nums, vector<vector<int>>& res, vector<int> path, int start, int remain) {
        if (start > nums.size()) return;
        if (remain == 0) {
            res.push_back(path);
            return;
        }
        for (int i = start; i < nums.size(); i++) {
            path.push_back(nums[i]);
            helper(nums, res, path, i + 1, remain - 1);
            path.pop_back();
        }
    }
};
```


## 日期

2018 年 3 月 11 日 
2018 年 12 月 20 日 —— 感冒害的我睡不着

