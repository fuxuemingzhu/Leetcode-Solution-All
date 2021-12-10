作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/find-k-closest-elements/description/

## 题目描述：

Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:

Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:

1. The value k is positive and will always be smaller than the length of the sorted array.
1. Length of the given array is positive and will not exceed 104
1. Absolute value of elements in the array and x will not exceed 104

UPDATE (2017/9/19):

The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.

## 题目大意

在数组arr中找出离x最近的k个数。

## 解题方法

### 方法一：堆

解法比较多。比较容易想到的一种解法是使用计算每个数字和x的距离，然后找出最近距离的数字。这就是常见的TopK问题。使用小根堆很容易实现。

时间复杂度是O(N)，空间复杂度是O(N)。

```python
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        N = len(arr)
        sub = [((arr[i] - x) ** 2, i) for i in range(N)]
        heapq.heapify(sub)
        return sorted([arr[heapq.heappop(sub)[1]] for i in range(k)])
```

### 方法二：双指针

由于数组已经排序，完全可以从左右两个方向向中间遍历，每次找到距离大的那个数字，弹出去就好了，最后保留k个数字。

```python
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        while len(arr) > k:
            if x - arr[0] <= arr[-1] - x:
                arr.pop()
            else:
                arr.pop(0)
        return arr
```

### 方法三：二分查找

最简单思想的二分是找出x的位置，然后找出其旁边的k个数。但是下面这个做法惊为天人，比较区间两端的数值和x的距离，如果左边离得远了，就向右边走；如果右边离得远了，就像左边走。这个对二分查找的理解必须很深刻了。

```python
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = 0
        right = len(arr) - k
        while left < right:
            mid = left + (right - left) / 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]
```


参考资料：

http://www.cnblogs.com/grandyang/p/7519466.html

## 日期

2018 年 10 月 8 日 —— 终于开学了。


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82960833
