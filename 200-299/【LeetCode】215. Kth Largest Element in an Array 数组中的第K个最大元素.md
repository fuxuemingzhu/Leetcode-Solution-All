
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/kth-largest-element-in-an-array/description/


## 题目描述


Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

	Input: [3,2,1,5,6,4] and k = 2
	Output: 5

Example 2:

	Input: [3,2,3,1,2,4,5,5,6] and k = 4
	Output: 4

Note: 

- You may assume k is always valid, 1 ≤ k ≤ array's length.

## 题目大意

找出数组中第k大的值。

## 解题方法

### 方法一：移除最大值

找出第k大的数字。这个题可以直接排序，速度还挺快。我的做法是通过循环``k-1``次，每次都在列表中去除列表的最大值。注意，列表的remove每次只会移除一个值。例如：

```
In [1]: a = [1,2,3,3,3,3]

In [2]: a.remove(3)

In [3]: a
Out[3]: [1, 2, 3, 3, 3]

In [4]: a.remove(3)

In [5]: a
Out[5]: [1, 2, 3, 3]

```

这题答案：

```python
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k - 1):
            nums.remove(max(nums))
        return max(nums)
```

### 方法二：排序

排序之后直接找倒数第k个数字即可。

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        return nums[nums.size() - k];
    }
};
```

### 方法三：大顶堆

使用大顶堆，弹出k-1个数字，那么再弹一次就是第k大的值了。

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> q;
        for (int n : nums) {
            q.push(n);
        }
        int res = 0;
        while (k--) {
            res = q.top(); q.pop();
        }
        return res;
    }
};
```

### 方法四：partition

待完成。


## 日期

2018 年 2 月 5 日 
2018 年 12 月 23 日 —— 周赛成绩新高
