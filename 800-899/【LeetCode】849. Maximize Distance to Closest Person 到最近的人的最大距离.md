
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/maximize-distance-to-closest-person/description/

## 题目描述

In a row of ``seats``, ``1`` represents a person sitting in that seat, and ``0`` represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

    Input: [1,0,0,0,1,0,1]
    Output: 2
    Explanation: 
    If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
    If Alex sits in any other open seat, the closest person has distance 1.
    Thus, the maximum distance to the closest person is 2.

Example 2:
    
    Input: [1,0,0,0]
    Output: 3
    Explanation: 
    If Alex sits in the last seat, the closest person is 3 seats away.
    This is the maximum distance possible, so the answer is 3.

Note:

1. 1 <= seats.length <= 20000
1. seats contains only 0s or 1s, at least one 0, and at least one 1.

## 题目大意

给出了一个列表表示一排座位，1代表这个位置有人坐，0代表这个位置没人做。现在需要找一个位置坐，并找出坐在哪个位置时，离旁边人的座位的距离最大，是多少。

## 解题方法

这道题是不是很眼熟呢？我翻了一下笔记，果然前几天做过啊！现在脑子里还有点印象：需要左右遍历两次。这个题目是[【LeetCode】821. Shortest Distance to a Character][1]。当时这个题目的要求是：给定字符串S和属于该字符串的一个字符C，要求出字符串中的每个字符到最近的C的距离。

不要看到一个是求最距离一个是求最远距离就觉得这两个题有不同。其实本题就是求最近距离的最大值！

上面的字符串题是求每个位置到C的最近距离，其实就是这个题的每个位置到1的最近距离。上面的题是要返回一个列表，这个题是要返回列表的最大值。所以就这。

我把字符串的题的解法改一下：

两步走的方案：

第一步，先假设在很远的位置有个座位有人坐，那么从左到右开始遍历，找出每个座位到其最近的左边的有人坐的位置的距离； 
第二步，再假设在很远的位置有个座位有人坐，那么从右到左开始遍历，找出每个字符到其最近的右边的有人坐的位置的距离，并和第一步求出的距离进行比较，找出最小值为结果；

最后，找出这个列表的最大值。

两个技巧：

1. 设了一个比字符串长度更远的一个字符C，保证后面求最小值更新距离时一定会被更新。
1. 无论如何都用到了abs求绝对值，哪怕可能是不需要的，目的是不用费脑子思考谁大谁小了。


代码如下：

```python
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        index = -200000
        _len = len(seats)
        ans = [0] * _len
        for i in range(_len):
            if seats[i] == 1:
                index = i
            else:
                ans[i] = abs(i - index)
        index = -200000
        for i in range(_len - 1, -1, -1):
            if seats[i] == 1:
                index = i
            else:
                ans[i] = min(abs(i - index), ans[i])
        return max(ans)
```

## 日期

2018 年 6 月 10 日 —— 等了两天的腾讯比赛复赛B的数据集，结果人家在复赛刚开始就给了。。
2018 年 11 月 22 日 —— 感恩节快乐～

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/80471765
