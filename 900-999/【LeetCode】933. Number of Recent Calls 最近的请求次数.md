
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/number-of-recent-calls/description/


## 题目描述

Write a class ``RecentCounter`` to count recent requests.

It has only one method: ``ping(int t)``, where t represents some time in milliseconds.

Return the number of ``ping``s that have been made from 3000 milliseconds ago until now.

Any ping with time in ``[t - 3000, t]`` will count, including the current ping.

It is guaranteed that every call to ``ping`` uses a strictly larger value of ``t`` than before.

 

Example 1:

    Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
    Output: [null,1,2,3,3]
 

Note:

1. Each test case will have at most 10000 calls to ping.
1. Each test case will call ping with strictly increasing values of t.
1. Each call to ping will have 1 <= t <= 10^9.

## 题目大意

找出最近的3000毫秒内有多少个调用请求。每个调用请求是ping(t)函数，其中t是请求的时间，可以保证每次ping的参数t是大于前面的。

## 解题方法

### 二分查找

本周周赛第一题，我是用二分查找快速写出了这个题的解法，为后面的题省下了不少时间。

二分的想法是，我找到小于t-3000时间的元素索引，那么总共有多少个元素就是总长度-小于t-3000时间的元素索引。题目严格递增这个描述直接告诉了我们可以只用二分。二分使用的是bisect的bisect_left()，这个给我们返回的是小于目标元素的第一个结果。

时间复杂度是O(t*log(t))，空间复杂度O(t).

```python
class RecentCounter:

    def __init__(self):
        self.nums = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.nums.append(t)
        cur_pos = len(self.nums)
        prev_pos = bisect.bisect_left(self.nums, t - 3000)
        return cur_pos - prev_pos

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
```

### 队列

这个解法我是看了discuss才想到的，这个方法使用一个队列，当t时间到达之后，在t-3000之前的调用全部删除，因为这些不会对后面的产生任何影响了。删除之后，求长度就好了。

时间复杂度是O(t)，空间复杂度O(t).比上面快一点。

```python
class RecentCounter:

    def __init__(self):
        self.que = collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.que and self.que[0] < t - 3000:
            self.que.popleft()
        self.que.append(t)
        return len(self.que)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
```


## 相似题目


## 参考资料

https://leetcode.com/articles/number-of-recent-calls/

## 日期

2018 年 11 月 4 日 —— 下雨的周日


  [1]: http://bookshadow.com/weblog/2016/03/10/leetcode-palindrome-pairs/
