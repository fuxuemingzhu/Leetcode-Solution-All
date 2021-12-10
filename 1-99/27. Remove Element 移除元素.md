作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：[https://leetcode.com/problems/remove-element/](https://leetcode.com/problems/remove-element/)

Total Accepted: 115693 Total Submissions: 341766 Difficulty: Easy


## 题目描述

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example: 
	
	Given input array nums = ``[3,2,2,3]``, val = ``3``
	
	Your function should return length = 2, with the first two elements of nums being 2.

## 题目大意

在原地去除数组中等于val的所有数字，返回的是数组要保留的之前位置的索引。

## 解题方法

### 双指针

一个指向前面等于val的数字，一个指向后面不等于val的数字，交换后移动的方式就是交换之后把末尾的指针前移；如果不进行交换操作则把前指针后移。

时间复杂度是O(N)，空间复杂度是O(1).

java版本。

```java
public class Solution {
    public int removeElement(int[] nums, int val) {
        int head=0;
        int tail=nums.length;
        while(head!=tail){
            if(nums[head]==val){
                nums[head]=nums[tail-1];
                tail--;
            }else{
                head++;    
            }
        }
        return tail;
    }
}
```
AC:1ms

Python 版本。

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        N = len(nums)
        l, r = 0, N - 1
        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1
        return l
```

也可以下面这么写，只不过需要加一个判断即当l>r的时候break掉。

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        N = len(nums)
        l, r = 0, N - 1
        while l <= r:
            while r >= 0 and nums[r] == val:
                r -= 1
            if l > r:
                break
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
        return l
```

### 记录起始位置

这个做法和双指针不一样的地方在于，这个做法使用了begin指针保存的是已经确定了没有val的数组范围，使用for循环来向后遍历查找不等于val的数字放入begin位置。这样确实做了很多无用功，即对出去了等于val的每个数字都做了一次赋值操作。

时间复杂度是O(N)，空间复杂度是O(1).

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        N = len(nums)
        begin = 0
        for i in range(N):
            if nums[i] != val:
                nums[begin] = nums[i]
                begin += 1
        return begin
```

## 日期


2016/5/3 11:29:08 
2018 年 10 月 31 日 ——十月最后一天，万圣节！
