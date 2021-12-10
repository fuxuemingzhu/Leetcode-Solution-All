- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/find-in-mountain-array/

# 题目描述


给你一个 山脉数组 `mountainArr`，请你返回能够使得 `mountainArr.get(index)` 等于 `target` 最小 的下标 `index` 值。

如果不存在这样的下标 `index`，就请返回 `-1`。

 

何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：

1. 首先，`A.length >= 3`
2. 其次，在 `0 < i < A.length - 1` 条件下，存在 `i` 使得：

- `A[0] < A[1] < ... A[i-1] < A[i]`
- `A[i] > A[i+1] > ... > A[A.length - 1]`
 

你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：

- `MountainArray.get(k)` - 会返回数组中索引为k 的元素（下标从 0 开始）
- `MountainArray.length()` - 会返回该数组的长度
 

注意：

对 MountainArray.get 发起超过 100 次调用的提交将被视为错误答案。此外，任何试图规避判题系统的解决方案都将会导致比赛资格被取消。

为了帮助大家更好地理解交互式问题，我们准备了一个样例 “答案”：https://leetcode-cn.com/playground/RKhe3ave，请注意这 不是一个正确答案。

 

示例 1：
    
    输入：array = [1,2,3,4,5,3,1], target = 3
    输出：2
    解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。

示例 2：
    
    输入：array = [0,1,2,4,2,1], target = 3
    输出：-1
    解释：3 在数组中没有出现，返回 -1。
     

提示：

1. `3 <= mountain_arr.length() <= 10000`
1. `0 <= target <= 10^9`
1. `0 <= mountain_arr.get(index) <= 10^9`



# 题目大意

在一个山形的数组上，找出 target 元素第一次出现的位置。
# 解题方法

## 二分查找

这个题疯狂提示用二分查找。
提示1. 山脉数组的左右两部分分别有序
提示2. array数组总长度是 10000，总的读取元素的次数不超过 100 次。
根据这两点，我们可以 100% 地确定用二分查找方法。

题目的难点在于找到 target 出现的第一个位置，如果我们想着只在山峰的左边或者右边使用一次二分查找的话，没法确定一次就就查找到。因此必须在山峰的左右两边都进行二分查找。

那么思路就是：
1. 找到山峰的位置
2. 在山峰的左边查找 target
3. 如果查找不到，则在山峰的右边查找 target

二分法是个经典的模板问题。推荐使用 [二分查找模板2](https://ojeveryday.github.io/AlgoWiki/#/BinarySearch/03-template-2)。

找到山峰的位置可以根据 mid 元素处于上坡还是下坡来识别出来。在左右两部分进行查找 target 就是普通的二分，唯一需要注意的是 左边是递增的，右边是递减的，二分查找的判断不要出错。

Python 代码如下：

```python
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, nums: 'nums') -> int:
        N = nums.length()
        peek = self.findPeek(target, nums)
        left_index = self.findInAscOrder(target, nums, 0, peek)
        right_index = self.findInDecOrder(target, nums, peek, N - 1)
        if left_index != -1:
            return left_index
        else:
            return right_index

    def findPeek(self, target, nums):
        N = nums.length()
        left, right = 1, N - 2
        while left <= right:
            mid = left + (right - left) // 2
            if nums.get(mid - 1) < nums.get(mid) > nums.get(mid + 1):
                return mid
            elif nums.get(mid - 1) < nums.get(mid) < nums.get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def findInAscOrder(self, target, nums, begin, end):
        left, right = begin, end
        while left <= right:
            mid = left + (right - left) // 2
            print(left, right, mid)
            cur = nums.get(mid)
            if cur == target:
                return mid
            elif cur < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def findInDecOrder(self, target, nums, begin, end):
        left, right = begin, end
        while left <= right:
            mid = left + (right - left) // 2
            cur = nums.get(mid)
            if cur == target:
                return mid
            elif cur < target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
```


**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 29 日 —— 连续刷二分


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79451733
