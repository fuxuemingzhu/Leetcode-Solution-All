
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/partition-equal-subset-sum/description/

## 题目描述

Given a ``non-empty`` array containing ``only positive integers``, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

1. Each of the array element will not exceed 100.
1. The array size will not exceed 200.


Example 1:
        
        Input: [1, 5, 11, 5]
        
        Output: true
        
        Explanation: The array can be partitioned as [1, 5, 5] and [11].
        
Example 2:
        
        Input: [1, 2, 3, 5]
        
        Output: false
        
        Explanation: The array cannot be partitioned into equal sum subsets.
    
## 题目大意

判断是否可以把一组数字分成两堆，两堆数字的和相等。

## 解题方法

### DFS

首先要判断所有数字的和是不是偶数，然后我们使用一个长度为2的数组进行保存我们要平分得到的target，这么做是我们可以通过使用-，+两种操作来跳过一些数字。同样是dfs，这里的dfs操作允许跳过某些位置去向下寻找，只要找到一个满足条件的就可以停止。而subsets的题不可以这么做，因为我们要找到所有的可能的答案。因此可以看做是两套模板。

Python代码：

```python
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _sum = sum(nums)
        div, mod = divmod(_sum, 2)
        if mod or max(nums) > div: return False
        nums.sort(reverse = True)
        target = [div] * 2
        return self.dfs(nums, 0, target)
    
    def dfs(self, nums, index, target):
        for i in range(2):
            if target[i] >= nums[index]:
                target[i] -= nums[index]
                if target[i] == 0 or self.dfs(nums, index + 1, target): return True
                target[i] += nums[index]
        return False
```

### 动态规划

这个题其实是个0-1背包问题。所以可以使用动态规划求解。

求和是必须的，目标target等于和的一半。如果和不是偶数的话则一定不可能由数组构成出来，直接返回false.

首先定义dp数组为dp[i][j]，其意义是使用前i个数字的和能不能构成整数j。我们需要把每个位置都进行遍历，同时也要对0~target之间的所有正整数进行遍历。很显然，状态转移的方程是，遍历到i位置时能不能构成target = 前面的数字的和能够成target  || 前面的数字能构成target - nums[i]。这两个状态分别是选不选取nums[i]的两种情况，如果有一种情况成立即可。

状态转移方程如下：

	dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i]]

这个题的技巧和难点就在于，需要把数组的每个数字的和当做dp的一个状态，这个是很少见的，其实题目给的有提示：数组的每个数都是整数，并且数字不会超过200，数组长度不超过100，这些说明了数字的和不会太大不会太多。


具体C++代码如下：

```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        const int N = nums.size();
        int target = sum >> 1;
        if (sum % 2 != 0) return false;
        //dp[i][j] means whether we can sum to j using first i numbers.
        vector<vector<bool>> dp(N + 1, vector<bool>(sum + 1, false));
        // every number can build number 0.
        for (int i = 0; i <= N; ++i) {
            dp[i][0] = true;
        }
        // but for position 0, it can build number nothing.
        for (int j = 1; j <= target; ++j) {
            dp[0][j] = false;
        }
        // anyway, position 0 can build number 0.
        dp[0][0] = true;
        for (int i = 1; i <= N; ++i) {
            for (int j = 0; j <= target; ++j) {
                if (j >= nums[i - 1])
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i - 1]];
                else
                    dp[i][j] = dp[i - 1][j];
            }
        }
        return dp[N][target];
    }
};
```

从上面的代码中可以看出，每个位置的状态只与其前面位置的状态有关，所以可以做``状态压缩``节约空间复杂度。

只使用一维dp数组，dp[j]表示从数组中任意取数字的和能不能构成j。状态转移方程就是忽略掉二维数组的第一个维度即可，即：

	dp[j] = dp[j] || dp[j - nums[i]]

还要说一下，为什么需要从后向前更新dp，这是因为每个位置依赖与前面的一个位置加上nums[i]，如果我们从前向后更新的话，那么dp[i - 2]会影响dp[i - 1]，然后dp[i - 1]接着影响dp[i]，即同样的一个nums[i]被反复使用了多次，结果肯定是不正确的。但是从后向前更新就没有问题了。

那么结合上面的分析，可以写出如下代码：

```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        const int N = nums.size();
        if (sum % 2 != 0) return false;
        int target = sum >> 1;
        vector<bool> dp(sum + 1, false);
        dp[0] = true;
        for (int num : nums) {
            for (int j = target; j >= num; --j) {
                dp[j] = dp[j] || dp[j - num];
            }
        }
        return dp[target];
    }
};
```

## 日期

2018 年 4 月 2 日 —— 要开始准备ACM了
2019 年 1 月 8 日 —— 别熬夜，我都开始有黑眼圈了。。

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79359540
