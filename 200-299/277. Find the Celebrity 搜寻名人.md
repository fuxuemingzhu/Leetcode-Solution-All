
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode-cn.com/problems/find-the-celebrity/

## 题目描述

Suppose you are at a party with `n` people (labeled from `0` to `n - 1`) and among them, there may exist one celebrity. The definition of a celebrity is that all the other `n - 1` people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

Example 1:


    Input: graph = [
      [1,1,0],
      [0,1,0],
      [1,1,1]
    ]
    Output: 1
    Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
Example 2:


    Input: graph = [
      [1,0,1],
      [1,1,0],
      [0,1,1]
    ]
    Output: -1
    Explanation: There is no celebrity.

Note:

1. The directed graph is represented as an adjacency matrix, which is an n x n matrix where a[i][j] = 1 means person i knows person j while a[i][j] = 0 means the contrary.
1. Remember that you won't have direct access to the adjacency matrix.

## 题目大意

假设你是一个专业的狗仔，参加了一个 n 人派对，其中每个人被从 0 到 n - 1 标号。在这个派对人群当中可能存在一位 “名人”。所谓 “名人” 的定义是：其他所有 n - 1 个人都认识他/她，而他/她并不认识其他任何人。

## 解题方法

### 暴力

把i当做是候选的名人，判断他是否认识其他每个人j，并且其他j都认识他。如果i认识j或者j不认识i，那么i就不是名人。

C++代码如下：

```cpp
// Forward declaration of the knows API.
bool knows(int a, int b);

class Solution {
public:
    int findCelebrity(int n) {
        for (int i = 0; i < n; ++i) {
            bool isCelebrity = true;
            for (int j = 0; j < n; ++j) {
                if (j == i) continue;
                if (knows(i, j) || !knows(j, i)) {
                    isCelebrity = false;
                    break;
                }
            }
            if (isCelebrity)
                return i;
        }
        return -1;
    }
};
```

## 日期

2019 年 9 月 22 日 —— 熬夜废掉半条命


  [1]: https://assets.leetcode.com/uploads/2018/10/12/maze_1_example_1.png
  [2]: https://assets.leetcode.com/uploads/2018/10/13/maze_1_example_2.png
  [3]: https://blog.csdn.net/fuxuemingzhu/article/details/101056461
