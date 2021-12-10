作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/house-robber-ii/description/

## 题目描述：

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are ``arranged in a circle``. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and ``it will automatically contact the police if two adjacent houses were broken into on the same night``.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight ``without alerting the police``.

Example 1:

    Input: [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
                 because they are adjacent houses.

Example 2:

    Input: [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                 Total amount you can rob = 1 + 3 = 4.


## 题目大意

这个是[198. House Robber][1]的拓展。本题目里面的房间是一个环的，也就是说第一个房子和最后一个房子是相邻的。在这种情况下，相邻的两个房子不能一起偷，求能偷到的金额的最大值。

## 解题方法

这个题多了环的条件，在这个约束下就多了个不同时偷第一个和最后一个就可以了。所以，两种偷的情况：第一种不偷最后一个房间，第二种不偷第一个房间，求这两种偷法能获得的最大值。所以只多了一个切片的过程。

状态转移方程仍然是：

    dp[0] = num[0] （当i=0时） 
    dp[1] = max(num[0], num[1]) （当i=1时） 
    dp[i] = max(num[i] + dp[i - 2], dp[i - 1]) （当i !=0 and i != 1时）

第三个式子就是当前的房间偷的情况和不偷情况下的最大值。

时间复杂度是O(N)，空间复杂度是O(N). (Beats 98%.)

代码如下：

```python
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        N = len(nums)
        return max(self.rob_range(nums[0 : N - 1]), self.rob_range(nums[1 : N]))
    
    def rob_range(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
```

参考资料：

http://www.cnblogs.com/grandyang/p/4518674.html

## 日期

2018 年 10 月 9 日 ———— 天气骤冷，注意保暖


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/51291936
