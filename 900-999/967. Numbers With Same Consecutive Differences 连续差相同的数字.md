

作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/numbers-with-same-consecutive-differences/


## 题目描述

Return all **non-negative** integers of length ``N`` such that the absolute difference between every two consecutive digits is ``K``.

Note that **every** number in the answer **must not** have leading zeros **except** for the number ``0`` itself. For example, 01 has one leading zero and is invalid, but ``0`` is valid.

You may return the answer in any order.
 

Example 1:

    Input: N = 3, K = 7
    Output: [181,292,707,818,929]
    Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:

    Input: N = 2, K = 1
    Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Note:

1. 1 <= N <= 9
1. 0 <= K <= 9

## 题目大意

找出N位数中，所有满足每个数字的所有连续数相减绝对值等于K的数字。比如第一个例子的181就满足|8-1| = |1 - 8| = 7.

## 解题方法

### DFS

明显这是个找出所有符合条件的题目，因此是个搜索题。看了给出的数字的范围只有9位数，大概判断使用DFS不会超时。因此，我们使用DFS找出所有符合条件的即可。

这里的DFS搜索方法是，我们先确定首位数字是1到9，然后计算以这个数字开头的整数满足条件的有多少。也就是``末位数字 + K <= 9`` 或者``末位数字 + K >= 0``两种符合条件，可以继续向后搜索，知道搜索到N==0，那么搜索结束，把现在的整数放到结果里即可。

题目里面有两个坑：第一，先导0的问题，我在上面搜索的过程中是假设了第一位数字不是0了，那么对于N>=2的时候是满足的，当N==1的时候直接返回0~9各个数字即可，这点题目没有说清楚，我觉得是不好的。第二，题目没有专门提到返回的数字不能有重复，我觉得题目应该提醒一下。

python代码如下：

```python
class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [0, 1,2,3,4,5,6,7,8,9]
        res = []
        for i in range(1, 10):
            self.dfs(res, i, N - 1, K)
        return list(set(res))
        
    def dfs(self, res, curint, N, K):
        if N == 0:
            res.append(curint)
            return
        last = curint % 10
        if last + K <= 9:
            self.dfs(res, curint * 10 + last + K, N - 1, K)
        if last - K >= 0:
            self.dfs(res, curint * 10 + last - K, N - 1, K)
```


用C++再写了一遍的时候，对去重的处理时当K不等于0的时候再向更小的数字搜索，因为K等于0的搜索已经在last + K <=9中完成了。C++代码如下：

```cpp
class Solution {
public:
    vector<int> numsSameConsecDiff(int N, int K) {
        if (N == 1)
            return {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        vector<int> res;
        for (int i = 1; i <= 9; i++)
            helper(res, i, N - 1, K);
        return res;
    }
    void helper(vector<int>& res, int curint, int N, int K) {
        if (N == 0) {
            res.push_back(curint);
            return;
        }
        int last = curint % 10;
        if (last + K <= 9)
            helper(res, curint * 10 + last + K, N - 1, K);
        if (last - K >= 0 && K)
            helper(res, curint * 10 + last - K, N - 1, K);
    }
};
```


## 日期

2018 年 12 月 30 日 —— 周赛差强人意


  [1]: https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png
  [2]: https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png
  [3]: https://blog.csdn.net/fuxuemingzhu/article/details/82620422
