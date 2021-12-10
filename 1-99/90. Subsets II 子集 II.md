- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)


---
@[TOC](目录)

题目地址：https://leetcode.com/problems/subsets-ii/description/

## 题目描述

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,

    If nums = [1,2,2], a solution is:
    
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]
    
## 题目大意

找出一个可能含有重复元素的所有子集。

## 解题方法
### 递归

第[【LeetCode】78. Subsets 解题报告][1]是一个不含重复元素的题。

递归最重要的是明白递归函数的意义。下面代码的dfs()函数，就是在当前index元素使用的情况下，从nums的index后面抽取0个或者全部数字放入path的后面，注意这个for循环，意义是当前元素如果使用，后面的那个元素从哪里开始，也就决定了后面的数字选择多少个。

这个题含有重复元素，需要先排序使重复元素放到一起。我们在进行循环的时候加入一个判断，即新加入的元素是否和刚刚加入的元素相同，如果相同就不加入了。这样就可以屏蔽掉了重复元素的问题。

Python代码如下：

代码：

```python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, 0, res, [])
        return res
        
    def dfs(self, nums, index, res, path):
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, res, path + [nums[i]])
```

### 回溯法

叫做回溯法是因为path是传的引用，这样path需要我们自己维护，添加元素、弹出元素操作分别在递归函数的前、后执行，从而达到了当前元素使用完成之后，进行回溯的效果。

同样地，在for循环内部判断一下这个起始位置的元素是不是和前面的那个元素是一样的，如果一样就不能以这个元素作为起始了。

C++代码如下：

```cpp
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> path;
        backtrack(res, path, nums, 0);
        return res;
    }
    void backtrack(vector<vector<int>>& res, vector<int>& path, vector<int>& nums, int index) {
        if (index > nums.size()) return;
        res.push_back(path);
        for (int i = index; i < nums.size(); ++i) {
            if (i != index && nums[i] == nums[i - 1]) continue;
            path.push_back(nums[i]);
            backtrack(res, path, nums, i + 1);
            path.pop_back();
        }
    }
};
```

## 日期

2018 年 4 月 2 日 —— 要开始准备ACM了
2018 年 12 月 21 日 —— 一周就要过去了
2019 年 9 月 25 日 —— 做梦都在秋招，这个秋天有毒

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79359540
