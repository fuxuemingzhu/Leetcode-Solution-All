
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/search-in-rotated-sorted-array/description/

## 题目描述


Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., ``[0,1,2,4,5,6,7]`` might become ``[4,5,6,7,0,1,2]``).

You are given a target value to search. If found in the array return its index, otherwise return ``-1``.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of ``O(log n)``.

Example 1:

	Input: nums = [4,5,6,7,0,1,2], target = 0
	Output: 4

Example 2:

	Input: nums = [4,5,6,7,0,1,2], target = 3
	Output: -1

## 题目大意

找出旋转有序数组中的是否包含某个值，如果有则返回序号，否则返回-1。

## 解题方法

明显也是二分查找，不过我错了好几次。。这个题重要的不是通过mid与左右指针指向的值的比较来移动指针。而是通过判断那一部分是有序的，target是否在这个有序的切片之中来实现的。

这个题让我们对二分查找有更深刻的理解：

我们的二分查找的思想就是找出某个条件，这个条件给了我们移动左右指针的参考，即要判断查找的target在mid的左边还是右边。具体到这个题目，因为给出的数组是旋转有序的，如果mid指向的位置在于pivot之后，那么mid向后部分是有序的，这个时候需要判断target在mid左边还是右边，最简单的方法就是判断target是不是在[pivot,r]区间内，如果的话就向mid后半部分搜索，否则就向mid左半部分搜索；同理，当mid在pivot之前，那么mid前面部分是有序的，根据target判断下面要向mid的左边还是右边搜索。

下面的解答摘自：http://blog.csdn.net/linhuanmars/article/details/20525681

具体来说，假设数组是A，每次左边缘为l，右边缘为r，还有中间位置是m。在每次迭代中，分三种情况：

（1）如果target==A[m]，那么m就是我们要的结果，直接返回；
（2）如果A[m]<A[r]，那么说明从m到r一定是有序的（没有受到rotate的影响），那么我们只需要判断target是不是在m到r之间，如果是则把左边缘移到m+1，否则就target在另一半，即把右边缘移到m-1。
（3）如果A[m]>=A[r]，那么说明从l到m一定是有序的，同样只需要判断target是否在这个范围内，相应的移动边缘即可。

注意，由于这个题目要进行和边缘元素的判断，所以没有采取[l,r)的左闭右开区间，而是使用了[l, r]双闭区间。

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1            
```

C++代码如下：

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        const int N = nums.size();
        // [l, r)
        int l = 0, r = N - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] < nums[r]) {
                if (target > nums[mid] && target <= nums[r]) {
                    l = mid + 1;
                } else  {
                    r = mid - 1;
                }
            } else {
                if (target >= nums[l] && target < nums[mid]) {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }
        }
        return -1;
    }
};
```


## 日期

2018 年 3 月 12 日 
2019 年 1 月 11 日 —— 小光棍节？
