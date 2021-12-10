

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/


## 题目描述

Return the **length** of the shortest, non-empty, contiguous subarray of ``A`` with sum at least ``K``.

If there is no non-empty subarray with sum at least ``K``, return ``-1``.

 

Example 1:

    Input: A = [1], K = 1
    Output: 1

Example 2:

    Input: A = [1,2], K = 4
    Output: -1

Example 3:

    Input: A = [2,-1,2], K = 3
    Output: 3
 

Note:

1. 1 <= A.length <= 50000
1. -10 ^ 5 <= A[i] <= 10 ^ 5
1. 1 <= K <= 10 ^ 9


## 题目大意

求最短的子数组长度，使得这个子数组的和最少为K，如果不存在这样的子数组，返回-1.

## 解题方法

### 队列

我尝试了O(N^2)的解法，果然超时了。也对，题目给出的数组长度是50000，基本上只有O(N)或者O(NlogN)的时间复杂度才行了。

这个题的做法要感谢lee215和演员的自我修养。下面的内容来自[演员的自我修养](https://buptwc.com/2018/07/02/Leetcode-862-Shortest-Subarray-with-Sum-at-Least-K/)。

分析：

1. 显然，我们会想到使用dp[i]记录sum(A[:i])，那么这道题就变成了，给定一个数组dp,找到一组i,j，使得dp[j]-dp[i]>=K，且j-i尽量小！
1. 数据长度达到50000，显然不能使用O(n^2)复杂度的方法，我们得想办法让i,j只走一遍
1. 用一个简单的示例来分析，设 A = [4,-1,2,3],，K = 5，那么dp = [0,4,3,5,8]，我们从dp数组的第2个数开始分析，（假设来了个-1，那么因为-1比0小，后面任意一个数val如若满足val-0>K,那么val+1也一定大于K，且-1所在的位置i显然能获得更优解，所以0这个位置就失去了意义），现在考虑示例，来了个4，我们发现4-0小于5，我们怎么对4进行处理呢，因为考虑到之后或许会出现一个足够大的数，比如9，那么4相对于0是更优的，但也有可能只来一个8，那么4就没作用了，所以先暂且保留观察。等到来了一个5以上的数，我们依次对保留的数（目前是0，4）进行判断得最优解。
1. 接下来来了个3，那么根据上面提到的论点，4将会被舍弃，但3比0要大，故此时0，3保留。
1. 然后来了个5，5-0>=5，故找到一组i,j，记录下来，然后判断 5-3>=5 ?如若确实大于，即再次找到一组i,j，若小于，则5保留（考虑到之后或许来了个10），依次类推

思路：

1. 建立一个队列记录保留数字，初始为0
1. 依次对dp中的数进行分析，如果dp[i] - dp[Q[0]] >= K，则记录一次i,j
1. 如果dp[i] < dp[Q[-1]]，则舍弃Q[-1]

C++代码如下：

```cpp
class Solution {
public:
    int shortestSubarray(vector<int>& A, int K) {
        const int N = A.size();
        vector<int> preSum(N + 1, 0);
        for (int i = 1; i < N + 1; i++) {
            preSum[i] = preSum[i - 1] + A[i - 1];
        }
        int res = INT_MAX;
        deque<int> q;
        q.push_back(0);
        for (int i = 1; i < N + 1; i++) {
            int a = preSum[i];
            while (!q.empty() && a - preSum[q.front()] >= K) {
                res = min(res, i - q.front());
                q.pop_front();
            }
            while (!q.empty() && a < preSum[q.back()]) {
                q.pop_back();
            }
            q.push_back(i);
        }
        return res == INT_MAX ? -1 : res;
    }
};
```

参考资料：

https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C%2B%2BJavaPython-O(N)-Using-Deque
https://buptwc.com/2018/07/02/Leetcode-862-Shortest-Subarray-with-Sum-at-Least-K/

## 日期

2018 年 12 月 20 日 —— 感冒害的我睡不着


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79368360
