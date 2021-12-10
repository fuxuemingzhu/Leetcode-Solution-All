作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/rotting-oranges/


## 题目描述

In a town, there are ``N`` people labelled from ``1`` to ``N``.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
1. Everybody (except for the town judge) trusts the town judge.
1. There is exactly one person that satisfies properties 1 and 2.

You are given ``trust``, an array of pairs ``trust[i] = [a, b]`` representing that the person labelled ``a`` trusts the person labelled ``b``.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

    Input: N = 2, trust = [[1,2]]
    Output: 2

Example 2:

    Input: N = 3, trust = [[1,3],[2,3]]
    Output: 3

Example 3:

    Input: N = 3, trust = [[1,3],[2,3],[3,1]]
    Output: -1

Example 4:

    Input: N = 3, trust = [[1,2],[2,3]]
    Output: -1

Example 5:

    Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    Output: 3
 

Note:

1. 1 <= N <= 1000
1. trust.length <= 10000
1. trust[i] are all different
1. trust[i][0] != trust[i][1]
1. 1 <= trust[i][0], trust[i][1] <= N

## 题目大意

镇里有编号1～N的N个人，如果有个法官存在的话，需要满足三个条件：

1. 法官谁也不信任
1. 每个人都信任这个人
2. 只有一个人满足条件1和2

给出的trust[i] = [a, b]代表了a信任b。

如果法官存在，返回他的序号，否则返回-1.

## 解题方法

### 度

其实这个就是有向图，[a, b]表示从顶点a出发指向顶点b的一条有向边。

所以，题目的意思就是：是否存在且只存在一个顶点，所有的顶点都指向他，但是这个点不指向任何点。用术语来说就是该顶点的入度是N - 1，出度是0.

我们可以使用一个数组存储每个点的``入度和出度的差``，当某个点的``入度和出度的差``是N - 1时，代表他是法官，否则不存在。

证明：如果``入度和出度的差`` = N - 1，又入度、出度 >= 0，那么入度 = N- 1，出度 = 0，满足条件1和2.一旦存在一个点满足条件，那么说明这个点没有出度，所以不存在另一个点的入度是N - 1，满足条件3.

C++代码如下：

```cpp
class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        vector<int> g(N + 1, 0); // in-degree - out-degree
        for (auto t : trust) {
            ++g[t[1]];
            --g[t[0]];
        }
        for (int i = 1; i <= N; ++i) {
            if (g[i] == N - 1)
                return i;
        }
        return -1;
    }
};
```

## 日期

2019 年 2 月 24 日 —— 周末又结束了


  [1]: https://assets.leetcode.com/uploads/2019/02/16/oranges.png
  [2]: https://blog.csdn.net/fuxuemingzhu/article/details/87829987
