
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

[https://leetcode.com/problems/remove-duplicates-from-sorted-array/][1]

Total Accepted: 129010 Total Submissions: 384622 Difficulty: Easy


## 题目描述

Given a sorted array `nums`, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array `in-place` with `O(1)` extra memory.

Example 1:

	Given nums = [1,1,2],
	
	Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
	
	It doesn't matter what you leave beyond the returned length.

Example 2:

	Given nums = [0,0,1,1,1,2,2,3,3,4],
	
	Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
	
	It doesn't matter what values are set beyond the returned length.

## 题目大意

从一个有序数组中删除重复的数字，只保留下无重复的有序数组，把这些数字放到原数组的前面部分，返回这部分的长度。

## 解题方法

### 双指针

慢指针指向应该放入元素的**位置**，每次移动一格。快指针找到应该放**哪个元素**，每次找到下一个新的元素。

Python代码如下：
```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N <= 1: return N
        left, right = 0, 1
        while right < N:
            while right < N and nums[right] == nums[left]:
                right += 1
            left += 1
            if right < N:
                nums[left] = nums[right]
        return left
```

C++代码如下：

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        const int L = nums.size();
        if (L <= 1) return L;
        int slow = 1;
        int fast = 1;
        while (fast < L) {
            while (fast < L && nums[fast] == nums[fast - 1]) {
                fast ++;
            }
            if (fast < L) {
                nums[slow] = nums[fast];
                slow ++;
                fast ++;
            }
        }
        return slow;
    }
};
```

Java代码如下：

```java
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}
```


## 日期

2016 年 05月 8日 
2019 年 9 月 17 日 —— 听了hulu宣讲会，觉得hulu的压力不大


  [1]: https://leetcode.com/problems/remove-duplicates-from-sorted-array 
