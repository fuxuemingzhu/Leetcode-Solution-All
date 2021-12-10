
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/keys-and-rooms/description/

## 题目描述

There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:
    
    Input: [[1],[2],[3],[]]
    Output: true
    Explanation:  
    We start in room 0, and pick up key 1.
    We then go to room 1, and pick up key 2.
    We then go to room 2, and pick up key 3.
    We then go to room 3.  Since we were able to go to every room, we return true.
    
Example 2:
    
    Input: [[1,3],[3,0,1],[2],[0]]
    Output: false
    Explanation: We can't enter the room with number 2.
Note:

1. 1 <= rooms.length <= 1000
1. 0 <= rooms[i].length <= 1000
1. The number of keys in all rooms combined is at most 3000.

## 题目大意

这个题目有点长，简单的翻译就是，我们有很多房间，每个房间里面有几个钥匙，每个钥匙是个数字对应着能开的房间的索引号。刚开始的时候只有第0个位置的房间是开着的，其他房间是锁着的。开了的门不会再锁上，可以允许后退。看到最后能不能把所有的房间的门都打开。

## 解题方法

### DFS

看到这个题，我们发现最后要求出是否存在一个解。这个解是通过一段深度遍历求得。

所以很快的写出来一段dfs，dfs里把当前的门打开，并看这个房间的钥匙，找到还没去过的房间，把门打开，依次类推。

这样，我们就遍历了所有的能去到的房间，最后看一下是否所有的房间都经历过即可。


```python
class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [0] * len(rooms)
        self.dfs(rooms, 0, visited)
        return sum(visited) == len(rooms)
        
    def dfs(self, rooms, index, visited):
        visited[index] = 1
        for key in rooms[index]:
            if not visited[key]:
                self.dfs(rooms, key, visited)
```

C++代码如下：

```cpp
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int N = rooms.size();
        vector<int> visited(N);
        dfs(visited, rooms, 0);
        int res = 0;
        for (int v : visited) res += v;
        return res == N;
    }
private:
    void dfs(vector<int>& visited, vector<vector<int>>& rooms, int pos) {
        visited[pos] = 1;
        for (int n : rooms[pos])
            if (!visited[n])
                dfs(visited, rooms, n);
    }
};
```

### BFS

使用BFS同样也可以，只要走不下去了，那么就停止。

```cpp
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int N = rooms.size();
        vector<int> visited(N);
        queue<int> q;
        q.push(0);
        while (!q.empty()) {
            int f = q.front(); q.pop();
            if (visited[f]) continue;
            visited[f] = 1;
            for (int n : rooms[f]) {
                q.push(n);
            }
        }
        int res = 0;
        for (int v : visited) res += v;
        return res == N;
    }
};
```

## 日期

2018 年 5 月 28 日 —— 太阳真的像日光灯～
2018 年 12 月 6 日 —— 周四啦！

  [1]: https://blog.csdn.net/firefly_2002/article/details/7886989
