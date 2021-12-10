
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/sum-of-even-numbers-after-queries/


## 题目描述

We have an array ``A`` of integers, and an array queries of queries.

For the ``i``-th query ``val = queries[i][0]``, ``index = queries[i][1]``, we add val to ``A[index]``.  Then, the answer to the ``i-th`` query is the sum of the even values of ``A``.

(Here, the given ``index = queries[i][1]`` is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have ``answer[i]`` as the answer to the i-th query.

 

Example 1:

    Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
    Output: [8,6,2,4]
    Explanation: 
    At the beginning, the array is [1,2,3,4].
    After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
    After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
    After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
    After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
     

Note:

1. 1 <= A.length <= 10000
1. -10000 <= A[i] <= 10000
1. 1 <= queries.length <= 10000
1. -10000 <= queries[i][0] <= 10000
1. 0 <= queries[i][1] < A.length

## 题目大意

给出了原始的数组，然后给出了一串查询步骤，每次查询的时候，都会在指定位置queries[i][1]加上queries[i][0]，在每次操作完毕之后，把所有数值是偶数的数字求和保存起来。求经过一系列的查询之后，生成的偶数之和序列是多少。

## 解题方法

### 暴力

首先，我们可以按照题目描述使用暴力解法。即每次查询之后都去遍历一次，计算偶数之和，保存起来。

设A的长度是M，queries的次数是M，那么时间复杂度是O(N*M)，竟然也通过了。C++用时3000ms，代码如下。

```cpp
class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& A, vector<vector<int>>& queries) {
        vector<int> res;
        for (auto q : queries) {
            A[q[1]] += q[0];
            int sum = 0;
            for (int a : A) {
                if (a % 2 == 0) {
                    sum += a;
                }
            }
            res.push_back(sum);
        }
        return res;
    }
};
```

### 找规律

上面的暴力解法显然不够优美。根据[@votrubac的解法][1]，我们可以先求出所有偶数之和，然后对于每次查询的时候，如果A[index]是偶数，那么就把这个值减去，然后把查询要添加的数值val加到A[index]上。如果加完的结果是偶数的话，需要把该结果加到sum上。

怎么证明？

首先，我们求出了所有偶数的和。

然后每次查询更改一个数字，有四种更改方式：

- 偶 ==> 奇
- 偶 ==> 偶
- 奇 ==> 奇
- 奇 ==> 偶

所以，如果我们要求在查询之后的偶数和，可以在初始化的偶数和的基础上，先减去在查询之前是偶数的（因为这些偶数已经计算到和里面了，即将变化走了），然后查询是当前的数字进行了变化，然后再加上变化之后是偶数的（因为这些偶数是新变化出来的，需要加到偶数和里面）。这样就求得了新的所有偶数的和。

C++代码如下：

```cpp
class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& A, vector<vector<int>>& queries) {
        vector<int> sums;
        int cursum = 0;
        for (int a : A) {
            if (a % 2 == 0) {
                cursum += a;
            }
        }
        for (auto q : queries) {
            if (A[q[1]] % 2 == 0) {
                cursum -= A[q[1]];
            }
            A[q[1]] += q[0];
            if (A[q[1]] % 2 == 0) {
                cursum += A[q[1]];
            }
            sums.push_back(cursum);
        }
        return sums;
    }
};
```

## 日期

2019 年 2 月 19 日 —— 重拾状态


  [1]: https://leetcode.com/problems/sum-of-even-numbers-after-queries/discuss/231098/C++-O%28n%29-track-even-sum
