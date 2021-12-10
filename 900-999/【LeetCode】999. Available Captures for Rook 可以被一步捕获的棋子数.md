作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/available-captures-for-rook/


## 题目描述

On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.


Example 1:

![此处输入图片的描述][1]

    Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    Output: 3
    Explanation: 
    In this example the rook is able to capture all the pawns.

Example 2:

![此处输入图片的描述][2]

    Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    Output: 0
    Explanation: 
    Bishops are blocking the rook to capture any pawn.

Example 3:

![此处输入图片的描述][3]
    
    Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
    Output: 3
    Explanation: 
    The rook can capture the pawns at positions b5, d6 and f5.
 

Note:

1. board.length == board[i].length == 8
1. board[i][j] is either 'R', '.', 'B', or 'p'
1. There is exactly one cell with board[i][j] == 'R'

## 题目大意

在一个国际象棋的棋盘上，有一个白车(``R``)，有若干白象（``B``）、黑卒（``p``），其余是空白（``.``），问这个白车在只移动一次的情况下，能吃掉哪几个黑卒。

## 解题方法

### 暴力遍历

棋盘只有8*8，只有一个白车，所以做法可以很简单地从白车出发，向四个方向进行搜索即可！

C++代码如下：

```cpp
class Solution {
public:
    int numRookCaptures(vector<vector<char>>& board) {
        const int N = 8;
        pair<int, int> pos;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (board[i][j] == 'R') {
                    pos.first = i;
                    pos.second = j;
                    break;
                }
            }
        }
        vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int res = 0;
        for (int i = pos.first + 1; i < N; ++i) {
            if (board[i][pos.second] == 'B')
                break;
            if (board[i][pos.second] == 'p') {
                ++res;
                break;
            }
        }
        for (int i = pos.first - 1; i >= 0; --i) {
            if (board[i][pos.second] == 'B')
                break;
            if (board[i][pos.second] == 'p') {
                ++res;
                break;
            }
        }
        for (int j = pos.second + 1; j < N; ++j) {
            if (board[pos.first][j] == 'B')
                break;
            if (board[pos.first][j] == 'p') {
                ++res;
                break;
            }
        }
        for (int j = pos.second - 1; j >= 0; --j) {
            if (board[pos.first][j] == 'B')
                break;
            if (board[pos.first][j] == 'p') {
                ++res;
                break;
            }
        }
        return res;
    }
};
```

## 日期

2019 年 2 月 24 日 —— 周末又结束了


  [1]: https://assets.leetcode.com/uploads/2019/02/20/1253_example_1_improved.PNG
  [2]: https://assets.leetcode.com/uploads/2019/02/19/1253_example_2_improved.PNG
  [3]: https://assets.leetcode.com/uploads/2019/02/20/1253_example_3_improved.PNG
