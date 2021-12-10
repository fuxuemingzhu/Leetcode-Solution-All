作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/


## 题目描述：

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., ``[0,0,1,2,2,5,6]`` might become ``[2,5,6,0,0,1,2]``).

You are given a target value to search. If found in the array return ``true``, otherwise return ``false``.

Example 1:

    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: true

Example 2:

    Input: nums = [2,5,6,0,0,1,2], target = 3
    Output: false

Follow up:

- This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
- Would this affect the run-time complexity? How and why?


## 题目大意

在一个含有重复数字的旋转递增数组中，找出是否存在某个数字。

## 解题方法

很明显的二分查找的题目，是[33. Search in Rotated Sorted Array][1]的拓展题目，变的是加了一个可能含有重复数字。

这样的话，如果直接进行左右指针的比较就不知道向哪个方向搜索了，所以，需要在正式比较之前，先移动左指针，是他指向一个和右指针不同的数字上。然后再做33题的查找。

至于查找部分，可以这么考虑：首先nums[l] > num[r]认为是恒成立的。

如果mid指向的位置比nums[l]还大，那么说明l到mid是有序的，这个时候如果``nums[l] <= target < nums[mid]``说明要查找的在Mid前面，移动右指针；否则要查找的在mid后面，移动左指针。

如果mid指向的位置比nums[r]还小，那么说明mid到r是有序的，然后同样的进行比较操作就行了。

时间复杂度是O(N)，空间复杂度是O(1).

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        N = len(nums)
        l, r = 0, N - 1
        while l <= r:
            while l < r and nums[l] == nums[r]:
                l += 1
            mid = l + (r - l) / 2
            if nums[mid] == target:
                return True
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
```

## 参考资料

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/177150/Search-in-Rotated-Sorted-Array-I


## 日期

2018 年 10 月 20 日 —— 10月剩余的时间又不多了


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79534213
