

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/the-earliest-moment-when-everyone-become-friends/

## 题目描述

In a social group, there are `N` people, with unique integer ids from `0` to `N-1`.

We have a list of logs, where each `logs[i] = [timestamp, id_A, id_B]` contains a non-negative integer timestamp, and the ids of two different people.

Each log represents the time in which two different people became friends.  Friendship is symmetric: if `A` is friends with `B`, then `B` is friends with `A`.

Let's say that person `A` is acquainted with person `B` if `A` is friends with `B`, or `A` is a friend of someone acquainted with `B`.

Return the earliest time for which every person became acquainted with every other person. Return -1 if there is no such earliest time.


Example 1:

    Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], N = 6
    Output: 20190301
    Explanation: 
    The first event occurs at timestamp = 20190101 and after 0 and 1 become friends we have the following friendship groups [0,1], [2], [3], [4], [5].
    The second event occurs at timestamp = 20190104 and after 3 and 4 become friends we have the following friendship groups [0,1], [2], [3,4], [5].
    The third event occurs at timestamp = 20190107 and after 2 and 3 become friends we have the following friendship groups [0,1], [2,3,4], [5].
    The fourth event occurs at timestamp = 20190211 and after 1 and 5 become friends we have the following friendship groups [0,1,5], [2,3,4].
    The fifth event occurs at timestamp = 20190224 and as 2 and 4 are already friend anything happens.
    The sixth event occurs at timestamp = 20190301 and after 0 and 3 become friends we have that all become friends.

Note:

1. `2 <= N <= 100`
1. `1 <= logs.length <= 10^4`
1. `0 <= logs[i][0] <= 10^9`
1. `0 <= logs[i][1], logs[i][2] <= N - 1`
1. It's guaranteed that all timestamps in `logs[i][0]` are different.
1. logs are not necessarily ordered by some criteria.
1. `logs[i][1] != logs[i][2]`



## 题目大意

在一个社交圈子当中，有 N 个人。每个人都有一个从 0 到 N-1 唯一的 id 编号。
我们有一份日志列表 logs，其中每条记录都包含一个非负整数的时间戳，以及分属两个人的不同 id，logs[i] = [timestamp, id_A, id_B]。
每条日志标识出两个人成为好友的时间，友谊是相互的：如果 A 和 B 是好友，那么 B 和 A 也是好友。
如果 A 是 B 的好友，或者 A 是 B 的好友的好友，那么就可以认为 A 也与 B 熟识。
返回圈子里所有人之间都熟识的最早时间。如果找不到最早时间，就返回 -1 。


## 解题方法

### 并查集

提示的不能更明显了，标准的并查集。

1. 对logs按照时间排序。
2. 遍历logs，合并两个人所属的环，如果环减少到1那就是最短的时间。

C++代码如下：

```cpp
class Solution {
public:
    int earliestAcq(vector<vector<int>>& logs, int N) {
        map_ = vector<int>(N);
        circle = N;
        for (int i = 0; i < N; ++i)
            map_[i] = i;
        sort(logs.begin(), logs.end(), [](vector<int>& a, vector<int>& b) {return a[0] < b[0];});
        for (auto& log : logs) {
            uni(log[1], log[2]);
            if (circle == 1)
                return log[0];
        }
        return -1;
    }
    int find(int a) {
        if (map_[a] == a)
            return a;
        return find(map_[a]);
    }
    void uni(int a, int b) {
        int pa = find(a);
        int pb = find(b);
        if (pa == pb)
            return;
        map_[pa] = pb;
        circle --;
    }
private:
    vector<int> map_;
    int circle = 0;
};
```


## 日期

2019 年 9 月 21 日 —— 莫生气，我若气病谁如意


  [1]: https://assets.leetcode.com/uploads/2018/10/12/candy_crush_example_2.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/101068011
