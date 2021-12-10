

- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/minimum-absolute-difference/

## 题目描述

Given an array of distinct integers `arr`, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair `[a, b]` follows

- `a, b` are from `arr`
- `a < b`
- `b - a` equals to the minimum absolute difference of any two elements in `arr`

Example 1:

    Input: arr = [4,2,1,3]
    Output: [[1,2],[2,3],[3,4]]
    Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:

    Input: arr = [1,3,6,10,15]
    Output: [[1,3]]

Example 3:
    
    Input: arr = [3,8,-10,23,19,-4,-14,27]
    Output: [[-14,-10],[19,23],[23,27]]
     

Constraints:

1. `2 <= arr.length <= 10^5`
1. `-10^6 <= arr[i] <= 10^6`


## 题目大意

给出了一个由不同数字构成的数组，哪些数字的差等于所有数字之差的最小值。

## 解题方法

### 排序

这个题肯定要先求所有数字差的最小值，暴力算是O(N^2)不可取。我们知道两个数字差最小，肯定是这两个数字比较接近，所以我们可以先排序，然后找到相邻数字的差的最小值。

找出所有数字差的最小值之后，再遍历一次，找出哪些相邻的数字差等于该最小值就行了。

C++代码如下：

```cpp
class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        const int N = arr.size();
        sort(arr.begin(), arr.end());
        int min_diff = INT_MAX;
        for (int i = 0; i < N - 1; ++i) {
            min_diff = min(min_diff, arr[i + 1] - arr[i]);
        }
        vector<vector<int>> res;
        for (int i = 0; i < N - 1; ++i) {
            if (arr[i + 1] - arr[i] == min_diff) {
                res.push_back({arr[i], arr[i + 1]});
            }
        }
        return res;
    }
};
```

## 日期

2019 年 9 月 22 日 —— 熬夜废掉半条命


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/101121394
