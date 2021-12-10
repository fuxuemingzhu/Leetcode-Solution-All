作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/matchsticks-to-square/description/

## 题目描述

Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:

    Input: [1,1,2,2,2]
    Output: true
    
    Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
    
Example 2:
    
    Input: [3,3,3,3,4]
    Output: false
    
    Explanation: You cannot find a way to form a square with all the matchsticks.

Note:

1. The length sum of the given matchsticks is in the range of 0 to 10^9.
1. The length of the given matchstick array will not exceed 15.
    
## 题目大意

题目很长，讲的是卖火孩的小女柴，把火柴拼在一起能不能得到一个正方形。当然火柴是不能折断的，而且要全部都用上。

## 解题方法

### 回溯法

这个题目很长，其实就一句话：能不能把一组数字分成4组，每组的和是相同的。

我们注意到题目给出的数组长度最多只有15个，基本上可以使用O(N!)的时间复杂度去解决。所以我们可以直接使用回溯法。回溯的思路是先设置好4条边，然后把每一个火柴看看能不能放到4条边中的一个去，如果可以的话就继续向后扫描，直到所有的火柴全部用上为止。

同样使用[416. Partition Equal Subset Sum][1]的方法，也就是在使用记录四组的和的方式，进行遍历的时候保存各个组的和，如果不能满足就把这个数字再加上，相当于跳过这个数字的方式。最后结束的条件就是所有的数字全部都用完了，因为如果用完了，说明我们把所有的火柴都放到了4条边中的一个，所以得到每组都满足我们条件的结论。

Python代码：

```python
class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 4: return False
        _sum = sum(nums)
        div, mod = divmod(_sum, 4)
        if mod != 0 or max(nums) > _sum / 4: return False
        nums.sort(reverse = True)
        target = [div] * 4
        return self.dfs(nums, 0, target)
        
    def dfs(self, nums, index, target):
        if index == len(nums): return True
        num = nums[index]
        for i in range(4):
            if target[i] >= num:
                target[i] -= num
                if self.dfs(nums, index + 1, target): return True
                target[i] += num
        return False
```

C++代码如下：

```cpp
class Solution {
public:
    bool makesquare(vector<int>& nums) {
        if (nums.size() < 4) return false;
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % 4 != 0)
            return false;
        int edge = sum / 4;
        vector<int> target(4, edge);
        return helper(nums, 0, target);
    }
    bool helper(vector<int>& nums, int index, vector<int>& target) {
        const int N = nums.size();
        if (index == N) return true;
        int num = nums[index];
        for (int i = 0; i < 4; ++i) {
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

## 日期

2018 年 4 月 2 日 —— 要开始准备ACM了
2019 年 2 月 23 日 —— 没时间了

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79787425
