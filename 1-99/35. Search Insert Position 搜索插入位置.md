
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/search-insert-position/#/description][1]


## 题目描述


Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

	Input: [1,3,5,6], 5
	Output: 2

Example 2:

	Input: [1,3,5,6], 2
	Output: 1

Example 3:

	Input: [1,3,5,6], 7
	Output: 4

Example 4:

	Input: [1,3,5,6], 0
	Output: 0

## 题目大意

找出一个数字应该插入到有序数组中的位置。

## 解题方法

### 二分查找

数组有序的，可以用二分查找的方法。注意，如果查找到结果的要返回mid，没查找到的话返回的是left，因为这个时候left和right已经交叉了，left是比较靠右的位置，也就是应该插入的位置。

对于Python来说可以直接使用bisect模块，bisect_left()函数就是题目想要的函数。

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect.bisect_left(nums, target)
```

如果自己手写二分查找的话，那么可以直接套用模板即可：

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        left, right = 0, N #[left, right)
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left
```

Java代码如下：

```java
public class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int mid = 0;
        while(left <= right){
            mid = (left + right) / 2;
            if(nums[mid] == target){
                return mid;
            }else if(nums[mid] > target){
                right--;
            }else{
                left++;
            }
        }
        return left;
    }
}
```

## 日期

2017 年 4 月 25 日 
2018 年 11 月 21 日 —— 又是一个美好的开始

  [1]: https://leetcode.com/problems/search-insert-position/#/description
