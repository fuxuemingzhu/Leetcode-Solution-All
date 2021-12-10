# 【LeetCode】657. Judge Route Circle

标签（空格分隔）： LeetCode

---

题目地址：[https://leetcode.com/problems/judge-route-circle/description/][1]


## 题目描述：

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false

## Ways

python里面表达坐标比较简单，直接用列表就可以。

这个题就是判断移动了几次之后是否在原来的位置，只要每步都去修改一次即可。

方法一，O(n)：
```python
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        position = [0, 0]
        for move in moves:
            if move == 'R':
                position[0] += 1
            if move == 'L':
                position[0] -= 1
            if move == 'U':
                position[1] += 1
            if move == 'D':
                position[1] -= 1
        return position == [0, 0]
```

方法二，数左右移动的次数和上下移动的次数是否相等：
```python
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
```

方法三，看了Discuss才知道，python原来也可以用复数！
```python
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        directs = {'L':-1, 'R':1, 'U':1j, 'D':-1j}
        return 0 == sum(directs[move] for move in moves)
```

## Date

2018 年 1 月 13 日 


  [1]: https://leetcode.com/problems/judge-route-circle/description/