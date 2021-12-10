
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/minesweeper/description/

## 题目描述

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. **'M'** represents an unrevealed mine, **'E'** represents an unrevealed empty square, **'B'** represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally **'X'** represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

1. If a mine ('M') is revealed, then the game is over - change it to 'X'.
2. If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
3. If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
4. Return the board when no more squares will be revealed.

Example 1:

    Input: 
    
    [['E', 'E', 'E', 'E', 'E'],
     ['E', 'E', 'M', 'E', 'E'],
     ['E', 'E', 'E', 'E', 'E'],
     ['E', 'E', 'E', 'E', 'E']]
    
    Click : [3,0]
    
    Output: 
    
    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'M', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]
    
    Explanation:
    
![此处输入图片的描述][1]
    
Example 2:

    Input: 
    
    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'M', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]
    
    Click : [1,2]
    
    Output: 
    
    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'X', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]

    Explanation:
![此处输入图片的描述][2]


Note:

1. The range of the input matrix's height and width is [1,50].
1. The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
1. The input board won't be a stage when game is over (some mines have been revealed).
1. For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.
    
## 题目大意

给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。

现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

1. 如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
2. 如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的方块都应该被递归地揭露。
3. 如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
4. 如果在此次点击中，若无更多方块可被揭露，则返回面板。
 

## 解题方法
### DFS

这个题标准的做法就是DFS或者BFS，如果使用DFS则按照题目所说的4种情况依次判断就行。

需要注意的是，如果挖出一个空的方块'E'，那么需要递归所有的相邻方块，即继续调用updateBoard函数，把周围的方块都点一下。

Python代码：

```python
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        (row, col), directions = click, ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            if board[row][col] == 'M':
                board[row][col] = 'X'
            elif board[row][col] == 'E':
                n = sum([board[row + r][col + c] == 'M' for r, c in directions if 0 <= row + r < len(board) and 0 <= col +c < len(board[0])])
                board[row][col] = str(n if n else 'B')
                if not n:
                    for r, c in directions:
                        self.updateBoard(board, [row + r, col + c])
        return board
```

二刷的C++做法。

```cpp
class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        int x = click[0], y = click[1];
        const int M = board.size(), N = board[0].size();
        if (board[x][y] == 'M') {
            board[x][y] = 'X';
        } else if (board[x][y] == 'E') {
            int mcount = 0;
            for (auto p : dirs) {
                int nx = x + p.first, ny = y + p.second;
                if (nx >= 0 && nx < M && ny >= 0 && ny < N && board[nx][ny] == 'M') {
                    mcount ++;
                }
            }
            if (mcount > 0) {
                board[x][y] = '0' + mcount;
            } else {
                board[x][y] = 'B';
                for (auto p : dirs) {
                    int nx = x + p.first, ny = y + p.second;
                    if (nx >= 0 && nx < M && ny >= 0 && ny < N && board[nx][ny] == 'E') {
                        vector<int> pos = {nx, ny};
                        updateBoard(board, pos);
                    }
                }
            }
        }
        return board;
    }
private:
    vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 1}, {1, 0}, {1, -1}, {-1, 1}, {-1, 0}, {-1, -1}};
};
```

参考资料：

https://leetcode-cn.com/problems/minesweeper


## 日期

2018 年 3 月 6 日 
2018 年 12 月 15 日 —— 今天四六级


  [1]: https://leetcode.com/static/images/problemset/minesweeper_example_1.png
  [2]: https://leetcode.com/static/images/problemset/minesweeper_example_2.png
