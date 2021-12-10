
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/sort-colors/description/


## 题目描述

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:

You are not suppose to use the library's sort function for this problem.

Example:

	Input: [2,0,2,1,1,0]
	Output: [0,0,1,1,2,2]

Follow up:

- A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

- Could you come up with an one-pass algorithm using only constant space?


## 题目大意

对乱序的0,1,2三个数字进行排序，保证结果是相同元素聚在一起。

## 解题方法

### 计数排序

因为只有三个数，所以简单的方法是计数排序。第一次遍历，统计出这三个数字出现的次数，第二次遍历，根据三个数字的次数对原列表进行修改。

```python
from collections import Counter
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        for i in xrange(len(nums)):
            if i < count[0]:
                nums[i] = 0
            elif i < count[0] + count[1]:
                nums[i] = 1
            else:
                nums[i] = 2
```

### 双指针

我看到这个题的时候，很明显的看出是要把一个数组分成三段，分别是小于v，等于v和大于v。由于只有三个数字，所以也就是0,1,2分别聚在一起。所以，这个题的考点来自快排之三项切分快速排序。在《算法》第四版中有介绍，也可以看[快速排序及三向切分快速排序](https://blog.csdn.net/i_scream_/article/details/51413057)。

下面是题目讲解：

如果只能扫一遍，很容易想到的就是左边存放0和1，右边存放2.两边往中间靠。

设置两个指针，zero和two；zero指向第一个1的位置（0串的末尾），two指向第一个非2的位置。然后用i对nums进行遍历：

然后使用i从头到尾扫一遍，直到与two相遇。

i遇到0就换到左边去，遇到2就换到右边去，遇到1就跳过。

需要注意的是：由于zero记录第一个1的位置，因此A[zero]与A[i]交换后，A[zero]为0,A[i]为1，因此i++，zero++；

而two记录第一个非2的位置，可能为0或1，因此A[two]与A[i]交换后，A[two]为2,A[i]为0或1，i不能前进，要后续判断。

```python
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0
        two = len(nums) - 1
        i = 0
        while i <= two:
            if nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1

```

## 日期

2018 年 2 月 27 日 
2019 年 1 月 5 日 —— 美好的周末又开始了
