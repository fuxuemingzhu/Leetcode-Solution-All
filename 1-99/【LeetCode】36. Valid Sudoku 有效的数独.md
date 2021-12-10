# 【LeetCode】36. Valid Sudoku 解题报告（Python）

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址：https://leetcode.com/problems/valid-sudoku/description/

## 题目描述：

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
1. Each column must contain the digits 1-9 without repetition.
1. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

![此处输入图片的描述][1]

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

    Input:
    [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    Output: true

Example 2:

    Input:
    [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being 
        modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:

1. A Sudoku board (partially filled) could be valid but is not necessarily solvable.
1. Only the filled cells need to be validated according to the mentioned rules.
1. The given board contain only digits 1-9 and the character '.'.
1. The given board size is always 9x9.

## 题目大意

判断一个9*9的二维数组是不是一个有效的数独。只用判断有效即可，即题目中的三个条件，不用求解。

## 解题方法

如果只判断有效的话，实现三个函数分别对应三个条件即可：判断行，判断列，判断9宫格。

把要判断的这些位置的数字取出来，然后用set后的长度是否等于原长度就能知道是不是有重复数字了。题目中已经说了给出的数字只有1~9，所以省掉了很多事。判断之前需要把'.'给去掉，因为数字只允许出现一次，而'.'可能出现多次。

时间复杂度是O(N^2)，空间复杂度是O(N).

代码如下：

```python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)
        return self.isValidRow(board) and self.isValidCol(board) and self.isValidNineCell(board)
        
    def isValidRow(self, board):
        n = len(board)
        for r in range(n):
            row = [x for x in board[r] if x != '.']
            if len(set(row)) != len(row):
                return False
        return True

    def isValidCol(self, board):
        n = len(board)
        for c in range(n):
            col = [board[r][c] for r in range(n) if board[r][c] != '.']
            if len(set(col)) != len(col):
                return False
        return True

    def isValidNineCell(self, board):
        n = len(board)
        for r in range(0, n, 3):
            for c in range(0, n, 3):
                cell = []
                for i in range(3):
                    for j in range(3):
                        num = board[r + i][c + j]
                        if num != '.':
                            cell.append(num)
                if len(set(cell)) != len(cell):
                    return False
        return True
```

参考资料：


## 日期

2018 年 9 月 22 日 —— 周末加班


  [1]: https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png
