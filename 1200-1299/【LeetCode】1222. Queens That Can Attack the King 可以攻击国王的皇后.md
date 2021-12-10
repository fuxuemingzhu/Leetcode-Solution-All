- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/queens-that-can-attack-the-king/

## 题目描述

On an **8x8** chessboard, there can be multiple Black Queens and one White King.

Given an array of integer coordinates queens that represents the positions of the Black Queens, and a pair of coordinates king that represent the position of the White King, return the coordinates of all the queens (in any order) that can attack the King.

Example 1:

![此处输入图片的描述][1]


    Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
    Output: [[0,1],[1,0],[3,3]]
    Explanation:  
    The queen at [0,1] can attack the king cause they're in the same row. 
    The queen at [1,0] can attack the king cause they're in the same column. 
    The queen at [3,3] can attack the king cause they're in the same diagnal. 
    The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1]. 
    The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0]. 
    The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.

Example 2:

![此处输入图片的描述][2]

    Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
    Output: [[2,2],[3,4],[4,4]]

Example 3:

![此处输入图片的描述][3]

    Input: queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
    Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
 

Constraints:

1. `1 <= queens.length <= 63`
1. `queens[0].length == 2`
1. `0 <= queens[i][j] < 8`
1. `king.length == 2`
1. `0 <= king[0], king[1] < 8`
1. At most one piece is allowed in a cell.

## 题目大意

棋盘上有一个国王K，和若干个皇后Q，求哪些皇后能威胁到国王。

## 解题方法

### 遍历

注意皇后会挡住其他的皇后，所以只有和国王处在同一条线上的第一个皇后才是威胁。因此我们从国王位置开始向8个方向辐射状遍历，找到在8个方向上能遇到的第一个皇后即可。

使用了set判断当前遍历到的位置上是否有皇后，如果找到皇后，则放入结果中，并且不再遍历。

C++代码如下：

```cpp
class Solution {
public:
    vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
        set<vector<int>> s(queens.begin(), queens.end());
        vector<vector<int>> res;
        for (auto& dir : dirs) {
            vector<int> pos = king;
            while (true) {
                pos[0] += dir[0];
                pos[1] += dir[1];
                if (pos[0] < 0 || pos[0] >= 8 || pos[1] < 0 || pos[1] >= 8)
                    break;
                if (s.count(pos)) {
                    res.push_back(pos);
                    break;
                }
            }
        }
        return res;
    }
private:
    vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
};
```


## 日期

2019 年 10 月 13 日 —— 国庆调休，这周末只有这一天假


  [1]: https://assets.leetcode.com/uploads/2019/10/01/untitled-diagram.jpg
  [2]: https://assets.leetcode.com/uploads/2019/10/01/untitled-diagram-1.jpg
  [3]: https://assets.leetcode.com/uploads/2019/10/01/untitled-diagram-2.jpg
