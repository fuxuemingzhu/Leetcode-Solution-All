# 【LeetCode】554. Brick Wall 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/brick-wall/description/

## 题目描述：

There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Example:
    Input: 
    
    [[1,2,2,1],
     [3,1,2],
     [1,3,2],
     [2,4],
     [3,1,2],
     [1,3,1,1]]
     
    Output: 2
    
Explanation: 
![此处输入图片的描述][1]


Note:

1. The width sum of bricks in different rows are the same and won't exceed INT_MAX.
1. The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000.


## 题目大意

这个题目给出了一个二维数组，代表了每层的每块砖的长度。要我们沿着竖直方向画一条线，这条线尽可能的穿过最少的砖块。

## 解题方法

尽可能少的穿过砖块，也就是画一条线能经过更多的砖块之间的空隙（两头不算）。那么思路就转成了，我们要统计出所有的位置中，哪里的空隙出现的次数最多。

所以，我们从上到下遍历每层，从左到右遍历每个砖块的边缘，用hashmap保存每个边缘和左边界的距离以及该位置出现的次数。那么我们只要找出某个空隙的位置出现的次数最多就好。

由于是求穿过的砖块的个数，所以需要用砖块的行数减去孔隙数。

代码如下：

```python
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        left_counter = collections.Counter()
        count = 0
        for row in wall:
            left = 0
            for i in range(len(row) - 1):
                left += row[i]
                left_counter.update([left])
                count = max(count, left_counter[left])
        return len(wall) - count
```

## 日期

2018 年 5 月 31 日 ———— 太阳暴晒，明天就要过儿童节了。激动


  [1]: https://leetcode.com/static/images/problemset/brick_wall.png