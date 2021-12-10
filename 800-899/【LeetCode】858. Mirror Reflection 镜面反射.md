
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/mirror-reflection/description/

## 题目描述

There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)

 

Example 1:

    Input: p = 2, q = 1
    Output: 2
    Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

![此处输入图片的描述][1]

Note:

1. 1 <= p <= 1000
1. 0 <= q <= p


## 题目大意

有个正方形的玻璃房子，从左下角射出一个光线，光线第一次打在右边墙上的高度是q。正方形边长是p，求最终这个光线射在了0,1,2的哪个位置。

## 解题方法

利用正方形的性质，其实可以看成两个平行的无限长的镜子。

![此处输入图片的描述][2]

找出``m * p = n * q``

m 是房子的拓展次数 + 1
n 是反射的拓展次数 + 1

显而易见，m 和 n 不可能都是偶数，否则会在之前就相遇。所以判断：

1. 如果，光的反射是奇数，则n是偶数，所以角落在左手边，只能是2.
1. 如果，光的反射是偶数，则n是偶数，所以角落在右手边，可能是0和1。在此基础上，如果房子的拓展是偶数，则m是奇数，所以角落是1，否则角落是0.

即：

    m is even & n is odd => return 0.
    m is odd & n is odd => return 1.
    m is odd & n is even => return 2.

代码如下：

```python
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        m, n = q, p
        while m % 2 == 0 and n % 2 == 0:
            m, n = m / 2, n / 2
        if m % 2 == 0 and n % 2 == 1:
            return 0
        elif m % 2 == 1 and n % 2 == 1:
            return 1
        elif m % 2 == 1 and n % 2 == 0:
            return 2
```


参考资料：

https://leetcode.com/problems/mirror-reflection/discuss/146336/Java-solution-with-an-easy-to-understand-explanation

## 日期

2018 年 9 月 5 日 —— 忙碌的一天
2018 年 12 月 16 日 —— 周赛好难

  [1]: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/18/reflection.png
  [2]: https://s3-lc-upload.s3.amazonaws.com/users/motorix/image_1529877876.png
