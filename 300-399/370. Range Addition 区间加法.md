- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/range-addition/

## 题目描述

Assume you have an array of length `n` initialized with all 0's and are given `k` update operations.

Each operation is represented as a triplet: `[startIndex, endIndex, inc]` which increments each element of subarray `A[startIndex ... endIndex]` (`startIndex` and `endIndex` inclusive) with inc.

Return the modified array after all `k` operations were executed.

Example:

    Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
    Output: [-2,0,3,5,3]
    Explanation:
    
    Initial state:
    [0,0,0,0,0]
    
    After applying operation [1,3,2]:
    [0,2,2,2,0]
    
    After applying operation [2,4,3]:
    [0,2,5,5,3]
    
    After applying operation [0,2,-2]:
    [-2,0,3,5,3]


## 题目大意

假设你有一个长度为 n 的数组，初始情况下所有的数字均为 0，你将会被给出 k​个更新的操作。
其中，每个操作会被表示为一个三元组：[startIndex, endIndex, inc]，你需要将子数组 A[startIndex ... endIndex]（包括 startIndex 和 endIndex）增加 inc。
请你返回 k 次操作后的数组。


## 解题方法

### 只修改区间起终点

我第一次做的时候，把[start,end]区间内的所有元素进行了遍历修改，会导致超时。

看了官方解答之后明白，哦，原来只用修改起始位置和结束位置就行了，让区间起点+=inc，区间终点-=inc，区间中间的部分**暂时**不用更新。最后从左到右再遍历一次，累计求和并修改每个位置的值。

总的时间复杂度是O(N + k)，空间复杂度是O(1).

C++代码如下：

```cpp
class Solution {
public:
    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
        vector<int> res(length, 0);
        for (auto& up : updates) {
            int start = up[0], end = up[1], inc = up[2];
            res[start] += inc;
            if (end < length - 1)
                res[end + 1] -= inc;
        }
        int cursum = 0;
        for (int i = 0; i < length; ++i) {
            cursum += res[i];
            res[i] = cursum;
        }
        return res;
    }
};
```

参考资料：https://leetcode-cn.com/problems/range-addition/solution/qu-jian-jia-fa-by-leetcode/

## 日期

2019 年 9 月 18 日 —— 今日又是九一八


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/100977773
