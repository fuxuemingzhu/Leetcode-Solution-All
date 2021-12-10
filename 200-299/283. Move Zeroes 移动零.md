
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/move-zeroes/](https://leetcode.com/problems/move-zeroes/)

Total Accepted: 77443 Total Submissions: 175420 Difficulty: Easy


## 题目描述

Given an array ``nums``, write a function to move all ``0``'s to the end of it while maintaining the relative order of the non-zero elements.

Example:

	Input: [0,1,0,3,12]
	Output: [1,3,12,0,0]

Note:

1. You must do this **in-place** without making a copy of the array.
1. Minimize the total number of operations.

## 题目大意

把数组中的0换到数组的结尾去，同时需要保证其他数字的位置不能改变。另外需要在原地进行操作。


## 解题方法

in-place的把0放到数组的最后，其他顺序不变。用两个指针。

### 方法一：首尾指针

两个指针，一个指向开始，一个指向结尾。开始这个判断是否为零，如果是零，就把其余的数据往前排，零放到末尾，开始和结尾指针向中间移动。开始这个不是零的话，就开始指针后移，结尾不变。直到两个指针重合为止。

算法效率较低，原因在于所有的数据往前移动，需要耗时。

```java
public class Solution {
    public void moveZeroes(int[] nums) {
        int start=0;
        int end=nums.length-1;
        while(start!=end){
            if(nums[start]==0){
                 for(int j=start+1;j<=end;j++){
                     nums[j-1]=nums[j];
                 }
                 nums[end]=0;
                 end--;
            }else{
                start++;
            }
        }
        
    }
}
```
AC:21ms

### 方法二：头部双指针+双循环

二刷的Python版本，使用两个指针，找到下个不为0的位置，然后和当前的0进行交换。

时间复杂度是O(N^2)，空间复杂度是O(1)。

```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        for i in range(N):
            if nums[i] != 0:
                continue
            j = i + 1
            while j < N:
                if nums[j] == 0:
                    j += 1
                    continue
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                break
            if j == N:
                break
```

### 方法三：指针指向第一个0的位置

使用两个指针遍历数组，一个指向数值为0的元素，另一个指向数值不为0的元素，在遍历的过程中，不断交换两个指针的值。

![](http://i.imgur.com/rlNMsDa.png)


这个比我的算法一简单，因为不需要把所有的数据进行搬移，只需要搬移正的数据。

```java
public class Solution {
    public void moveZeroes(int[] nums) {
		int zero = 0;
		while (zero < nums.length && nums[zero] != 0) {
			zero++;
		}
		int non_zero = zero + 1;//非零的数值开始的位置应该在零值的后头，这样交换才有意义
		while (non_zero < nums.length && nums[non_zero] == 0) {
			non_zero++;
		}
		while (zero < nums.length && non_zero < nums.length) {
			int temp = nums[zero];
			nums[zero] = nums[non_zero];
			nums[non_zero] = temp;
			while (nums[non_zero] == 0) {//寻找下一个非零数值
				non_zero++;
				if (non_zero >= nums.length) {
					return;//找不到说明已经排好序了
				}
			}
			zero++;
		}
    }
}
```
AC:1ms

这个算法竟然写了一个小时。。崩溃。主要注意while里边进行判断，不要溢出。


---

二刷的时候写了个python版本的这个代码，简洁的多了。


```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i = 0
        for j in range(N):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
```

## 日期

2016/4/30 0:17:23 
2018 年 11 月 10 日 —— 这么快就到双十一了？？
