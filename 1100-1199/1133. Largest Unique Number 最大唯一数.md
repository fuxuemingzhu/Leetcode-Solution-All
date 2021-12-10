
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

## 题目描述

Given an array of integers A`, return the largest integer that only occurs once.

If no integer occurs once, return -1.

 Example 1:

Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: 
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.
Example 2:

Input: [9,9,8,8]
Output: -1
Explanation: 
There is no number that occurs only once.
 
Note:

1. `1 <= A.length <= 2000`
1.0 <= A[i] <= 1000

## 题目大意

给你一个整数数组 A，请找出并返回在该数组中仅出现一次的最大整数。

如果不存在这个只出现一次的整数，则返回 -1。

## 解题方法

### 桶排序

类似于桶排序的方式，计算每个数字出现了多少次，从最大数字开始向左遍历，找到第一个出现次数为1的数。

C++代码如下：

```cpp
class Solution {
public:
    int largestUniqueNumber(vector<int>& A) {
        vector<int> count(1010, 0);
        for (int a : A) {
            count[a]++;
        }
        for (int i = 1000; i >= 0; i --) {
            if (count[i] == 1) {
                return i;
            }
        }
        return -1;
    }
};
```

## 日期

2019 年 9 月 18 日 —— 今日又是九一八
