
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/n-queens/


## 题目描述

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

![此处输入图片的描述][1]

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where ``'Q'`` and ``'.'`` both indicate a queen and an empty space respectively.

Example:

    Input: 4
    Output: [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],
    
     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
    Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

## 题目大意

求n皇后问题的每个解。注意题意，n皇后问题是在n*n的棋盘上放n个皇后，每一种放置方案。

## 解题方法

### 回溯法

这个题是[52. N-Queens II][2]题目的拓展，52题只要求了统计个数，这个题要求把每一种结果写出来。其实代码基本一样了，只是最后在搜索到对应的解的时候，52题只把结果+1即可，现在的这个题需要构造出对应的放置方案，然后放入到res中。

所以定义了两个函数：helper函数是我们即将要处理row行了，进行回溯；isValid是我们如果这一步放在第row,col位置，合不合法？

python代码如下：

```python
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<int> board(n, -1);
        vector<vector<string>> res;
        helper(board, res, 0);
        return res;
    }
    // how to put in row? (havent put down yet)
    void helper(vector<int>& board, vector<vector<string>>& res, int row) {
        const int N = board.size();
        if (row == N) {
            vector<string> path(N, string(N, '.'));
            for (int i = 0; i < N; i++) {
                path[i][board[i]] = 'Q';
            }
            res.push_back(path);
        } else {
            for (int col = 0; col < N; col++) {
                board[row] = col;
                if (isValid(board, row, col)) {
                    helper(board, res, row + 1);
                }
                board[row] = -1;
            }
        }
    }
    // have put down in (row, col), alright?
    bool isValid(vector<int>& board, int row, int col) {
        for (int prow = 0; prow < row; prow ++) {
            int pcol = board[prow];
            if (pcol == col || abs(prow - row) == abs(pcol - col)) {
                return false;
            }
        }
        return true;
    }
};
```


## 日期

2018 年 12 月 23 日 —— 周赛成绩新高


  [1]: https://assets.leetcode.com/uploads/2018/10/12/8-queens.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/79517109
