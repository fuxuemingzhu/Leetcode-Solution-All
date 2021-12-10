

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/robot-bounded-in-circle/

## 题目描述

On an infinite plane, a robot initially stands at ``(0, 0)`` and faces ``north``.  The robot can receive one of three instructions:

- "G": go straight 1 unit;
- "L": turn 90 degrees to the left;
- "R": turn 90 degress to the right.

The robot performs the instructions given in order, and repeats them forever.

Return `true` if and only if there exists a circle in the plane such that the robot never leaves the circle.


Example 1:

    Input: "GGLLGG"
    Output: true
    Explanation: 
    The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
    When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:

    Input: "GG"
    Output: false
    Explanation: 
    The robot moves north indefinitely.

Example 3:

    Input: "GL"
    Output: true
    Explanation: 
    The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 

Note:

1. 1 <= instructions.length <= 100
1. instructions[i] is in `{'G', 'L', 'R'}`


## 题目大意

机器人初始位置在原点，面向北。接受到一串指令，G代表直走1步；L代表左转；R代表右转。指令会无限的循环下去。问是否会有一个圆，把机器人的路径包括？


## 解题方法

### 找规律

我们一定知道，这个题不能用暴力解法。机器人的路径最终被圆包括的充分条件是机器在一些指令之后回到原点。由于指令是循环的，题目只给出了部分指令。那么对于该部分指令的要求是，机器人`回到了原点`或者`不再原点且不面向北`。

回到原点很好理解，那么`不再原点且不面向北`是什么意思呢？

如果题目中的指令结束之后，机器人不在原点，那么说明它相对原点移动了一个向量v。机器人在指令结束后的位置成为了新的原点，题目说机器人的初始状态时是面向北的，那么如果在新的原点上仍然面向北，那么一定还会继续向第一次一样相对新的原点移动相同的向量v，此时机器人距原点的向量是2v。

那么为什么不面向北就一定能回到原点呢？这是由于在新的原点新的方向上再次接受相同指令后，机器人移动新向量的长度为|向量v|、方向和v成90度或者180度；多次指令的结果叠加就会抵消第一次移动的v。


Python代码如下：

```python
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        x, y = 0, 0
        curd = 0
        for i in instructions:
            if i == "G":
                x += dirs[curd][0]
                y += dirs[curd % 4][1]
            elif i == "L":
                curd = (curd + 1) % 4
            elif i == "R":
                curd = (curd - 1) % 4
        return (x == 0 and y == 0) or curd != 0
```

从上面的说明中我们看出来，如果要把第一次的向量v进行抵消，那么指令最多重复4次即可。即该机器人的路径能不能形成圆的充分必要条件是该指令重复4次后机器人能回到原点。

```python
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        x, y = 0, 0
        curd = 0
        for i in instructions * 4:
            if i == "G":
                x += dirs[curd][0]
                y += dirs[curd % 4][1]
            elif i == "L":
                curd = (curd + 1) % 4
            elif i == "R":
                curd = (curd - 1) % 4
        return x == 0 and y == 0
```


参考资料：
https://leetcode.com/problems/robot-bounded-in-circle/discuss/304977/1041.-C-Solution-Beats-100-Runtime-and-100-Memory-(with-explanation)

## 日期

2019 年 6 月 15 日 —— 今天这个题有意思
