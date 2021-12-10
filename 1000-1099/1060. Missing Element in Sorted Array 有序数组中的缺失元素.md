

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/missing-element-in-sorted-array/

## 题目描述

Given a sorted array `A` of unique numbers, find the `K`-th missing number starting from the leftmost number of the array.

Example 1:

    Input: A = [4,7,9,10], K = 1
    Output: 5
    Explanation: 
    The first missing number is 5.

Example 2:

    Input: A = [4,7,9,10], K = 3
    Output: 8
    Explanation: 
    The missing numbers are [5,6,8,...], hence the third missing number is 8.

Example 3:

    Input: A = [1,2,4], K = 3
    Output: 6
    Explanation: 
    The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

Note:

1. `1 <= A.length <= 50000`
1. `1 <= A[i] <= 1e7`
1. `1 <= K <= 1e8`



## 题目大意

给出一个有序数组 A，数组中的每个数字都是 独一无二的，找出从数组最左边开始的第 K 个缺失数字。

## 解题方法

### 遍历

拿到这个题之后，看了下Note中取值范围都比较大，因此如果想一个数字一个数字去判断的话肯定会超时。所以需要使用一个点小技巧，即跳过不需要判断的数字。直接计算出每两个相邻数字之间能满足多少个，从而更新k。

先对nums排序。然后开始遍历，计算nums相邻两个元素之间的数字数即`nums[i] - pre - 1`个，是否可以满足需要的k。如果能满足，那么直接找出要返回的数字pre+k。如果不能满足，把k去掉已能满足的数字`nums[i] - pre - 1`。最后如果所有的nums数字都已经用完，但是还不能满足k，则需要返回`nums[nums.size() - 1] + k`。

C++代码如下：

```cpp
class Solution {
public:
    int missingElement(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int pre = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            if (k < nums[i] - pre) {
                return pre + k;
            } else {
                k -= nums[i] - pre - 1;
            }
            pre = nums[i];
        }
        return pre + k;
    }
};
 ```


## 日期

2019 年 9 月 21 日 —— 莫生气，我若气病谁如意


  [1]: https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png
  [2]: https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png
  [3]: https://assets.leetcode.com/uploads/2018/10/12/bstdllreturnbst.png
  [4]: https://blog.csdn.net/fuxuemingzhu/article/details/79294461
