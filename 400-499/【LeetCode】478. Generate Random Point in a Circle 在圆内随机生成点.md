作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/generate-random-point-in-a-circle/description/

## 题目描述：

Given the radius and x-y positions of the center of a circle, write a function ``randPoint`` which generates a uniform random point in the circle.

Note:

1. input and output values are in floating-point.
1. radius and x-y position of the center of the circle is passed into the class constructor.
1. a point on the circumference of the circle is considered to be in the circle.
1. ``randPoint`` returns a size 2 array containing x-position and y-position of the random point, in that order.

Example 1:

    Input: 
    ["Solution","randPoint","randPoint","randPoint"]
    [[1,0,0],[],[],[]]
    Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

Example 2:

    Input: 
    ["Solution","randPoint","randPoint","randPoint"]
    [[10,5,-7.5],[],[],[]]
    Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if there aren't any.

## 题目大意

给定圆的圆心和半径，生成落在这个圆里面的随机点。

## 解题方法

比较简单的方法是拒绝采样（Rejection Sampling），先在圆的外接圆内随机采点，然后判断这个点是不是在圆内，如果是的话就返回，否则再取一次。这个方法还可以用来估计圆周率。方法就不写了。

我直觉的方法还是使用极坐标的方式，随机找半径、随机找角度，然后就确定了一个点。但是没有通过最后一个测试用例。如果不查资料我是不会发现，这个做法是错的！

直接对半径和角度进行随机采样的方式会使得靠近圆心的点被取到的概率偏大，结果是取点的概率在这个圆内不是均匀的。为什么呢？因为题目要求的是对圆内任何面积上的点是均匀分布的，而不是对圆心出发的半径上是均匀分布的。那么以圆心为半径的小圆的范围内的点密度一定会比更大圆的密度大。

下图中左侧是随机生成半径和角度构成的点，右侧是随即生成的半径取根号和角度构成的点。

![此处输入图片的描述][1]

正确的做法是对边的随机数求根号。具体做法需要看[478. Generate Random Point in a Circle（随机）][2]

那么这个事情应该怎么理解呢？

首先我们要明白，题目要我们产生的是在圆内产生均匀的点，也就是说，对于圆中**任意小的面积内**落入点的概率相等。注意刚才说的是任意面积落点的概率是相等的。而如果采用随机半径+随机角度的方式，那么在**任意半径上**落入点的概率相等。很明显的是靠近圆心的半径比较密，远离圆心的时候半径比较稀疏。（类比一下太阳，太阳表面光线密度最大也就最亮，随着光线的传播，距离越远，光的亮度越小。）

右图这种对半径去根号的为什么是对的呢？因为我们产生的随机数是在0~1之间，那么去了根号之后会使得生成的点在1附近的密度更大，在0附近的密度变小。直觉上来看，那就是使得半径最外边被取到的概率变大，在圆心附近被取到的概率变小了。从而修正了圆心取到的点更密集的问题。

时间复杂度是O(1)，空间复杂度是O(1)。

```python
class Solution:

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        nr = math.sqrt(random.random()) * self.r
        alpha = random.random() * 2 * 3.141592653
        newx = self.x + nr * math.cos(alpha)
        newy = self.y + nr * math.sin(alpha)
        return [newx, newy]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
```

C++代码如下：

```cpp
class Solution {
public:
    Solution(double radius, double x_center, double y_center) {
        rad = radius;
        x = x_center;
        y = y_center;
    }
    
    vector<double> randPoint() {
        const double PI = 3.141592653;
        double nr = sqrt(rand() / double(RAND_MAX)) * rad;
        double alpha = rand() / double(RAND_MAX) * 2 * PI;
        double nx = x + nr * cos(alpha);
        double ny = y + nr * sin(alpha);
        return {nx, ny};
    }
private:
    double rad;
    double x, y;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj.randPoint();
 */
```



参考资料：

https://zhanghuimeng.github.io/post/leetcode-478-generate-random-point-in-a-circle/

## 日期

2018 年 10 月 14 日 —— 周赛做出来3个题，开心
2019 年 2 月 1 日 —— 2019已经过去了一个月

  [1]: https://zhanghuimeng.github.io/post/leetcode-478-generate-random-point-in-a-circle/distribution.jpg
  [2]: https://zhanghuimeng.github.io/post/leetcode-478-generate-random-point-in-a-circle/
