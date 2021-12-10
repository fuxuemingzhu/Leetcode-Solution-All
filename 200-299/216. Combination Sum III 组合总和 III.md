
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/combination-sum-iii/description/


## 题目描述：



Find all possible combinations of ``k`` numbers that add up to a number ``n``, given that only numbers from ``1 to 9`` can be used and each combination should be a unique set of numbers.

Note:

1. All numbers will be positive integers.
1. The solution set must not contain duplicate combinations.

Example 1:

	Input: k = 3, n = 7
	Output: [[1,2,4]]

Example 2:

	Input: k = 3, n = 9
	Output: [[1,2,6], [1,3,5], [2,3,4]]


## 题目大意

只是用１～９这几个数字，而且每个数字只能使用一次，要用k个不同的数字组成和为n的组合，问有多少中不同的组合方式。


## 解题方法

### 方法一：DFS

这是这个系列的第三个题，同样使用回溯法去做。这个题的不同之处在于k，n的可变性。所以只有两者同时满足等于零的条件的时候才是满意的结果。另外注意题目中给的范围是1-9的数字，所以缩小了范围。

```python
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(xrange(1, 10), k, n, 0, res, [])
        return res
        
    def dfs(self, nums, k, n, index, res, path):
        if k < 0 or n < 0:
            return 
        elif k == 0 and n == 0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            self.dfs(nums, k - 1, n - nums[i], i + 1, res, path + [nums[i]])
```

### 方法二：回溯法

使用回溯法，方法和39题基本一样，唯一的区别是这个题不允许数字多次使用，所以每次循环开始的时候，都要比上一轮大1.

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> res;
        helper(res, {}, k, n, 0);
        return res;
    }
    void helper(vector<vector<int>>& res, vector<int> path, int k, int n, int start) {
        if (n < 0) return;
        if (k == 0 && n == 0) res.push_back(path);
        for (int i = start + 1; i <= 9; i ++) {
            path.push_back(i);
            helper(res, path, k - 1, n - i, i);
            path.pop_back();
        }
    }
};
```

## 日期

2018 年 2 月 21 日 
2018 年 12 月 20 日 —— 感冒害的我睡不着
