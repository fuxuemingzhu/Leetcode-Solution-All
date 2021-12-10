
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/battleships-in-a-board/description/


## 题目描述

Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

Example:

    X..X
    ...X
    ...X
    In the above board there are 2 battleships.

Invalid Example:

    ...X
    XXXX
    ...X
    This is an invalid board that you will not receive - as battleships will always have a cell separating between them.

Follow up:

- Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

## 题目大意

战列舰计数。第一遍看这个题的时候看不懂，看了别人的解答，我算是明白了，就是求用x组成的区域有几个。单独的一个或者连续的一条线都算一个。另外就是战列舰不会交叉，不会平行。

## 解题方法

方法比较简单，直接数就行。如果一个位置有x，并且（这个位置在最左边或者不在最左边但是该位置左侧是.），并且（这个位置在最上边或者不在最上边但是该位置上侧是.），那么就是一个新的战列舰，计数即可。

```python
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if len(board) == 0 or len(board[0]) == 0:
            return 0
        row, col = len(board), len(board[0])
        count = 0
        for i in xrange(row):
            for j in xrange(col):
                if board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                    count += 1
        return count
```

C++版本代码如下

```cpp
class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int M = board.size();
        int N = board[0].size();
        int res = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 'X' && (i == 0 || board[i - 1][j] == '.') && (j == 0 || board[i][j - 1] == '.'))
                    res ++;
            }
        }
        return res;
    }
};
```

## 日期

2018 年 2 月 28 日 
2018 年 12 月 2 日 —— 又到了周日
