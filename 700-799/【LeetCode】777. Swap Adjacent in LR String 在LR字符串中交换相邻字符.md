作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/swap-adjacent-in-lr-string/description/


## 题目描述

In a string composed of ``'L'``, ``'R'``, and ``'X'`` characters, like ``"RXXLRXRXL"``, a move consists of either replacing one occurrence of ``"XL"`` with ``"LX"``, or replacing one occurrence of ``"RX"`` with ``"XR"``. Given the starting string ``start`` and the ending string ``end``, return True if and only if there exists a sequence of moves to transform one string to the other.

Example:

    Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
    Output: True
    Explanation:
    We can transform start to end following these steps:
    RXXLRXRXL ->
    XRXLRXRXL ->
    XRLXRXRXL ->
    XRLXXRRXL ->
    XRLXXRRLX

Note:

1. 1 <= len(start) = len(end) <= 10000.
1. Both start and end will only consist of characters in {'L', 'R', 'X'}.



## 题目大意

给出了一个初始的字符串，可以把初始字符串中的XL换成LX，可以把初始字符串中的RX换成XR，求问能不能通过一定的次数之后，把初始字符串变成结束字符串。


## 解题方法

### 智商题

本来以为是类似于迷宫的搜索问题，看到数据规模这么大，感觉不像，一看tag果然是智商题，那我就放弃了，智商不够用啊。

题目说了可以把初始字符串中的XL换成LX，可以把初始字符串中的RX换成XR，那么也就是说初始字符串中的L只能向左移动，初始字符串中R只能向右移动。并且L和R是不可能交换顺序的，两个字符串的L和R对应次数应该相等。知道这个规律之后，就使用双指针去解决就好了。

用i,j分别指向start和end的起始位置，如果他们指向的是X，那么都向右移动到不是X的位置，那么他们指向的字符应该相等，否则返回False。如果指向的是L，那么，start中的L的索引一定只能比end中L的索引小；如果指向的是R，那么，end中的R的索引一定只能比end中R的索引大。在while的结束之前需要把i和j同时向后移动。

全部判断完成之后返回True.

时间复杂度是O(N)，空间复杂度是O(1).

```python
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        i, j = 0, 0
        N = len(start)
        while i < N and j < N:
            while i < N - 1 and start[i] == 'X':
                i += 1
            while j < N - 1 and end[j] == 'X':
                j += 1
            if start[i] != end[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
        return True
```


## 相似题目


## 参考资料

http://www.cnblogs.com/grandyang/p/9001474.html

## 日期

2018 年 10 月 30 日 —— 啊，十月过完了


  [1]: https://leetcode.com/static/images/courses/range_sum_query_2d.png
  [2]: https://leetcode.com/static/images/courses/sum_od.png
  [3]: https://leetcode.com/static/images/courses/sum_ob.png
  [4]: https://leetcode.com/static/images/courses/sum_oc.png
  [5]: https://leetcode.com/static/images/courses/sum_oa.png
  [6]: https://blog.csdn.net/fuxuemingzhu/article/details/79253036
