

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/walking-robot-simulation/description/

## 题目描述

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

- ``-2``: turn left 90 degrees
- ``-1``: turn right 90 degrees
- ``1 <= x <= 9``: move forward x units

Some of the grid squares are obstacles. 

The ``i-th`` obstacle is at grid point ``(obstacles[i][0], obstacles[i][1])``

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.

 

Example 1:

    Input: commands = [4,-1,3], obstacles = []
    Output: 25
    Explanation: robot will go to (3, 4)

Example 2:

    Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
    Output: 65
    Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)
     

Note:

1. 0 <= commands.length <= 10000
1. 0 <= obstacles.length <= 10000
1. -30000 <= obstacle[i][0] <= 30000
1. -30000 <= obstacle[i][1] <= 30000
1. The answer is guaranteed to be less than 2 ^ 31.


## 题目大意

一个机器人初始位置在（0,0）坐标，面朝北边。下面的移动方式是按照command来操作的，如果command==-2，左转；如果command==-1，右转；如果其他的正值，就对应了向前移动对应的步数。

另外，某些位置上会有障碍物，遇到障碍物他就只能停在前一个位置，等着下一个操作。

最后求，这个机器人离原点的坐标的笛卡尔距离的平方最大值，即max(x^2 + y^2)。

## 解题方法

### 模拟

按照这个操作如实的过一遍就行了，这里边难点是怎么判断障碍物，其实最直接的方法就是一步一步的移动，然后判断是否有障碍物，同时在每个位置都去计算距离的最大值。判断障碍物使用set可以做到线性时间复杂度。

整个算法的时间复杂度是O(MN)，其中M是命令数，N是障碍物数。在题目中估算大概是1亿的样子，没想到这样也能过。

代码如下：

```python
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # directions = ['N', 'E', 'S', 'W']
        # 0 - N, 1 - E, 2 - S, 3 - W
        position_offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacles = set(map(tuple, obstacles))
        x, y, direction, max_distance = 0, 0, 0, 0
        for command in commands:
            if command == -2: direction = (direction - 1) % 4
            elif command == -1: direction = (direction + 1) % 4
            else:
                x_off, y_off = position_offset[direction]
                while command:
                    if (x + x_off, y + y_off) not in obstacles:
                        x += x_off
                        y += y_off
                    command -= 1
                max_distance = max(max_distance, x**2 + y**2)
        print(x, y)
        return max_distance
```

二刷使用C++写了一遍，python支持列表的负索引，但是C++数组是不支持的，所以求下一个方向移动的时候，需要使用+3代替-1.

```cpp
class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        int res = 0;
        int dx[4] = {0, 1, 0, -1};
        int dy[4] = {1, 0, -1, 0};
        set<pair<int, int>> obs;
        for (auto ob : obstacles) {
            obs.insert(make_pair(ob[0], ob[1]));
        }
        int x = 0, y = 0;
        int d = 0;
        for (int command : commands) {
            if (command == -1) {
                d = (d + 1) % 4;
            } else if (command == -2) {
                d = (d + 3) % 4;
            } else {
                while (command--){
                    int nx = x + dx[d];
                    int ny = y + dy[d];
                    if (obs.find(make_pair(nx, ny)) != obs.end()){
                        break;
                    }
                    x = nx;
                    y = ny;
                    res = max(res, x * x + y * y);
                }
            }
        }
        return res;
    }
};
```

参考资料：

https://leetcode.com/problems/walking-robot-simulation/discuss/157505/Simple-Python-solution-Accepted

## 日期

2018 年 9 月 3 日 ———— 新学期开学第一天！
