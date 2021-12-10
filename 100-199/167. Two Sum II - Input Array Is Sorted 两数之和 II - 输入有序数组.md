
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/description][1]


## 题目描述


Given an array of integers that is already **sorted in ascending order**, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

- Your returned answers (both index1 and index2) are not zero-based.
- You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:

	Input: numbers = [2,7,11,15], target = 9
	Output: [1,2]
	Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

## 题目大意

在已经排好序的数组中，找到两个数字的和等于target，返回两个数字的基于1开始的索引。

## 解题方法

### Java解法

已经排序好了的数组，找出目标和。可以挨个试，时间复杂度是O(n^2)，复杂度太高。可以用双指针，同时向中间靠拢，肯定能达到目标的和。

```java
public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int index[] = new int[2];
        int left = 0;
        int right = numbers.length - 1;
        while(left < right){
            long temp = numbers[left] + numbers[right];
            if(temp == target){
                index[0] = left + 1;
                index[1] = right + 1;
                break;
            }else if(temp < target){
                left++;
            }else{
                right--;
            }
        }
        return index;
    }
}
```

### Python解法

二刷，python解法。

```python
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        N = len(numbers)
        left, right = 0, N - 1
        while left < right:
            cursum = numbers[left] + numbers[right]
            if cursum == target:
                return [left + 1, right + 1]
            elif cursum < target:
                left += 1
            else:
                right -= 1
        return [0, 0]
```

## 日期

2017 年 4 月 18 日 
2018 年 11 月 14 日 —— 又到周五了

  [1]: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/description
