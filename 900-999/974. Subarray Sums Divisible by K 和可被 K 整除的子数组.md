
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/subarray-sums-divisible-by-k/


## 题目描述

Given an array ``A`` of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by ``K``.

 

Example 1:
    
    Input: A = [4,5,0,-2,-3,1], K = 5
    Output: 7
    Explanation: There are 7 subarrays with a sum divisible by K = 5:
    [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1. 1 <= A.length <= 30000
1. -10000 <= A[i] <= 10000
1. 2 <= K <= 10000

## 题目大意

在一个数组中有多少个连续子数组的和，恰好能被K整除。

## 解题方法

### 动态规划

定义DP数组，其中dp[i]代表以i结尾的能被K整除的子数组的最多个数。既然要求子数组的和，那么我们知道，肯定需要求数组累积和sums的。那么，对于sums每个位置i向前找，找到第一个差能被K整除的位置j，就停止即可。此时的dp[i] = dp[j] + 1. 题目要求的结果是sum(dp).

下面分析这个递推公式怎么来的。dp[j]表示以j位置结尾的子数组，该子数组的和能被K整除。那么当我们寻找到(sums[i] - sums[j]) % K == 0的时候，说明子数组sums[i, j]也能被K整除，那么，以i结尾的所有子数组个数等于以j结尾的子数组后面拼接上[i,j]子数组，加上[i,j]子数组.即dp[i] = dp[j] + 1。那么，为什么会break掉呢？这是因为，我们dp的状态是以i结尾的子数组的最大个数，再往前搜索则不是最大的。

这个代码的时间复杂度是O(N^2)的，也AC了，我认为主要是break的功劳。

c++代码如下：

```cpp
class Solution {
public:
    int subarraysDivByK(vector<int>& A, int K) {
        const int N = A.size();
        vector<int> sums = {0};
        for (int a : A)
            sums.push_back(a + sums.back());
        vector<int> dp(N + 1, 0);
        int res = 0;
        for (int i = 1; i <= N; ++i) {
            for (int j = i - 1; j >= 0; --j) {
                if ((sums[i] - sums[j]) % K == 0) {
                    dp[i] = dp[j] + 1;
                    res += dp[i];
                    break;
                }
            }
        }
        return res;
    }
};
```

### 前缀和求余

其实，在上面这个做法当中，我们对于每个i位置都向前去查询``(sums[i] - sums[j]) % K == 0``的j，找到之后立马break，这一步可以更加简化，只要我们使用前缀和，并且相同余数的和。

如果``(sums[i] - sums[j]) % K == 0``，说明sums[i]和sums[j]都是K的倍数，所以得出``sums[i] % K == sums[j] % K``。也就是说，我们找到``sums[i] % K``这个数字的之前的状态即可。根据上面的DP，我们知道只需要找到最后的这个结果，然后break掉的意思就是，我们只需要保存最后的状态。总之，我们需要维护一个hash_map，保存每个余数在每个位置前面，出现的次数。

刚开始时，m[0] = 1，即假设0的出现了1次。然后遍历每个数字，对前缀和+当前数字再求余，在C++里面由于负数求余得到的是负数，所以要把负余数+K才行。把字典中保存的之前的结果累计，就是结果。

想了很久为什么是加的当前数字之前的结果，而不是现在的结果？这是因为，我们当前再次遇到了这个数字，才能说明形成了一个同余的区间。所以加的永远是前面的余数存在了多少次。这样，当某个余数只出现了1次时，并不会计入到结果里。

```cpp
class Solution {
public:
    int subarraysDivByK(vector<int>& A, int K) {
        unordered_map<int, int> m;
        int preSum = 0;
        int res = 0;
        m[0] = 1;
        for (int a : A) {
            preSum = (preSum + a) % K;
            if (preSum < 0) preSum += K;
            res += m[preSum]++;
        }
        return res;
    }
};
```


## 日期

2019 年 1 月 13 日 —— 时间太快了


  [1]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png
  [2]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png
