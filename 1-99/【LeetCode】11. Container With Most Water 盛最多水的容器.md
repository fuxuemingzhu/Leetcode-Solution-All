
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)
- 个人公众号：负雪明烛
- 本文关键词：盛水，容器，题解，leetcode, 力扣，python, c++, java

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/container-with-most-water/description/

## 题目描述

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 
![此处输入图片的描述][1]


The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

Example:

    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49

## 题目大意

有很多挡板，从这些挡板中选两个，然后计算能够成的面积的最大值。

## 解题方法

### 双指针

如果纯暴力计算两两之间的面积，时间复杂度是O(N^2)，肯定会超时。

一个比较好的解决的方法是，使用双指针方法，一个从最左边开始，一个从最右边开始，计算两个挡板之间的面积，然后在向中间移动。移动的规则是这样的，如果哪个挡板比较矮，就舍弃掉这个挡板，把指向这个挡板的指针向中间移动。

这样的移动方式是我们每次都保留了比较长的哪个挡板，也就能获得更多的水。当两个挡板的高度一样的话，移动任意一个即可，因为这两个是高度一样的挡板，如果中间有更高的挡板，那么当前的挡板决定了以后的挡板的最低值，也就是说以其中任意一个为边界的容器面积不可能超过当前的当前的值。

我们在遍历的过程中需要保留遍历时候得到的最大值，最后返回即可。

时间复杂度是O(N)，空间复杂度是O(1).

代码如下：

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
```

参考资料：

https://www.youtube.com/watch?v=IONgE6QZgGI
https://leetcode.com/articles/container-with-most-water/
https://leetcode.windliang.cc/leetCode-11-Container-With-Most-Water.html

## 日期

2018 年 9 月 23 日 —— 今天是实验室第一个打卡的


  [1]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
