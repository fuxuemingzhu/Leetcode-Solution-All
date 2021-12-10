作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/


## 题目描述

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

 

Example 1:

    Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    Output: 5

Example 2:

    Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    Output: 3

Example 3:

    Input: stones = [[0,0]]
    Output: 0
 

Note:

1. 1 <= stones.length <= 1000
1. 0 <= stones[i][j] < 10000
 

## 题目大意

在二维坐标的整数坐标点上，有一些石头，如果一个石头和另外一个石头的横坐标或者纵坐标相等，那么认为他们是有链接的。我们每次取一个和别人有链接的石头，问最终能取得多少个石头。

## 解题方法

### 并查集

这个题翻译一下就是，横或者纵坐标相等的坐标点会互相链接构成一个区域，问总的有多少个独立的区域。结果是总的石头数减去独立区域数。

所以，我们根本不用考虑太多，只需要统计有多少区域即可。这个方法最简单的就是并查集。

思路是，两重循环，分别判断石头两两之间是否有链接，如果有链接，那么把他们组成同一个区域。这样的优点是我们只需要和石头等长的数组放每个的parent即可。最后统计最后的区域中-1的数量就是独立区域的个数。石头个数减去独立区域数即可。

python代码如下，可惜超时了。

```python
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        N = len(stones)
        self.map = [-1] * N
        for i in range(N):
            for j in range(i + 1, N):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.union(i, j)
        res = N
        print(self.map)
        for i in range(N):
            if self.map[i] == -1:
                res -= 1
        return res
        
    def find(self, x):
        return x if self.map[x] == -1 else self.find(self.map[x])
        
    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.map[fx] = fy
```

这个版本的C++可以做通过，说明了C++速度的优越性。

```cpp
class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        if(stones.size() <= 1) return 0;
        int N = stones.size();
        vector<int> p(N, -1);
        for (int i = 0; i < N; ++i){
            for(int j = i + 1; j < N; ++j){
                if (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]){
                    u(p, i, j);
                }
            }
        }
        int res = N;
        for(auto e: p) if(e == -1) --res;
        return res;
    }
private:
    int f(vector<int> &p, int x){
        if(p[x] == -1) return x;
        return f(p, p[x]);
    }
    
    void u(vector<int> &p, int x, int y){
        int px = f(p, x);
        int py = f(p, y);
        if(px != py){
            p[px] = py;
        }
    }
};
```

其实上面这个版本可以做优化，我们不用对石头进行两两判断，而是对他们的横纵坐标同等看待。怎么区分横纵坐标呢？使用的方法是把纵坐标+10000，这样行的索引没变，纵坐标的范围跑到了后面去了。

这个做法的思路是，一个坐标其实就是把横纵坐标对应的两个区域进行了链接。所以，只需要对stones进行一次遍历把对应的区域链接到一起即可。在完成链接之后，我们最后统计一下有多少个独立的区域，需要使用set+find。

Python代码如下：

```python
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        N = len(stones)
        self.map = [-1] * 20000
        for x, y in stones:
            self.union(x, y + 10000)
        count = set()
        return N - len({self.find(x) for x, y in stones})
        
    def find(self, x):
        return x if self.map[x] == -1 else self.find(self.map[x])
        
    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.map[fx] = fy
```

C++代码如下：

```cpp
class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        if(stones.size() <= 1) return 0;
        int N = stones.size();
        vector<int> p(20000, -1);
        for(auto stone : stones){
            u(p, stone[0], stone[1] + 10000);
        }
        set<int> parents;
        for(auto stone : stones){
            parents.insert(f(p, stone[0]));
        }
        return N - parents.size();
    }
private:
    int f(vector<int> &p, int x){
        if(p[x] == -1) return x;
        return f(p, p[x]);
    }
    
    void u(vector<int> &p, int x, int y){
        int px = f(p, x);
        int py = f(p, y);
        if(px != py){
            p[px] = py;
        }
    }
};
```


## 日期

2018 年 11 月 24 日 —— 周日开始！一周就过去了～


  [1]: http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-730-count-different-palindromic-subsequences/
