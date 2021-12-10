作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

@[TOC](目录)

题目地址：https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/

## 题目描述

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
    
    Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
    Output: True
    
    Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Note:

1. 1 <= k <= len(nums) <= 16.
1. 0 < nums[i] < 10000.

    
## 题目大意

判断一个数组是否可以分成k组，每组的和相等。

## 解题方法

### 回溯法

这是一个套题，和[416. Partition Equal Subset Sum][1]，[473. Matchsticks to Square][2]基本一致的代码，上面的两个题分别是求平分成2份和4份。这个是任意的k份。所以改成了k组数字记录的div，最后看是否能够正好进行平分。

直接使用回溯法即可，这个回溯的要求是恰好把nums的所有数字用过一遍，使得目标数组中恰好有k个相同数字。当所有的数字恰好用完的时候，就是我们平分的时候，即可返回true。题目给出的数字范围只到16，所以本算法时间复杂度是O(N!)，仍然能通过。

这里要证明，为什么只需要判断恰好用完即可返回true。因为我们所有数字的和是确定的，即sum(target) = div * k = sum(nums)。如果我们在每个位置放数字的时候，保证了放置的数字<=该位置的数字，即保证了在最终状态的target[i]>=0。此时有sum(target) >= 0。又已知所有数字恰好用完，所以恰好有sum(target) = 0。故，当所有数字恰好用完时，target的每个位置都是0.

Python代码：

```python
class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or len(nums) < k: return False
        _sum = sum(nums)
        div, mod = divmod(_sum, k)
        if _sum % k or max(nums) > _sum / k: return False
        nums.sort(reverse = True)
        target = [div] * k
        return self.dfs(nums, k, 0, target)
        
    def dfs(self, nums, k, index, target):
        if index == len(nums): return True
        num = nums[index]
        for i in range(k):
            if target[i] >= num:
                target[i] -= num
                if self.dfs(nums, k, index + 1, target): return True
                target[i] += num
        return False
```

C++代码如下：

```cpp
class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        if (nums.size() < k) return false;
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % k != 0) return false;
        vector<int> target(k, sum / k);
        return helper(nums, 0, target);
    }
    
    bool helper(vector<int>& nums, int index, vector<int>& target) {
        if (index == nums.size()) return true;
        int num = nums[index];
        for (int i = 0; i < target.size(); ++i) {
            if (target[i] >= num) {
                target[i] -= num;
                if (helper(nums, index + 1, target))
                    return true;
                target[i] += num;
            }
        }
        return false;
    }
};
```

另外一种Python解法定义的dfs()函数的意义是使用nums[ind:]能不能构成k个和分别为self.target的数字，因为这种做法会反复遍历nums，而不像上面这种做法只用遍历一次，所以这个做法需要用visited数组，表示nums[i]数字是否已经使用过。

```python
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 1: return True
        self.n = len(nums)
        if self.n < k: return False
        total = sum(nums)
        if total % k: return False
        self.target = total / k
        visited = [0] * self.n
        nums.sort(reverse = True)
        def dfs(k, ind, sum, cnt):
            if k == 1: return True
            if sum == self.target and cnt > 0:
                return dfs(k - 1, 0, 0, 0)
            for i in range(ind, self.n):
                if not visited[i] and sum + nums[i] <= self.target:
                    visited[i] = 1
                    if dfs(k, i + 1, sum + nums[i], cnt + 1):
                        return True
                    visited[i] = 0
            return False
        return dfs(k, 0, 0, 0)
```

## 日期

2018 年 4 月 2 日 —— 要开始准备ACM了
2019 年 2 月 24 日 —— 周末又结束了

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79787425
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/79787660
