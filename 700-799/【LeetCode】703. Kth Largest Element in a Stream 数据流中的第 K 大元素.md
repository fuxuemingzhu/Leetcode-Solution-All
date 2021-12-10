
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

## 题目描述

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your ``KthLargest`` class will have a constructor which accepts an integer ``k`` and an integer array ``nums``, which contains initial elements from the stream. For each call to the method ``KthLargest.add``, return the element representing the kth largest element in the stream.

Example:

    int k = 3;
    int[] arr = [4,5,8,2];
    KthLargest kthLargest = new KthLargest(3, arr);
    kthLargest.add(3);   // returns 4
    kthLargest.add(5);   // returns 5
    kthLargest.add(10);  // returns 5
    kthLargest.add(9);   // returns 8
    kthLargest.add(4);   // returns 8

Note: 

You may assume that nums' length ≥ k-1 and k ≥ 1.

## 题目大意

实现一个类，这个类能找出一个数据流中第K大的数。

## 解题方法

### 小根堆

曾经在亚马逊遇到过的面试题，可惜当时不会，甚至连用堆来实现都没想到。现在知道用堆来实现了。

Python的堆是小根堆，不需要对其进行转换，我们想一想，如果一个堆的大小是k的话，那么最小的数字就在其最前面（即为第k大的数字），只要维护当新来的数字和最前面的这个数字比较即可。

所以我们的工作就是维护一个小根堆，这个小根堆保存的是从第K大的数字到最大的数字。堆的大小即为K。

实现过程比较简单，只要熟悉Python中堆的操作即可。

代码如下：

```python
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pool = nums
        self.size = len(self.pool)
        self.k = k
        heapq.heapify(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.size < self.k:
            heapq.heappush(self.pool, val)
            self.size += 1
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```

## 日期

2018 年 7 月 13 日 —— 早起困一上午，中午必须好好休息才行啊
2018 年 11 月 21 日 —— 又是一个美好的开始
