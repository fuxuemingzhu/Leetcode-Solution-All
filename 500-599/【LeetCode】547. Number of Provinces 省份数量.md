
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：[https://leetcode.com/problems/friend-circles/#/description][1]


## 题目描述

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

    Input: 
    [[1,1,0],
     [1,1,0],
     [0,0,1]]
    Output: 2
    Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
    The 2nd student himself is in a friend circle. So return 2.

Example 2:

    Input: 
    [[1,1,0],
     [1,1,1],
     [0,1,1]]
    Output: 1
    Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
    so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

## 题目大意

有一些学生，他们的朋友关系是以邻接矩阵的形式给出的，并且朋友关系可以传递。求总共有多少个朋友圈子。

## 解题方法

经典的并查集问题，并查集就是考察一个组中的互相联通问题。在这个题中，就是看有几个好友环。

首先，定义一个200大小的数组，记录节点对应的根节点编号。findRoot(int x)函数是找出x节点的根节点，在查找某个特定节点的根节点时，同时将其与根节点之间的所有节点都指向根节点，这个工程叫做路径压缩。

在遍历矩阵之前，首先把数组所有的值都初始化为-1，这样如果之后某个节点的根节点编号为-1，说明它是根节点；如果某节点对应的根节点编号不是-1，那么说明这个节点不是根节点，并且已经被捆绑到另外的节点上。

遍历矩阵时，如果矩阵(i,j)位置的值为1，说明它们直接相连，分别用findRoot()找出i,j对应的根节点，如果根节点不相同，则把他们绑在一起。

最终统计下-1的个数，就是有多少个根节点，即有多少个环。

Java解法如下：

```java
public class Solution {
    int tree[] = new int[200];
    public int findCircleNum(int[][] M) {
        int len = M[0].length;
        for(int i = 0; i < len; i++){
            tree[i] = -1;
        }
        for(int i = 0; i < len; i++){
            for(int j = 0; j < len; j++){
                if(M[i][j] == 1){
                    int aRoot = findRoot(i);
                    int bRoot = findRoot(j);
                    if(aRoot != bRoot){
                        tree[aRoot] = bRoot;
                    }
                }
            }
        }
        int ans = 0;
        for(int i = 0; i < len; i++){
            if(tree[i] == -1){
                ans++;
            }
        }
        return ans;
    }
    
    public int findRoot(int x){
        if(tree[x] == -1){
            return x;
        }else{
            int temp = findRoot(tree[x]);
            tree[x] = temp;
            return temp;
        }
    }
}
```

Python版本的解法使用了带权并查集，每次把权重小的加到权重大的上面，这样可以使树的高度尽可能低。权重表示树的节点个数。

代码如下：

```python
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        dsu = DSU()
        N = len(M)
        for i in range(N):
            for j in range(i, N):
                if M[i][j]:
                    dsu.u(i, j)
        res = 0
        for i in range(N):
            if dsu.f(i) == i:
                res += 1
        return res
        
class DSU(object):
    def __init__(self):
        self.d = range(201)
        self.r = [0] * 201
        
    def f(self, a):
        return a if a == self.d[a] else self.f(self.d[a])
    
    def u(self, a, b):
        pa = self.f(a)
        pb = self.f(b)
        if (pa == pb):
            return
        if self.r[pa] < self.r[pb]:
            self.d[pa] = pb
            self.r[pb] += self.r[pa]
        else:
            self.d[pb] = pa
            self.r[pa] += self.r[pb]
```


在union方法中注意，需要把父亲节点进行union，而不是直接把a, b进行合并。

C++版本如下：

```cpp

class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        const int N = M.size();
        for (int i = 0; i < N; i ++)
            map_.push_back(i);
        for (int i = 0; i < N; i ++) {
            for (int j = i + 1; j < N; j ++) {
                if (M[i][j])
                    u(i, j);
            }
        }
        int res = 0;
        for (int i = 0; i < N; i++) {
            if (map_[i] == i)
                res ++;
        }
        return res;
    }
private:
    vector<int> map_; //i的parent，默认是i
    int f(int a) {
        if (map_[a] == a)
            return a;
        return f(map_[a]);
    }
    void u(int a, int b) {
        int pa = f(a);
        int pb = f(b);
        if (pa == pb)
            return;
        map_[pa] = pb;
    }
};
```

## 日期

2017 年 4 月 20 日 
2018 年 12 月 14 日 —— 12月过半，2019就要开始

  [1]: https://leetcode.com/problems/friend-circles/#/description
