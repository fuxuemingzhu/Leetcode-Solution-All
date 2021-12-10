作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/minimum-time-difference/description/

## 题目描述：

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

    Example 1:
    Input: ["23:59","00:00"]
    Output: 1

Note:

1. The number of time points in the given list is at least 2 and won't exceed 20000.
1. The input time is legal and ranges from 00:00 to 23:59.


## 题目大意

给出了一个时间数组，找出这个数组中最接近的两个时间的差。

## 解题方法

容易想到时间是个循环，正如题目中的所示，需要考虑循环问题。所以解决的方案是先求出每个时间点超出0点的分钟数，对时间进行排序。然后采取zip循环的方式，找出每两个时间之间的时间差，求最小值即可。

注意对24小时的分钟总数进行了求余，这样能保证题目中所示的例子能得到正确结果。

补充一下zip的用法：

```python
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
>>> zip(*zipped)          # 与 zip 相反，可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]
```

代码如下：

```python
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])
        timePoints = map(convert, timePoints)
        timePoints.sort()
        return min((y - x) % (24 * 60)  for x, y in zip(timePoints, timePoints[1:] + timePoints[:1]))
```

参考资料：https://leetcode.com/problems/minimum-time-difference/discuss/100637/Python-Straightforward-with-Explanation

## 日期

2018 年 5 月 31 日 ———— 太阳暴晒，明天就要过儿童节了。激动
