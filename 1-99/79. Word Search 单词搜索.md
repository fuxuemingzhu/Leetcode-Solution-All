
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/word-search/description/


## 题目描述

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

    For example,
    Given board =
    
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    word = "ABCCED", -> returns true,
    word = "SEE", -> returns true,
    word = "ABCB", -> returns false.


## 题目大意

在一个二维表格里面，看看能不能连续的一笔画出word这个词。

## 解题方法

### 回溯法

还是经典的回溯法问题。这个题的回溯的起点可以是二维数组的任意位置。

回溯法的判定条件比较简单，需要注意的是把已经走过的路给改变了，不能再走了。python中通过swapcase()交换该字母的大小写即可行。

```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for y in xrange(len(board)):
            for x in xrange(len(board[0])):
                if self.exit(board, word, x, y, 0):
                    return True
        return False
    
    def exit(self, board, word, x, y, i):
        if i == len(word):
            return True
        if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
            return False
        if board[y][x] != word[i]:
            return False
        board[y][x] = board[y][x].swapcase()
        isexit =  self.exit(board, word, x + 1, y, i + 1) or self.exit(board, word, x, y + 1, i + 1) or self.exit(board, word, x - 1, y, i + 1) or self.exit(board, word, x, y - 1, i + 1)
        board[y][x] = board[y][x].swapcase()
        return isexit
```

使用C++的话，新开辟了一个visited数组，代表是否已经访问过了。总体代码不难。我使用了pair来保存位置，所以代码略显长了一些。

```cpp
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if (word.size() == 0) return false;
        const int M = board.size(), N = board[0].size();
        vector<vector<bool>> visited(M, vector<bool>(N, false));
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j ++) {
                if (dfs(board, word, 0, {i, j}, visited)) {
                    return true;
                }
            }
        }
        return false;
    }
    bool dfs(const vector<vector<char>>& board, const string& word, int start, pair<int, int> curpos, vector<vector<bool>>& visited) {
        const int M = board.size(), N = board[0].size();
        if (start == word.size()) return true;
        if (curpos.first < 0 || curpos.first >= M || curpos.second < 0 || curpos.second >= N || visited[curpos.first][curpos.second] || word[start] != board[curpos.first][curpos.second]) 
            return false;
        visited[curpos.first][curpos.second] = true;
        for (auto d : dirs) {
            int nx = curpos.first + d.first;
            int ny = curpos.second + d.second;
            if (dfs(board, word, start + 1, {nx, ny}, visited)) 
                return true;
        }
        visited[curpos.first][curpos.second] = false;
        return false;
    }
private:
    vector<pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
};
```

## 日期

2018 年 2 月 27 日 
2018 年 12 月 22 日 —— 今天冬至
