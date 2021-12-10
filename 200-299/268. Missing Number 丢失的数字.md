
作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/missing-number/#/description][1]


## 题目描述


Given an array containing ``n`` distinct numbers taken from ``0, 1, 2, ..., n``, find the one that is missing from the array.

Example 1:

	Input: [3,0,1]
	Output: 2

Example 2:

	Input: [9,6,4,2,3,5,7,0,1]
	Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

## 题目大意

求N+1个不同的数字（0～N）中缺失了一个数字，求这个数字是多少？

## 解题方法

### 求和

因为数字是从0, 1, 2, ..., n中抽走一个，因此，该数字的值是0, 1, 2, ..., n的和减去现有数字的和。

```java
public class Solution {
    public int missingNumber(int[] nums) {
        int sum = 0;
        int len = nums.length;
        for(int i = 0; i < len; i++){
            sum += nums[i];
        }
        return len * (len + 1)/2 - sum;
    }
}
```

---
二刷，python

```python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        num_sum = sum(nums)
        return n * (n + 1) / 2 - num_sum
```

### 异或

索引是0～N，直接异或一遍0~N各个数字共N+1个，并且异或所有出现的数字，剩下的结果是只出现一次的数字，也就是说缺失的那个数字。

需要注意的是初始化是N，这样才能把0~N各个索引多异或一遍。

```java
public int missingNumber(int[] nums) { //xor
    int res = nums.length;
    for(int i=0; i<nums.length; i++){
        res ^= i;
        res ^= nums[i];
    }
    return res;
}
```




## 日期

2017 年 4 月 21 日 
2018 年 11 月 16 日 —— 又到周五了！

  [1]: https://leetcode.com/problems/missing-number/#/description
