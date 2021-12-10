
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/sliding-window-maximum/

## 题目描述

Given an array nums, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

    Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
    Output: [3,3,5,5,6,7] 
    
    Explanation: 
    
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7

Note:

- You may assume `k` is always valid, `1 ≤ k ≤ input` array's size for non-empty array.

Follow up:
- Could you solve it in linear time?

 
## 题目大意

求一个滑动窗口中的最大值。

## 解题方法

### 单调递减队列

这个题是剑指offer的题目，做法挺多，我使用的是单调递减双向队列解决。

设定一个大小为k的单调递减双向队列，时刻保持队列是单调递减的，即如果从最右边加入了一个较大的数字，需要从右开始退队列，退到队列中剩余的数字都比该数字大位置，此时队列是单调递减的。如果队列的大小达到了k，则应该把队列最前面的数字（其实是之前区间的最大值）删除掉。

时间复杂度是O(N).

python代码如下：

```python
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        que = collections.deque() # [[i, num]]
        res = []
        for i, num in enumerate(nums):
            if que and i - que[0][0] >= k:
                que.popleft()
            while que and que[-1][1] <= num:
                que.pop()
            que.append([i, num])
            if i >= k - 1:
                res.append(que[0][1])
        return res
```

### MultiSet

在使用这个方法前，我们从这个题目入手。这个题目想让我们得到一个区间里面的最大值，每次这个区间在一次操作中增加一个值、（可能）去掉一个值。那么我们想到如何求一个区间的最大值？简单的方法是使用遍历区间的方式，时间复杂度是O(k)，但是既然每次最多只会更改两个数字，没必要遍历整个区间求最大值，于是会想到set/multiset这种结构，C++中的set/multi是使用红黑树实现的，会对内部的元素排序。set会进行去重，而multiset不去重。因此，我们可以使用multiset这个结构，每次新加入一个元素，则会自动排序，最大值的位置是rbegin()；如果元素个数达到了k，则把该区间最左边的元素去除，使用st.find(nums[i - k])找到最左边元素的位置，并删除即可。

时间复杂度是O(N*log(k))，每次插入和删除操作是log(k)时间复杂度。

```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        multiset<int> st;
        for (int i = 0; i < nums.size(); ++i) {
            if (st.size() >= k) st.erase(st.find(nums[i - k]));
            st.insert(nums[i]);
            if (i >= k - 1)
                res.push_back(*st.rbegin());
        }
        return res;
    }
};
```

参考资料：https://www.cnblogs.com/grandyang/p/4656517.html

## 日期

2019 年 9 月 14 日 —— 假期的生活就是不规律
