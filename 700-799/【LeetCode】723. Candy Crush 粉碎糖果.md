
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/candy-crush/

## 题目描述

This question is about implementing a basic elimination algorithm for Candy Crush.

Given a `2D` integer array board representing the grid of candy, different positive integers `board[i][j]` represent different types of candies. A value of `board[i][j] = 0` represents that the cell at position `(i, j)` is empty. The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

1. If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
1. After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
1. After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
1. If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
1. You need to perform the above rules until the board becomes stable, then return the current board.

 

Example:

    Input:
    board =
    [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
    
    Output:
    [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]

    Explanation:

 ![此处输入图片的描述][1]

Note:

1. The length of board will be in the range [3, 50].
1. The length of board[i] will be in the range [3, 50].
1. Each board[i][j] will initially start as an integer in the range [1, 2000].



## 题目大意

消消乐玩过没有？这就是开始消除至少有三个相连的糖果，一直到达没有糖果可以消除为止。

## 解题方法

### 暴力

这个题和炸弹人[361. Bomb Enemy][2]有点类似。题目是让从刚开始的Board就开始同时消除该board下所有的至少三个相连的数字。很显然，我们必须保存下目前可以消除的位置，在把当前的board遍历完成之后，在一起一次性全部消除。具体来说分为三步：

1. 找出行和列中所有相连且相等长度大于三的数字位置。（对于每个位置都向四个方向寻找，类似于炸弹人寻找墙壁）
2. 把这些位置的值设置为0。（此时如果这些位置不存在，则返回结果）
3. 被消除的这些位置应该被消除掉，所以把上面的数字都向下移。（对于每列而言，从下向上查找不为0的数字，放到从下面的倒数位置上）

C++代码如下：

```cpp
class Solution {
public:
    vector<vector<int>> candyCrush(vector<vector<int>>& board) {
        const int M = board.size();
        const int N = board[0].size();
        while (true) {
            vector<pair<int, int>> del; 
            for (int i = 0; i < M; ++i) {
                for (int j = 0; j < N; ++j) {
                    if (board[i][j] == 0) continue;
                    int x0 = i, x1 = i, y0 = j, y1 = j;
                    while (x0 >= 0 && x0 > i - 3 && board[x0][j] == board[i][j]) x0--;
                    while (x1 < M && x1 < i + 3 && board[x1][j] == board[i][j]) x1++;
                    while (y0 >= 0 && y0 > j - 3 && board[i][y0] == board[i][j]) y0--;
                    while (y1 < N && y1 < j + 3 && board[i][y1] == board[i][j]) y1++;
                    if (x1 - x0 > 3 || y1 - y0 > 3) {
                        del.push_back({i, j});
                    }
                }
            }
            if (del.empty()) break;
            for (auto& d : del) {
                board[d.first][d.second] = 0;
            }
            for (int j = 0; j < N; ++j) {
                int t = M - 1;
                for (int i = M - 1; i >= 0; --i) {
                    if (board[i][j])
                        swap(board[i][j], board[t--][j]);
                }
            }
        }
        return board;
    }
};
```


## 日期

2019 年 9 月 21 日 —— 莫生气，我若气病谁如意


  [1]: https://assets.leetcode.com/uploads/2018/10/12/candy_crush_example_2.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/101068011
