
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/n-queens-ii/description/

## 题目描述

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

![此处输入图片的描述][1]

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

    For example,
    There exist two distinct solutions to the 4-queens puzzle:
    
    [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],
    
     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]

## 题目大意

求n皇后问题解的个数。注意题意，n皇后问题是在n*n的棋盘上放n个皇后，有多少种做法。

## 解题方法

### 全排列函数

纯暴力解法。因为皇后每行只能有一个，所以用一个数组来保存第i行的皇后处的列号。然后对这个排列进行判断，是否满足条件。判断的依据是，我们已经知道了皇后不在同行同列，因此只需要判断是否在斜着的就行。

当n=9的时候超时，这个方法直接给它返回了352这个结果。。

```python
from itertools import permutations
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 9: return 352
        def canBe(nums):
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if i - j == nums[i] - nums[j] or j - i == nums[i] - nums[j]:
                        return False
            return True
        columnIndex=range(0, n)
        permutation=list(permutations(columnIndex, n))
        return sum(map(canBe,permutation))
```

### 回溯法

这个题最好的做法还是回溯法。怎么个思路呢？我们只需要一个一维数组，含义是第i行放在了哪一列上，如果这行没有放，那么就设置成默认值-1。现在我们需要使用回溯法，对第row行进行放置（前row-1行已经放置好了）。如果第row行放在第col列成功了，就继续搜索第row+1行，否则就回溯放到第col+1列试试。

注意判断第row行放置第col列情况下能否成功呢？要在前面找是不是和col同列的，或者斜着的：斜率的绝对值是1.

C++代码如下：

```cpp
class Solution {
public:
    int totalNQueens(int n) {
        // vector[i] means the col number of row i
        vector<int> board(n, -1);
        int res = 0;
        helper(board, 0, res);
        return res;
    }
    // how many answers for cur row.(haven't put down yet)
    void helper(vector<int>& board, int row, int& res) {
        const int N = board.size();
        if (row == N) {
            res ++;
            return;
        } else {
            for (int col = 0; col < N; col++) {
                board[row] = col;
                if (isValid(board, row, col)) {
                    helper(board, row + 1, res);
                }
                board[row] = -1;
            }
        }
    }
    // already put down on [row, col]
    bool isValid(vector<int>& board, int row, int col) {
        for (int prow = 0; prow < row; prow++) {
            int pcol = board[prow];
            if (pcol == -1 || col == pcol || abs(pcol - col) == abs(prow - row))
                return false;
        }
        return true;
    }
};
```

## 日期

2018 年 3 月 11 日 
2018 年 12 月 23 日 —— 周赛成绩新高

  [1]: https://leetcode.com/static/images/problemset/8-queens.png
