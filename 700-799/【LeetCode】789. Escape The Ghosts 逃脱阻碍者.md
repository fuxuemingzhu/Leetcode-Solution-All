
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/escape-the-ghosts/description/

## 题目描述

You are playing a simplified Pacman game. You start at the point ``(0, 0)``, and your destination is ``(target[0], target[1])``. There are several ghosts on the map, the i-th ghost starts at ``(ghosts[i][0], ghosts[i][1])``.

Each turn, you and all ghosts simultaneously ``*may*`` move in one of 4 cardinal directions: north, east, west, or south, going from the previous point to a new point 1 unit of distance away.

You escape if and only if you can reach the target before any ghost reaches you (for any given moves the ghosts may take.)  If you reach any square (including the target) at the same time as a ghost, it doesn't count as an escape.

Return True if and only if it is possible to escape.

Example 1:

    Input: 
    ghosts = [[1, 0], [0, 3]]
    target = [0, 1]
    Output: true
    Explanation: 
    You can directly reach the destination (0, 1) at time 1, while the ghosts located at (1, 0) or (0, 3) have no way to catch up with you.
    
Example 2:

    Input: 
    ghosts = [[1, 0]]
    target = [2, 0]
    Output: false
    Explanation: 
    You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you and the destination.
    
Example 3:

    Input: 
    ghosts = [[2, 0]]
    target = [1, 0]
    Output: false
    Explanation: 
    The ghost can reach the target at the same time as you.

Note:

1. All points have coordinates with absolute value <= 10000.
1. The number of ghosts will not exceed 100.

## 题目大意

这是吃豆人游戏。角色和鬼魂一起在地图上游荡，可以有上下左右四个移动方向。注意，也可以不移动。如果碰到了鬼魂就输了。看有没有一种可能，在不碰到鬼魂的情况下到达target.

## 解题方法

我看到这个题考的是math就不想做了。。参考了[书影博客][2]的做法。直接考虑曼哈顿距离即可。

可以这么考虑，在地图上有很多鬼魂都往target上走，只要有鬼魂提前到了target，然后它就在那里等着你就好了！

所以，解题方法是你到target的距离比任何鬼魂到target的距离都小～～

```python
class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        mht = sum(map(abs, target))
        tx, ty = target
        return not any(abs(gx - tx) + abs(gy - ty) <= mht for gx, gy in ghosts)
```

二刷的时候想到了这个是考曼哈顿距离，是否存在小鬼离target的距离比source离target的距离小。

C++代码如下：

```cpp
class Solution {
public:
    bool escapeGhosts(vector<vector<int>>& ghosts, vector<int>& target) {
        int time = distance({0, 0}, target);
        for (auto g : ghosts) {
            if (distance(g, target) <= time)
                return false;
        }
        return true;
    }
private:
    int distance(vector<int> source, vector<int>& target) {
        return abs(target[0] - source[0]) + abs(target[1] - source[1]);
    }
};
```


## 日期

2018 年 5 月 28 日 ———— 太阳真的像日光灯～
2018 年 12 月 11 日 —— 双十一已经过去一个月了，真快啊。。

  [2]: http://bookshadow.com/weblog/2018/02/25/leetcode-escape-the-ghosts/
