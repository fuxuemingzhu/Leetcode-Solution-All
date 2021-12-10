作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/rectangle-area/description/

## 题目描述：

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

![Rectangle Area][1]

Example:

    Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
    Output: 45

Note:

Assume that the total area is never beyond the maximum possible value of int.

## 题目大意

求两个矩形覆盖的总面积。

## 解题方法

很好理解，总面积等于两个矩形的面积和 - 公共面积。实际上就是让我们求公共面积。

拿到两个矩形的问题，我一般都会先对坐标进行排序，这样的好处是可以使两者的位置相对固定，按照相对顺序的模式求解。排序的方式就是按照四个坐标对应关系去排。因为总的只有两个矩形，排序这步速度很快。

但是这个题并不需要排序也可以，因为求公共面积使用了最小最大值关系，所以没必要排序。事实上，排不排序这一步对时间没有影响，都是56ms，因此我建议还是排序。

公共面积等于``(min(C, G) - max(A, E)) × (min(D, H) - max(B, F))``，从图中很容易看出来。就不讲了。需要注意的是不能把两个直接相乘，因为当两个矩形不想交的时候，这两个部分可能都是负值，相乘得到了正值，误以为相交了，其实没有。所以需要一个判断。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200318114625714.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1eHVlbWluZ3podQ==,size_16,color_FFFFFF,t_70)

时间复杂度是O(1)，空间复杂度是O(1)。

```python
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        points = [((A, B), (C, D)), ((E, F), (G, H))]
        points.sort()
        ((A, B), (C, D)), ((E, F), (G, H)) = points
        area1 = (D - B) * (C - A)
        area2 = (H - F) * (G - E)
        x, y = (min(C, G) - max(A, E)), (min(D, H) - max(B, F))
        area = 0
        if x > 0 and y > 0:
            area = x * y
        return area1 + area2 - area
```


参考资料：


## 日期

2018 年 10 月 8 日 —— 终于开学了。


  [1]: https://leetcode.com/static/images/problemset/rectangle_area.png
