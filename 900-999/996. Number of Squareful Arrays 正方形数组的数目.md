作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/number-of-squareful-arrays/


## 题目描述

Given an array ``A`` of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

Return the number of permutations of A that are squareful.  Two permutations ``A1`` and ``A2`` differ if and only if there is some index ``i`` such that ``A1[i] != A2[i]``.

Example 1:

    Input: [1,17,8]
    Output: 2
    Explanation: 
    [1,8,17] and [17,8,1] are the valid permutations.

Example 2:

    Input: [2,2,2]
    Output: 1
 

Note:

1. 1 <= A.length <= 12
1. 0 <= A[i] <= 1e9

## 题目大意

给出了一个非负数字组成的数组，如果一个数组是可平方的，那么这个数组每两个相邻的元素的和是一个平方数字。判断给出的数组的所有排列中，有多少个不同的排列是可平方的。

## 解题方法

### 回溯法

这个题的问题规模只有12个，也就是提醒我们可以使用O(N!)的算法，所以可以直接使用回溯法。

首先要排序使得相同的数字都排列在一起，这个题的回溯策略是使用visited数组表示每个数字是否用过了，从起点位置0开始，每次向后遍历，如果后面的这个数字没有用过，并且如果前面的数字和它相同、那么前面的数字也没有用过，和前面的数字相加是可以平方的，那么把当前数字放到路径cur中，设置当前的数组访问状态为已访问，然后继续从0开始遍历即可。

这个题虽然是Hard，但是还不是很难，应该会才对。


C++代码如下：

```cpp
class Solution {
public:
    int numSquarefulPerms(vector<int>& A) {
        sort(A.begin(), A.end());
        vector<int> cur;
        vector<bool> visited(A.size());
        int res = 0;
        dfs(A, visited, res, cur);
        return res;
    }
    int squareful(int x, int y) {
        int s = sqrt(x + y);
        return s * s == x + y;
    }
    void dfs(vector<int>& A, vector<bool>& visited, int& res, vector<int>& cur) {
        if (cur.size() == A.size()) {
            ++res;
            return;
        }
        for (int i = 0; i < A.size(); ++i) {
            if (visited[i]) continue;
            if (i > 0 && !visited[i - 1] && A[i] == A[i - 1]) continue;
            if (!cur.empty() && !squareful(cur.back(), A[i])) continue;
            cur.push_back(A[i]);
            visited[i] = true;
            dfs(A, visited, res, cur);
            visited[i] = false;
            cur.pop_back();
        }
    }
};
```

参考资料：https://zxi.mytechroad.com/blog/searching/leetcode-996-number-of-squareful-arrays/


## 日期

2019 年 2 月 28 日 —— 二月最后一天


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/85227593
