
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/single-number/][1]

 - Total Accepted: 183838
 - Total Submissions: 348610
 - Difficulty: Easy

## 题目描述

Given a **non-empty** array of integers, every element appears twice **except for one**. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

	Input: [2,2,1]
	Output: 1

Example 2:

	Input: [4,1,2,1,2]
	Output: 4

## 题目大意

数组中除了有一个数字只出现了一次之外，其余的数字都出现了偶数次。找出这个只出现了一次的叛徒。

## 解题方法

### 异或

标准的异或运算！

异或运算是可以交换顺序的运算，也就是说和元素的排列顺序无关，自己异或自己等于0,0异或别人等于别人。故，

> we use bitwise XOR to solve this problem :
> 
> first , we have to know the bitwise XOR in java
>  **1. 0 ^ N = N** 
>  **2.  N ^ N = 0**
> So..... if N is the single number
> 
> N1 ^ N1 ^ N2 ^ N2 ^..............^ Nx ^ Nx ^ N
> 
> = (N1^N1) ^ (N2^N2) ^..............^ (Nx^Nx) ^ N
> 
> = 0 ^ 0 ^ ..........^ 0 ^ N
> 
> = N

即，只要把所有的数字异或一遍，如果出现两次的数字，进行异或之后自动消失，剩余的就是只出现一次的那个数字。

java代码如下。

```java
public class Solution {
    public int singleNumber(int[] nums) {
        int returnNum=0;
        for(int i=0; i<nums.length; i++){
            returnNum ^=nums[i];
        }
        return returnNum;
    }
}
```

AC:1ms

----

二刷 python。同样使用异或，对于Python2来说可以直接使用reduce函数，就所有数字进行运算的结果。

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)
```

### 字典

别只记得位运算，忘记了最简单的数字统计啊！可以使用Counter直接求只出现一次的数字即可。

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        return count.most_common()[-1][0]
```


## 日期

2017 年 1 月 7 日 
2018 年 3 月 14 日 -- 霍金去世
2018 年 11 月 ９ 日 —— 睡眠可以


  [1]: https://leetcode.com/problems/single-number/
