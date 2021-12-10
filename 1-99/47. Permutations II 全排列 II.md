
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/permutations-ii/description/

## 题目描述

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,

    [1,1,2] have the following unique permutations:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]

## 题目大意

找出有可能有重复数字的一个数组的所有全排列。

## 解题方法

### 方法一：递归

之前的[【LeetCode】46. Permutations 解题报告](http://blog.csdn.net/fuxuemingzhu/article/details/79363903)是没有重复数字的，这个题有重复数字。我的做法很简单，就是在以前的基础上加了一个判断条件：``path not in res``。这样的做法是在每个path生成之后才去做的判断，因此效率一点都不高。最后竟然也能通过了。

```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(nums, res, [])
        return res
    
    def helper(self, nums, res, path):
        if not nums and path not in res:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.helper(nums[:i] + nums[i+1:], res, path + [nums[i]])
```


### 方法二：回溯法

上面的做法并不是标准的回溯法，标准的回溯法应该不更改nums。下面这个做法是标准的回溯法，需要用到visited来表示哪些位置已经被添加到path中了。

如何去重呢？我们想一想为什么会有重复出现：在这个例子中，我们在第一个1开始的排列中已经取了第二个1的情况；如果在第二个1开始的排列中仍然取第一个1，就有重复了。

所以，我们的做法是先对数组进行排序，保证相等的数字放在一起，然后当我们遇到的不是第一个数字，并且现在的数字和前面的数字相等，同时前面的数字还没有访问过，我们是不能搜索的，需要直接返回。原因是，这种情况下，必须是由前面搜索到现在的这个位置，而不能是由现在的位置向前面搜索。

C++代码如下:

```cpp

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        const int N = nums.size();
        sort(nums.begin(), nums.end());
        vector<bool> visited(N, false);
        vector<vector<int>> res;
        helper(nums, res, {}, visited, 0);
        return res;
    }
    void helper(vector<int>& nums, vector<vector<int>>& res, vector<int> path, vector<bool>& visited, int count) {
        if (count == nums.size()) {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (visited[i]) continue;
            if (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1]) continue;
            visited[i] = true;
            path.push_back(nums[i]);
            helper(nums, res, path, visited, count + 1);
            path.pop_back();
            visited[i] = false;
        }
    }
};
```

## 日期

2018 年 3 月 10 日 
2018 年 12 月 21 日 —— 一周就要过去了

