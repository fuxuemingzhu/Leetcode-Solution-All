
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/array-partition-i/#/description][1]


## 题目描述

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:

    Input: [1,4,3,2]
    
    Output: 4
    Explanation: n is 2, and the maximum sum of pairs is 4.

Note:

 1. n is a positive integer, which is in the range of [1, 10000].
 2. All the integers in the array will be in the range of [-10000, 10000].

## 题目大意

给出2n个数字，找出如何划分数据使每个括号内的最小值的和是最大的。

## 解题方法

### 排序

这个题我的方法比较简单直白。那么我想，比较大的数字一定要和比较大的数字在一起才行，否则括号内的小的结果是较小的数字。所以先排序，排序后的结果找每个组中数据的第一个数字即可。

时间复杂度是O(NlogN)，空间复杂度是O(1).

Java代码如下：

```java
public class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int ans = 0;
        for(int i = 0; i < nums.length; i += 2){
            ans += nums[i];
        }
        return ans;
    }
}
```

python版本可以写的更简单，因为可以使用切片直接取出偶数位置的数字进行求和。

```python
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])
```

## 日期

2017 年 5 月 8 日 
2018 年 11 月 5 日 —— 打了羽毛球，有点累

  [1]: https://leetcode.com/problems/array-partition-i/#/description
