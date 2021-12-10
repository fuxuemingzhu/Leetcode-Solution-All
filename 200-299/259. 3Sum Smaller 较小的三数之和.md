- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/3sum-smaller/

## 题目描述

Given an array of `n` integers nums and a target, find the number of index triplets `i, j, k` with `0 <= i < j < k < n` that satisfy the condition `nums[i] + nums[j] + nums[k] < target`.

Example:

    Input: nums = [-2,0,1,3], and target = 2
    Output: 2 
    Explanation: Because there are two triplets which sums are less than 2:
                 [-2,0,1]
                 [-2,0,3]

Follow up: Could you solve it in O(n2) runtime?

## 题目大意

给定一个长度为 n 的整数数组和一个目标值 target，寻找能够使条件 `nums[i] + nums[j] + nums[k] < target` 成立的三元组  `i, j, k` 个数`（0 <= i < j < k < n）`。

## 解题方法

### 二分查找

先对数组进行排序。

固定`i, j`找出`k`，使得`nums[k] >= target - nums[i] - nums[j]`。
此时满足`nums[i] + nums[j] + nums[k] < target` 成立的三元组 `i, j, k` 个数是 `k - j - 1`个。

- `lower_bound()`找出`A[i] >= target`的`i`
- `upper_bound()`找出`A[i] > target`的`i`

所以使用lower_bound()找出大于等于`target - nums[i] - nums[j]`的k位置，此位置的k是第一个不满足题设的位置。因此满足条件的k在左边，共有`k - j - 1`个。

另外二分查找的时候，并不是从头开始查找，而是从`nums.begin() + j + 1`查找，即j的下一个元素位置开始。

时间复杂度O(N^2 * log(N)).

C++代码如下：

```cpp
class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
        const int N = nums.size();
        if (N <= 2) return 0;
        sort(nums.begin(), nums.end());
        int res = 0;
        for (int i = 0; i < N; ++i) {
            for (int j = i + 1; j < N; ++j) {
                int numsk = target - nums[i] - nums[j];
                int k = lower_bound(nums.begin() + j + 1, nums.end(), numsk) - nums.begin();
                res += k - j - 1;
            }
        }
        return res;
    }
};
```

### 双指针

`j`指向起始，`k`指向结束，找到`nums[j] + nums[k] < target - nums[i]`的区间长度，里面的元素全都符合。

- 如果`nums[j] + nums[k] >= target - nums[i]`，说明k太大，需要k--;
- 如果`nums[j] + nums[k] < target - nums[i]`，说明满足条件，又由于j比较小，需要j++;

时间复杂度O(N^2).

C++代码如下：

```cpp
class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
        const int N = nums.size();
        if (N <= 2) return 0;
        sort(nums.begin(), nums.end());
        int res = 0;
        for (int i = 0; i < N; ++i) {
            int j = i + 1;
            int k = N - 1;
            while (j < N && k > i && j != k) {
                if (nums[j] + nums[k] >= target - nums[i]) {
                    k --;
                } else {
                    res += k - j;
                    j ++;
                }
            }
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 22 日 —— 熬夜废掉半条命


  [1]: https://assets.leetcode.com/uploads/2018/10/12/maze_1_example_1.png
  [2]: https://assets.leetcode.com/uploads/2018/10/13/maze_1_example_2.png
  [3]: https://blog.csdn.net/fuxuemingzhu/article/details/101056461
