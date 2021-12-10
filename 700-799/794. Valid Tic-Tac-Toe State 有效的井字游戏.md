作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/valid-tic-tac-toe-state/description/

## 题目描述：

A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.

Example 1:

    Input: board = ["O  ", "   ", "   "]
    Output: false
    Explanation: The first player always plays "X".

Example 2:

    Input: board = ["XOX", " X ", "   "]
    Output: false
    Explanation: Players take turns making moves.

Example 3:

    Input: board = ["XXX", "   ", "OOO"]
    Output: false

Example 4:

    Input: board = ["XOX", "O O", "XOX"]
    Output: true

Note:

1. board is a length-3 array of strings, where each string board[i] has length 3.
1. Each board[i][j] is a character in the set {" ", "X", "O"}.


## 题目大意

判断一个棋盘是不是有效的井字棋的状态。

## 解题方法

判断是否是个合法的状态，我只需要排除不合法的状态就好了。不合法的状态分为三种情况：

1. 初始的棋盘上O的个数不等于X的个数，或者O的个数不等于X-1；
2. 棋盘上O的个数等于X - 1（轮到O下），但是O还没下棋，此时O已经赢了；
3. 棋盘上O的个数等于X（轮到X下），但是X还没下棋，此时X已经赢了；

除此之外，就能下棋，或者棋局已经结束。

时间复杂度是O(N^2)，空间复杂度是O(1)。N是棋盘变长。

```python
class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        xCount, oCount = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'O':
                    oCount += 1
                elif board[i][j] == 'X':
                    xCount += 1
        if oCount != xCount and oCount != xCount - 1: return False
        if oCount != xCount and self.win(board, 'O'): return False
        if oCount != xCount - 1 and self.win(board, 'X'): return False
        return True
        
    def win(self, board, P):
        # board is list[str]
        # P is 'X' or 'O' for two players
        for j in range(3):
            if all(board[i][j] == P for i in range(3)): return True
            if all(board[j][i] == P for i in range(3)): return True
        if board[0][0] == board[1][1] == board[2][2] == P: return True
        if board[0][2] == board[1][1] == board[2][0] == P: return True
        return False
```


参考资料：


## 日期

2018 年 10 月 14 日 —— 美好的周一怎么会出现雾霾呢？
