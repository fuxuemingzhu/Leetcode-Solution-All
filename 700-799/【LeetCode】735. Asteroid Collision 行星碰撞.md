
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/asteroid-collision/description/

## 题目描述

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

    Input: 
    asteroids = [5, 10, -5]
    Output: [5, 10]
    Explanation: 
    The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Example 2:

    Input: 
    asteroids = [8, -8]
    Output: []
    Explanation: 
    The 8 and -8 collide exploding each other.

Example 3:

    Input: 
    asteroids = [10, 2, -5]
    Output: [10]
    Explanation: 
    The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.

Example 4:

    Input: 
    asteroids = [-2, -1, 1, 2]
    Output: [-2, -1, 1, 2]
    Explanation: 
    The -2 and -1 are moving left, while the 1 and 2 are moving right.
    Asteroids moving the same direction never meet, so no asteroids will meet each other.

Note:

- The length of asteroids will be at most 10000.
- Each asteroid will be a non-zero integer in the range [-1000, 1000]..

## 题目大意

在同一轨道上有一堆小行星，列表给出的是他们的体积。数字的正负代表了他们的移动方向，同样方向的不会相撞，相同方向的会相撞。当相撞时，体积大小相等的两个都会消失，否则就是体积小的小时。求稳定之后留下来的行星。

## 解题方法

### 栈

当我们意识到，行星是两两之间互相作用的，那我们很容易就想到了用栈。因为栈能处理这样抵消和遗留的问题。

算法的思想是，从左到右遍历每个行星，并和栈顶数字相比较，当栈顶数字为正（向右），当前数字为负（向左）的时候，会发生碰撞。这时候，判断遗留下来的数字是多少，保存到ast里，如果ast为空代表啥都没有了，如果ast质量大于栈顶元素会留下来ast，否则留下pre。判断ast是否为空，不为空就把遗留下来的数字进栈就好了。

自己犯下的一个严重错误：12行写成了ast == None，检查了n多遍都没检查出来错误！所以刷题写代码一定要一气呵成，不要分心啊！

代码如下：

```python
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] >= 0:
                pre = stack.pop()
                if ast == -pre:
                    ast = None
                    break
                elif -ast < pre:
                    ast = pre
            if ast != None:
                stack.append(ast)
        return stack
```

使用C++写的代码如下，使用了一个bool型变量，表示现在的行星需不需要入栈。默认情况下是需要入栈的，但是当行星质量小于等于栈顶元素的时候，自己就消失了，也就不用入栈了。C++的stack转成vector不太方便，所以我直接使用vector了。

代码如下：

```cpp
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> s;
        for (int a : asteroids) {
            bool ispush = true;
            while (!s.empty() && a < 0 && s.back() > 0) {
                int t = s.back();
                if (abs(a) > abs(t)) {
                    s.pop_back();
                } else if (abs(a) == abs(t)) {
                    s.pop_back();
                    ispush = false;
                    break;
                } else {
                    ispush = false;
                    break;
                }
            }
            if (ispush)
                s.push_back(a);
        }
        return s;
    }
};
```

## 日期

2018 年 7 月 17 日 —— 连天大雨，这种情况很少见，但是很舒服
2018 年 12 月 26 日 —— 转眼就周三了，一万年太久，只争朝夕

  [1]: http://www.cnblogs.com/grandyang/p/7500082.html
