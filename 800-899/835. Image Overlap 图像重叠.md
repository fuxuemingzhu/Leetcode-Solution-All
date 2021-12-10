
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/image-overlap/description/

## 题目描述

Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

    Input: A = [[1,1,0],
                [0,1,0],
                [0,1,0]]
           B = [[0,0,0],
                [0,1,1],
                [0,0,1]]
    Output: 3
    Explanation: We slide A to right by 1 unit and down by 1 unit.

Notes: 

- 1 <= A.length = A[0].length = B.length = B[0].length <= 30
- 0 <= A[i][j], B[i][j] <= 1

## 题目大意

两个形状相同的正方形矩阵，求用什么体位把它两个重叠在一起，然后重叠部分中1的个数最多。

## 解题方法

思路挺好玩的，直接找出所有1的位置，然后对两个矩阵的所有这些位置进行求差。然后统计这些差出现最多的次数是多少。

两个坐标的差是什么含义？就是把其中一个坐标移动到另一个坐标需要移动的向量。因此，在遍历过程中，我们找出了A中所有值为1的坐标移动到B中所有值为1的坐标需要移动的向量。那么，在这些向量中出现次数最多的向量就是我们要求的整个矩阵应该移动的向量。这个向量出现的次数，就是我们向该向量方向移动了之后，能重叠的1的个数。

结尾的or [0]挺有意思，防止了d.values()是空。


Python代码如下：

```python
class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        N = len(A)
        LA = [(xi, yi) for xi in range(N) for yi in range(N) if A[xi][yi]]
        LB = [(xi, yi) for xi in range(N) for yi in range(N) if B[xi][yi]]
        d = collections.Counter([(x1 - x2, y1 - y2) for (x1, y1) in LA for (x2, y2) in LB])
        return max(d.values() or [0])
```

二刷的时候使用C++，首先是上面同样的做法，没有优化的代码如下：

```cpp
class Solution {
public:
    int largestOverlap(vector<vector<int>>& A, vector<vector<int>>& B) {
        map<pair<int, int>, int> move;
        vector<pair<int, int>> A1s, B1s;
        for (int i = 0; i < A.size(); ++i) {
            for (int j = 0; j < A[0].size(); ++j) {
                if (A[i][j])
                    A1s.push_back({i, j});
            }
        }
        for (int i = 0; i < B.size(); ++i) {
            for (int j = 0; j < B[0].size(); ++j) {
                if (B[i][j])
                    B1s.push_back({i, j});
            }
        }
        int res = 0;
        for (auto a : A1s) {
            for (auto b : B1s) {
                pair<int, int> dir = make_pair(b.first - a.first, b.second - a.second);
                move[dir]++;
                res = max(res, move[dir]);
            }
        }
        return res;
    }
};
```

上面这个代码确实啰嗦了，看了[寒神的答案](https://leetcode.com/problems/image-overlap/discuss/130623/C++JavaPython-Straight-Forward)，感觉自愧不如啊！

寒神的做法的优点：第一，注意到了题目给的A和B是大小相等的正方形！第二，遍历正方形的方式使用的是``i``在``[0,N*N)``区间里，然后``[i/N][i%N]``这个求位置方法，可以把两重循环简写成一重（但是时间复杂没有变化）。第三，使用了数字表示向量，即把一个向量的行数*100+列数，比如第13行第19列，可以用一个数字表示1319。寒神告诉我们，这个100的选择是因为太小的话不能有效区分，应该最小是2N。

```cpp
class Solution {
public:
    int largestOverlap(vector<vector<int>>& A, vector<vector<int>>& B) {
        const int N = A.size();
        unordered_map<int, int> move;
        vector<int> A1s, B1s;
        for (int i = 0; i < N * N; ++i) {
            if (A[i / N][i % N])
                A1s.push_back((i / N) * 100 + i % N);
            if (B[i / N][i % N])
                B1s.push_back((i / N) * 100 + i % N);
        }
        int res = 0;
        for (auto a : A1s) {
            for (auto b : B1s) {
                move[b - a]++;
                res = max(res, move[b - a]);
            }
        }
        return res;
    }
};

```


参考资料：

https://blog.csdn.net/zjucor/article/details/80298134
https://leetcode.com/problems/image-overlap/discuss/150504/Python-Easy-Logic
https://leetcode.com/problems/image-overlap/discuss/130623/C%2B%2BJavaPython-Straight-Forward

## 日期

2018 年 9 月 10 日 —— 教师节快乐！
2018 年 12 月 28 日 —— 元旦假期到了
