
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/product-of-array-except-self/description/

## 题目描述

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

    For example, given [1,2,3,4], return [24,12,8,6].

Follow up:

Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)



## 解题方法

### 两次遍历

当我想了一个用除法做的答案之后就发现题目不允许用除法做233333.

这个题巧妙的地方在于，结果数组不算作空间复杂度里，所以可以用在结果数组中遍历的方式去做。第一次遍历在结果数组里保存每个数字左边的数字乘积，第二个遍历保存的是左边乘积和这个数字右边的乘积的乘积。

所以就得到了出了本身以外的其他元素的乘积。

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        _len = len(nums)
        prod = 1
        for i in range(_len):
            answer.append(prod)
            prod *= nums[i]
        prod = 1
        for i in range(_len - 1, -1, -1):
            answer[i] *= prod
            prod *= nums[i]
        return answer
```

C++代码如下：

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        const int N = nums.size();
        vector<int> res(N, 1);
        int prod = 1;
        for (int i = 0; i < N; i ++) {
            res[i] = prod;
            prod *= nums[i];
        }
        prod = 1;
        for (int i = N - 1; i >= 0; i--) {
            res[i] *= prod;
            prod *= nums[i];
        }
        return res;
    }
};
```

## 日期

2018 年 2 月 14 日 
2018 年 12 月 14 日 —— 12月过半，2019就要开始

