- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)


---
@[TOC](目录)

题目地址：https://leetcode.com/problems/subsets/description/


## 题目描述

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,

	If nums = [1,2,3], a solution is:
	
	[
	  [3],
	  [1],
	  [2],
	  [1,2,3],
	  [1,3],
	  [2,3],
	  [1,2],
	  []
	]

## 题目大意

给了输入数组，返回这个数组的所有能够成的子集。

## 解题方法

### 递归

先要找出一个数组全部的子集，可以从题目给的实例中找出答案。我们发现这个实例就是从数组中的每个数字都有`用`和`不用`两个状态。

因此可以写两个递归，分别表示用和不用当前元素的情况下，后续的递归结果。当index到达数组结尾的时候，就把路径path放入结果中就好了。

C++代码如下：

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        dfs(res, {}, nums, 0);
        return res;
    }
    void dfs(vector<vector<int>>& res, vector<int> path, vector<int>& nums, int index) {
        if (index >= nums.size()) {
            res.push_back(path);
            return;
        }
        dfs(res, path, nums, index + 1);
        path.push_back(nums[index]);
        dfs(res, path, nums, index + 1);
    }
};
```

上面的递归解法是当前元素用或者不用两种状态，另外一种递归解法是当前的元素一定使用，然后递归把后面的元素是否选择一些放入当前元素后面。

递归最重要的是明白递归函数的意义。下面代码的`dfs()`函数，就是在当前index元素使用的情况下，从nums的index后面抽取0个或者全部数字放入path的后面，注意这个for循环，意义是当前元素如果使用，后面的那个元素从哪里开始，也就决定了后面的数字选择多少个。

python代码如下：

```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, res, [])
        return res
    
    def dfs(self, nums, index, res, path):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i + 1, res, path + [nums[i]])
```

### 回溯法

C++解法，同样的也是回溯法。

和上面的python递归解法有点类似，不过称其为回溯法是因为path是传的引用，这样path需要我们自己维护，添加元素弹出元素操作分别在递归函数的前后执行，从而达到了当前元素使用完成之后，进行回溯的效果。

C++代码如下：

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        helper(nums, res, path, 0);
        return res;
    }
    void helper(const vector<int>& nums, vector<vector<int>>& res, vector<int>& path, int start) {
        res.push_back(path);
        for (int i = start; i < nums.size(); i ++) {
            path.push_back(nums[i]);
            helper(nums, res, path, i + 1);
            path.pop_back();
        }
    }
};
```

## 日期

2018 年 2 月 24 日 
2018 年 12 月 20 日 —— 感冒害的我睡不着
2019 年 9 月 25 日 —— 做梦都在秋招，这个秋天有毒
