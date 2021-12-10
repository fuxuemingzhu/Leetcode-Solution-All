
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/word-search-ii/


## 题目描述

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

    Input: 
    
    words = ["oath","pea","eat","rain"] and board =
    [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    
    Output: ["eat","oath"]

Note:

１．You may assume that all inputs are consist of lowercase letters a-z.

## 题目大意

给定一组坐标，找出四个顶点使其能构成长方形，求最小的长方形的面积。注意，边有可能不和x,y轴平行。

## 解题方法

### 前缀树

这个题仍然是前缀树的题目，但是我抠了很久。。果然Hard题就是不好写啊。

首先，这个题给出的words特别多，但是board的大小反而稍微小了一点，但是题目没有提示，这就造成了在board中搜索每个单词的方法会超时。正确的做法应该是，直接对board进行搜索，判断搜索过程中能不能构成words中的某个字符串。

如果我们保存路径，再去word中查，这个效率就很低了，这里对前缀树进行了改变，对于单词节点不去保存isWord，而是保存现在位置的字符串是什么，那么在board搜索过程中，如果恰好找到了一个前缀树中的单词，那就放到结果里。

这个题我一直在错，却想不明白的地方是在找到一个单词之后对p->str进行了清空的同时，return了！这是错误的！因为对于相同前缀的字符串，我们还要继续向后搜索的。比如``"anes","anesis"``如果在第一个单词搜索到之后return，就不可能搜索到第二个单词。所以不能return.

另外，返回的结果排不排序不影响，对时间影响不大。

当代码比较长的时候，一定要保证写出的每个模块是对的，只有这样才能减少检查的时间。特别是细节错误，千万不能犯。

C++代码如下：

```python
class TrieNode {
public:
    vector<TrieNode*> child;
    string str;
    TrieNode() : child(26, nullptr), str("") {};
    ~TrieNode() {
        for (auto c : child) delete c;
    }
};
class Trie {
public:
    TrieNode* root;
    Trie() : root(new TrieNode()){};
    void insert(string word) {
        TrieNode* p = root;
        for (char c : word) {
            int i = c - 'a';
            if (!p->child[i])
                p->child[i] = new TrieNode();
            p = p->child[i];
        }
        p->str = word;
    }
};
class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        const int M = board.size(), N = board[0].size();
        vector<vector<bool>> visited(M, vector<bool>(N, false));
        Trie trie;
        for (string word : words)
            trie.insert(word);
        vector<string> res;
        for (int r = 0; r < M; r ++) {
            for (int c = 0; c < N; c++) {
                if (trie.root->child[board[r][c] - 'a']) {
                    helper(board, trie.root->child[board[r][c] - 'a'], r, c, visited, res);
                }
            }
        }
        sort(res.begin(), res.end());
        return res;
    }
    void helper(vector<vector<char>>& board, TrieNode* p, int r, int c, vector<vector<bool>>& visited, vector<string>& res) {
        const int M = board.size(), N = board[0].size();
        if (!p->str.empty()){
            res.push_back(p->str);
            p->str.clear();
        }
        visited[r][c] = true;
        for (auto d : dirs) {
            int nx = r + d.first;
            int ny = c + d.second;
            if (nx < 0 || nx >= M || ny < 0 || ny >= N || visited[nx][ny] || !p->child[board[nx][ny] - 'a'])
                continue;
            helper(board, p->child[board[nx][ny] - 'a'], nx, ny, visited, res);
        }
        visited[r][c] = false;
    }

private:
    vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
};
```


## 日期

2018 年 12 月 23 日 —— 周赛成绩新高


  [1]: https://assets.leetcode.com/uploads/2018/12/21/1a.png
  [2]: https://assets.leetcode.com/uploads/2018/12/22/2.png
  [3]: https://assets.leetcode.com/uploads/2018/12/22/3.png
  [4]: https://assets.leetcode.com/uploads/2018/12/21/4c.png
  [5]: https://blog.csdn.net/fuxuemingzhu/article/details/79368360
  [6]: https://blog.csdn.net/fuxuemingzhu/article/details/79368360
  [7]: https://blog.csdn.net/fuxuemingzhu/article/details/79368360
