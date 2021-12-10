作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/smallest-range/description/

## 题目描述：

You have ``k`` lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the ``k`` lists.

We define the range ``[a,b]`` is smaller than range ``[c,d]`` if ``b-a < d-c`` or ``a < c`` if ``b-a == d-c``.

Example 1:

    Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    Output: [20,24]
    Explanation: 
    List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
    List 2: [0, 9, 12, 20], 20 is in range [20,24].
    List 3: [5, 18, 22, 30], 22 is in range [20,24].

Note:

1. The given list may contain duplicates, so ascending order means >= here.
1. 1 <= k <= 3500
1. -105 <= value of elements <= 105.
1. For Java users, please note that the input type has been changed to List<List<Integer>>. And after you reset the code template, you'll see this point.

## 题目大意

找出一个最小的区间，这个区间对每个数组都至少包含其中的一个数字。

## 解题方法

这个题是[76. Minimum Window Substring][1]的变形，第76题要我们查找出s中一个最小的窗口，使得这个窗口中包含t的所有字符。如果把本题的nums中的每个数组合并成一个总的数组，那么就是找出一个小的窗口，使得这个窗口包含有不同区间的最少一个字符。

所以把nums放到一个数组里面去，放的过程中需要把这个数组的索引号也放进去。然后就可以通过查找出一个小的区间，这个区间里包含所有数组的索引号了。就是第76题。

使用right指针向右搜索，同时要记录在left～right这个区间内包含的数组个数和。如果在[left,right]区间内，数组个数和的个数和与原始数组个数相等了，说明在这个区间是符合要求的一个区间，但是不一定是最短区间。

因此，现在要移动left指针，要求，在[left, right]区间内的数组出现个数应该把所有的数组个数都进行包含。同样使用cnt来验证是否包含了所有的数组。

在移动left指针的时候要注意存储最短的区间，当所有的循环都结束之后最短区间即为题目要求了。

这个题使用字典保存不同数组出现的次数，以此来维护cnt。

这个题是寻找子字符串的模板题，应该记住。

时间复杂度是O(N*log(N) + N)，空间复杂度是O(N)。其中N是所有数组的长度和。

```python
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        v  = list()
        for i in range(len(nums)):
            for num in nums[i]:
                v.append((num, i))
        v.sort()
        l, r, n = 0, 0, len(v)
        d = collections.defaultdict(int)
        k = len(nums)
        cnt = 0
        res = [0, 0]
        diff = float('inf')
        while r < n:
            if d[v[r][1]] == 0:
                cnt += 1
            d[v[r][1]] += 1
            while l <= r and cnt == k:
                if v[r][0] - v[l][0] < diff:
                    diff = v[r][0] - v[l][0]
                    res = [v[l][0], v[r][0]]
                d[v[l][1]] -= 1
                if d[v[l][1]] == 0:
                    del d[v[l][1]]
                    cnt -= 1
                l += 1
            r += 1
        return res
```

参考资料：

http://www.cnblogs.com/grandyang/p/7200016.html

## 日期

2018 年 10 月 3 日 —— 玩游戏导致没睡好，脑子是浆糊。


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82931106
