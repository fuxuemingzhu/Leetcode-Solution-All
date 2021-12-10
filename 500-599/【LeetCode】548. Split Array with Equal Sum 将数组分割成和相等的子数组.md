

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/split-array-with-equal-sum/

## 题目描述

Given an array with n integers, you need to find if there are triplets `(i, j, k)` which satisfies following conditions:

1. `0 < i, i + 1 < j, j + 1 < k < n - 1`
1. Sum of subarrays `(0, i - 1)`, `(i + 1, j - 1)`, `(j + 1, k - 1)` and `(k + 1, n - 1)` should be equal.

where we define that subarray `(L, R)` represents a slice of the original array starting from the element indexed `L` to the element indexed `R`.

Example:

    Input: [1,2,1,2,1,2,1]
    Output: True
    Explanation:
    i = 1, j = 3, k = 5. 
    sum(0, i - 1) = sum(0, 0) = 1
    sum(i + 1, j - 1) = sum(2, 2) = 1
    sum(j + 1, k - 1) = sum(4, 4) = 1
    sum(k + 1, n - 1) = sum(6, 6) = 1

Note:

- `1 <= n <= 2000`.
- Elements in the given array will be in range [-1,000,000, 1,000,000].


## 题目大意

在nums数组中插入三个隔板i,j,k，使得 `(0, i - 1)`, `(i + 1, j - 1)`, `(j + 1, k - 1)` and `(k + 1, n - 1)`的和相等。

## 解题方法

### 暴力

这个题好像没有简单的做法，直接暴力三层循环即可。一个常见的优化就是提前算出从位置0到每个位置的累加和preSum，这样区间[i, j]的和 = preSum[j] - preSum[i - 1];

另外有个case是1000多个0，导致超时，此时需要一个优化：跳过`nums[j] == nums[j-1] == 0`的点。

C++代码如下：

```cpp
class Solution {
public:
    bool splitArray(vector<int>& nums) {
        const int N = nums.size();
        vector<long long> preSum(N, 0);
        long long sum = 0;
        for (int i = 0; i < N; ++i) {
            sum += nums[i];
            preSum[i] = sum;
        }
        for (int i = 1; i < N; ++i) {
            long long sum_0i = preSum[i - 1];
            for (int j = i + 1; j < N; ++j) {
                long long sum_ij = preSum[j - 1] - preSum[i];
                if ((nums[j] == 0 && nums[j - 1] == 0) || sum_0i != sum_ij)
                    continue;
                for (int k = j + 1; k < N; ++k) {
                    long long sum_jk = preSum[k - 1] - preSum[j];
                    if (sum_0i != sum_jk)
                        continue;
                    long long sum_k = preSum[N - 1] - preSum[k];
                    if (sum_0i == sum_k) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};
```

## 日期

2019 年 9 月 20 日 —— 是选择中国互联网式加班？还是外企式养生？


  [1]: https://assets.leetcode.com/uploads/2018/10/12/maze_1_example_1.png
  [2]: https://assets.leetcode.com/uploads/2018/10/13/maze_1_example_2.png
