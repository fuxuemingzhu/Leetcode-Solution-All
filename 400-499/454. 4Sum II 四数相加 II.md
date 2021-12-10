
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/4sum-ii/description/

## 题目描述

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

    Example:
    
    Input:
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    
    Output:
    2
    
    Explanation:
    The two tuples are:
    1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
    2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

## 题目大意

有四个等长的数组，分别找出四个数组中的下标，能让四个数组该位置的和是0，统计这种组合的次数。

## 解题方法
### 字典

蛮力求解肯定不行的。给出了4个数，把A,B一组，C,D一组先进行遍历求和保存到字典中，就能把复杂度从O(n^4)降到O(n^2)

具体的是使用Counter计算，具体的实现不难，复杂度是O(n^2)。

方法是先对A,B能组成的和进行统计，然后对C,D遍历求和并取相反数，看在A,B中出现了多少次。

代码：

```python
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = collections.Counter(a + b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)
```

不能对两个字典进行遍历求解，那样复杂度增大，而是直接使用对一个遍历，对另个进行直接查询的方式，C++代码如下：

```cpp
class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        const int N = A.size();
        unordered_map<int, int> AB;
        unordered_map<int, int> CD;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                ++AB[A[i] + B[j]];
                ++CD[C[i] + D[j]];
            }
        }
        int res = 0;
        for (auto ab : AB) {
            res += ab.second * CD[-ab.first];
        }
        return res;
    }
};
```

## 日期

2018 年 3 月 7 日 
2018 年 11 月 11 日 —— 剁手节快乐
2019 年 1 月 25 日 —— 这学期最后一个工作日
