
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/magic-squares-in-grid/description/

## 题目描述

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers ``from 1 to 9`` such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:
    
    Input: [[4,3,8,4],
            [9,5,1,9],
            [2,7,6,2]]
    Output: 1
    
    Explanation: 
    
    The following subgrid is a 3 x 3 magic square:
    438
    951
    276
    
    while this one is not:
    384
    519
    762
    
    In total, there is only one magic square inside the given grid.

Note:

- 1 <= grid.length <= 10
- 1 <= grid[0].length <= 10
- 0 <= grid[i][j] <= 15

## 题目大意

判断一个大矩阵中有多少``河图``。河图这个词很古典文化，其实就是1到9填在9个格子中，让横竖斜的3个数相加都相等。

## 解题方法

### 利用河图规律

直接按照河图的规定去做就OK了。用到了一个结论：河图的中心数字是5.

注意一个易忽略的点，就是所有的数字应该在1~9之间。测试用例里面出现了不在这个范围内的数字也能组成河图。

另外，关于河图，其实有很多有用的结论，我并没有使用。

河图记忆方法：**偶角奇边坐心五.一线双角相对画.**

这个帖子挺有意思的：[1到9填在9个格子中，让横竖斜的3个数相加都相等][1]


```python
class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        counter = 0
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                sub_matrix = [[grid[row + i][col + j] for j in range(3)] for i in range(3)]
                if self.magic_square(sub_matrix):
                    counter += 1
        return counter

    def magic_square(self, matrix):
        is_number_right = all(1 <= matrix[i][j] <= 9 for i in range(3) for j in range(3))
        is_row_right = all(sum(row) == 15 for row in matrix)
        is_col_right = all(sum(col) == 15 for col in [[matrix[i][j] for i in range(3)] for j in range(3)])
        is_diagonal_right = matrix[1][1] == 5 and matrix[0][0] + matrix[-1][-1] == 10 and matrix[0][-1] + matrix[-1][0] == 10
        is_repeat_right = len(set(matrix[i][j] for i in range(3) for j in range(3))) == 9
        return is_number_right and is_row_right and is_col_right and is_diagonal_right and is_repeat_right
```

### 暴力解法

二刷的时候完全忘了什么性质了……直接暴力解法，这样的话，需要按照题目做各种判断，所以函数更为复杂了。

```python
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        res = 0
        for r in range(M - 2):
            for c in range(N - 2):
                curgrid = [[grid[r + i][c + j] for j in range(3)] for i in range(3)]
                if self.isMagic(curgrid):
                    res += 1
        return res

        
    def isMagic(self, grid):
        count = list(range(9))
        for i in range(3):
            for j in range(3):
                if not (1 <= grid[i][j] <= 9):
                    return False
                count[grid[i][j] - 1] += 1
        if 0 in count: return False
        row, col = [0, 0, 0], [0, 0, 0]
        for i in range(3):
            row[i] += sum(grid[i][j] for j in range(3))
        for j in range(3):
            col[j] += sum(grid[i][j] for i in range(3))
        if row[0] != row[1] != row[2] or col[0] != col[1] != col[2]:
            return False
        if grid[0][0] + grid[2][2] != grid[0][2] + grid[2][0]:
            return False
        return True
```

## 日期

2018 年 5 月 27 日 —— 周末的天气很好～
2018 年 11 月 24 日 —— 周六快乐

  [1]: https://blog.csdn.net/firefly_2002/article/details/7886989
